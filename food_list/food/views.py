from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import ItemForm
from .models import Item


class IndexClassView(ListView):
	model = Item
	template_name = 'food/index.html'
	context_object_name = 'item_list'


def item(request):
	return HttpResponse("This is an item view")


class FoodDetail(DetailView):
	model = Item
	template_name = 'food/detail.html'


class AddItem(CreateView):
	model = Item
	fields = ['name', 'description', 'price', 'image']
	template_name = 'food/item-form.html'

	def form_valid(self, form):
		form.instance.user_name = self.request.user

		return super().form_valid(form)


def edit_item(request, item_id):
	item_instance = Item.objects.get(id=item_id)
	form = ItemForm(request.POST or None, instance=item_instance)

	if form.is_valid():
		form.save()
		return redirect('food:index')
	return render(request, 'food/item-form.html', {'form': form, 'item': item_instance})


def delete_item(request, item_id):
	item_instance = Item.objects.get(id=item_id)

	if request.method == "POST":
		item_instance.delete()
		return redirect('food:index')

	return render(request, 'food/item-delete.html', {'item': item_instance})
