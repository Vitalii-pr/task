from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.restaurants import views

router = DefaultRouter()

router.register('restaurants', views.RestaurantModelViewSet, basename='restaurant')
router.register('menu', views.MenuModelViewSet, basename='menu')

urlpatterns = [
    path('', include(router.urls)),
    path('vote_for_menu/<int:pk>', views.vote_for_menu),
    path('add_menu/', views.upload_menu_to_restaurant),
    path('get_ranking/', views.get_ranking),
]


