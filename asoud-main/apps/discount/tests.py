from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from apps.discount.models import Discount
from apps.product.models import Product
from apps.users.models import User

import uuid


class DiscountModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(mobile_number="09123456789", password="test")
        self.content_type = ContentType.objects.get_for_model(Product)

    def test_valid_discount(self):
        """Discount should be valid when not expired and below usage limit."""
        discount = Discount.objects.create(
            owner=self.user,
            content_type=self.content_type,
            object_id=uuid.uuid4(),
            code="VALID",
            percentage=10,
            expiry=timezone.now() + timezone.timedelta(days=1),
            limitation=5,
            consumed=1,
        )

        self.assertTrue(discount.is_valid())

    def test_expired_discount(self):
        """An expired discount should be invalid."""
        discount = Discount.objects.create(
            owner=self.user,
            content_type=self.content_type,
            object_id=uuid.uuid4(),
            code="EXPIRED",
            percentage=10,
            expiry=timezone.now() - timezone.timedelta(days=1),
            limitation=5,
        )

        self.assertFalse(discount.is_valid())

    def test_usage_over_limitation(self):
        """Discount usage equal to or greater than limitation is invalid."""
        discount = Discount.objects.create(
            owner=self.user,
            content_type=self.content_type,
            object_id=uuid.uuid4(),
            code="OVERUSE",
            percentage=10,
            expiry=timezone.now() + timezone.timedelta(days=1),
            limitation=2,
            consumed=2,
        )

        self.assertFalse(discount.is_valid())
