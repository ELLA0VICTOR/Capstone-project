from django.test import TestCase
from restaurant.models import Menu_table
from restaurant.serializers import Menuserializer

class MenuViewSetTest(TestCase):
    def setUp(self):
        Menu_table.objects.create(title='Item1', price=10, inventory=50)
        Menu_table.objects.create(title='Item2', price=20, inventory=30)

    def test_getall(self):
        response = self.client.get('/menu/')
        menu_items = Menu_table.objects.all()
        serializer = Menuserializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)