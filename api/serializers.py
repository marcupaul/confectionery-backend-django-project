from rest_framework import serializers
from .models import Fridge
from .models import Confection
from .models import Rat
from .models import ClaimedCheese


class FridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fridge
        fields = ('__all__')

    def validate_fridge_description(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Description is too short.")
        return value

class ConfectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confection
        fields = ('__all__')

    def validate_confection_description(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Description is too short.")
        return value


class RatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rat
        fields = ('__all__')

    def validate_rat_species(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Species name is too short.")
        return value


class ConfectionExtendedSerializer(serializers.ModelSerializer):
    fridge_data = FridgeSerializer(source='current_fridge', read_only=True)

    class Meta:
        model = Confection
        fields = ('confection_name', 'date_added', 'confection_country', 'confection_calories', 'confection_description', 'fridge_data')


class FridgeExtendedSerializer(serializers.ModelSerializer):
    confections = ConfectionSerializer(many=True, read_only=True)
    rats = RatSerializer(many=True, read_only=True)

    class Meta:
        model = Fridge
        fields = ('fridge_name', 'date_added', 'fridge_manufacturer', 'fridge_volume', 'fridge_description', 'confections', 'rats')


class FridgeCountSerializer(serializers.ModelSerializer):
    confections_count = serializers.IntegerField(source='confections.count', read_only=True)

    class Meta:
        model = Fridge
        fields = ('fridge_name', 'date_added', 'fridge_manufacturer', 'fridge_volume', 'fridge_description', 'confections_count')


class FridgeRatCountSerializer(serializers.ModelSerializer):
    rat_count = serializers.IntegerField(source='rats.count', read_only=True)

    class Meta:
        model = Fridge
        fields = ('fridge_name', 'date_added', 'fridge_manufacturer', 'fridge_volume', 'fridge_description', 'rat_count')


class ClaimedCheeseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimedCheese
        fields = ('fridge', 'rat', 'cheese_amount', 'cheese_type')


class RatExtendedSerializer(serializers.ModelSerializer):
    fridges = FridgeSerializer(many=True, read_only=True)
    cheeses = ClaimedCheeseSerializer(many=True, read_only=True)

    class Meta:
        model = Rat
        fields = ('rat_name', 'date_added', 'rat_species', 'rat_weight', 'rat_size', 'fridges', 'cheeses')
