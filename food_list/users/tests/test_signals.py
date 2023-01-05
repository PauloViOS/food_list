from model_bakery import baker
from django.contrib.auth.models import User
from ..models import Profile
import pytest


@pytest.mark.django_db
def test_creates_and_saves_profile_on_user_creation():
	user = baker.make(User)
	user.save()
	profile = Profile.objects.filter(user=user)
	assert len(profile) == 1
