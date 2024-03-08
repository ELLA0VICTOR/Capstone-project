from django.test import TestCase
from restaurant.models import Menu_table
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu_table.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream: 80")

