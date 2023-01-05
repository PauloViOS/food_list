from django.urls import path

from . import views

app_name = 'food'
urlpatterns = [
	path('', views.IndexClassView.as_view(), name='index'),
	path('item/', views.item, name='item'),
	path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
	path('add/', views.AddItem.as_view(), name='add_item'),
	path('edit/<int:item_id>', views.edit_item, name='edit_item'),
	path('delete/<int:item_id>', views.delete_item, name='delete_item'),
]
