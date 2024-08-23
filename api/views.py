from django.db.models import Count, Avg, Sum
from rest_framework import generics

from .models import Fridge, ClaimedCheese
from .models import Confection
from .models import Rat
from .serializers import FridgeSerializer, FridgeRatCountSerializer
from .serializers import FridgeExtendedSerializer
from .serializers import FridgeCountSerializer
from .serializers import ConfectionSerializer
from .serializers import ConfectionExtendedSerializer
from .serializers import RatSerializer
from .serializers import RatExtendedSerializer
from .serializers import ClaimedCheeseSerializer


class FridgeList(generics.ListCreateAPIView):
    serializer_class = FridgeSerializer
    queryset = Fridge.objects.all()


class FridgeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FridgeExtendedSerializer
    queryset = Fridge.objects.all()


class ConfectionList(generics.ListCreateAPIView):
    serializer_class = ConfectionSerializer

    def get_queryset(self):
        queryset = Confection.objects.all()
        fridge = self.request.query_params.get('fridge')
        if fridge is not None:
            queryset = queryset.filter(current_fridge=fridge)
        return queryset


class ConfectionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ConfectionExtendedSerializer
    queryset = Confection.objects.all()


class RatList(generics.ListCreateAPIView):
    serializer_class = RatSerializer
    queryset = Rat.objects.all()


class RatDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatExtendedSerializer
    queryset = Rat.objects.all()


class RatWeightFilter(generics.ListAPIView):
    serializer_class = RatSerializer

    def get_queryset(self):
        queryset = Rat.objects.all()
        min_weight = self.request.GET.get('min_weight', 0)
        if min_weight is not None:
            queryset = queryset.filter(rat_weight__gt=min_weight)
        return queryset


class FridgeRatList(generics.CreateAPIView):
    serializer_class = ClaimedCheeseSerializer
    queryset = ClaimedCheese.objects.all()


class FridgeOrderedList(generics.ListAPIView):
    serializer_class = FridgeCountSerializer
    queryset = Fridge.objects.all().annotate(confections_count=Count('confections')).order_by('-confections_count')


class FridgeOrderedRatAmount(generics.ListAPIView):
    serializer_class = FridgeRatCountSerializer
    queryset = Fridge.objects.all().annotate(rat_count=Count('rats')).order_by('-rat_count')
