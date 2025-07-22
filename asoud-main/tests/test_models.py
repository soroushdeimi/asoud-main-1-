import os
import django
from django.test import SimpleTestCase

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
django.setup()

from apps.users.models import User, UserProfile, UserDocument, UserColleague
from apps.product.models import ProductDiscount

class StrMethodTests(SimpleTestCase):
    def test_user_related_str_methods(self):
        user = User(mobile_number="123")
        profile = UserProfile(user=user)
        self.assertEqual(str(profile), "123")
        document = UserDocument(user=user)
        self.assertEqual(str(document), "123")
        colleague = UserColleague(user=user, mobile_number="321")
        self.assertEqual(str(colleague), "123")

    def test_productdiscount_str(self):
        class DummyProduct:
            name = "Product"
        discount = ProductDiscount(product=DummyProduct(), percentage=10)
        self.assertEqual(str(discount), "Product - 10%")
