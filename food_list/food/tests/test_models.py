import pytest
from django.core.exceptions import ValidationError

from ..models import Item


@pytest.mark.django_db
def test_item_name_not_over_200_chars():
	with pytest.raises(ValidationError):
		test_instance = Item(name='a' * 201, description='a', price=0, image='a')
		test_instance.full_clean()


def test_item_description_not_over_200_chars():
	with pytest.raises(ValidationError):
		test_instance = Item(name='a', description='a' * 201, price=0, image='a')
		test_instance.full_clean()


def test_item_image_not_over_200_chars():
	with pytest.raises(ValidationError):
		test_instance = Item(name='a', description='a', price=0, image='a' * 501)
		test_instance.full_clean()
