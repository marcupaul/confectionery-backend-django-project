from django.test import TestCase

from api.models import Rat, Fridge, Confection


class ConfectioneryViewTests(TestCase):
    def setUp(self):
        Rat.objects.create(rat_name="Guido", rat_species="Brown", rat_weight=300, rat_size="16")
        Rat.objects.create(rat_name="Sinclair", rat_species="White", rat_weight=100, rat_size="15")
        Fridge.objects.create(fridge_name="Fridge A", fridge_manufacturer="Beko", fridge_volume=200, fridge_description="Grey")
        Fridge.objects.create(fridge_name="Fridge B", fridge_manufacturer="Arctic", fridge_volume=200, fridge_description="White")
        Confection.objects.create(confection_name="Key Lime Pie", confection_country="USA", confection_calories=200,
                                  confection_description="Lime", current_fridge=Fridge.objects.get(id=1))
        Confection.objects.create(confection_name="Savarina", confection_country="Romania", confection_calories=200,
                                  confection_description="Dulce", current_fridge=Fridge.objects.get(id=2))
        Confection.objects.create(confection_name="Creme Brulee", confection_country="France", confection_calories=200,
                                  confection_description="Caramel", current_fridge=Fridge.objects.get(id=2))

    def test_weight_filter(self):
        filtered_rat = self.client.get('/api/rat/search/?min_weight=200')
        filtered_rat_data = filtered_rat.json()
        self.assertEqual(filtered_rat_data[0]['rat_name'], "Guido")

    def test_fridge_contents(self):
        ordered_fridges = self.client.get('/api/fridge/amounts/')
        ordered_fridges_data = ordered_fridges.json()
        self.assertEqual(ordered_fridges_data[0]['fridge_name'], "Fridge B")
