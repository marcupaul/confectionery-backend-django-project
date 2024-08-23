from django.db import models


class Fridge(models.Model):
    fridge_name = models.CharField(max_length=64)
    date_added = models.DateField(auto_now_add=True)
    fridge_manufacturer = models.CharField(max_length=64)
    fridge_volume = models.IntegerField(default=0)
    fridge_description = models.CharField(max_length=256)

    def __str__(self):
        return self.fridge_name


class Confection(models.Model):
    confection_name = models.CharField(max_length=64)
    date_added = models.DateField(auto_now_add=True)
    confection_country = models.CharField(max_length=64)
    confection_calories = models.IntegerField(default=0)
    confection_description = models.CharField(max_length=256)
    current_fridge = models.ForeignKey(Fridge, related_name='confections', on_delete=models.CASCADE)

    def __str__(self):
        return self.confection_name


class Rat(models.Model):
    rat_name = models.CharField(max_length=64)
    date_added = models.DateField(auto_now_add=True)
    rat_species = models.CharField(max_length=64)
    rat_weight = models.IntegerField(default=0)
    rat_size = models.IntegerField(default=0)
    fridges = models.ManyToManyField(Fridge, related_name='rats', through='ClaimedCheese', blank=True)

    def __str__(self):
        return self.rat_name


class ClaimedCheese(models.Model):
    fridge = models.ForeignKey(Fridge, related_name='cheese_fridge', on_delete=models.CASCADE)
    rat = models.ForeignKey(Rat, related_name='cheese_rat', on_delete=models.CASCADE)
    cheese_amount = models.IntegerField(default=0)
    cheese_type = models.CharField(max_length=64)

    class Meta:
        unique_together = [['fridge', 'rat']]
