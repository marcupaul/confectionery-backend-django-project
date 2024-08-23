from django.urls import path
from .views import FridgeList, FridgeDetail, ConfectionList, ConfectionDetail, RatList, RatDetail, RatWeightFilter, \
    FridgeRatList, FridgeOrderedList, FridgeOrderedRatAmount

urlpatterns = [
    path('fridge/', FridgeList.as_view()),
    path('fridge/amounts/', FridgeOrderedList.as_view()),
    path('fridge/rat_leaderboard/', FridgeOrderedRatAmount.as_view()),
    path('fridge/<int:pk>/', FridgeDetail.as_view()),
    path('fridge-rats/', FridgeRatList.as_view()),
    path('confection/', ConfectionList.as_view()),
    path('confection/<int:pk>/', ConfectionDetail.as_view()),
    path('rat/', RatList.as_view()),
    path('rat/<int:pk>/', RatDetail.as_view()),
    path('rat/fridges/', FridgeRatList.as_view()),
    path('rat/search/', RatWeightFilter.as_view()),
]