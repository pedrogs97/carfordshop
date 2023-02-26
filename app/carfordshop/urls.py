from django.urls import path
from . import views

urlpatterns = [
    path(
        "owners/",
        views.OwnerListCreateView.as_view(),
        name="owner_list_create",
    ),
    path(
        "owners/<int:pk>/",
        views.OwnerRetrieveUpdateDestroyView.as_view(),
        name="owner_retrieve_update_destroy",
    ),
    path("cars/", views.CarListCreateView.as_view(), name="car_list_create"),
    path(
        "cars/<int:pk>/",
        views.CarRetrieveUpdateDestroyView.as_view(),
        name="car_retrieve_update_destroy",
    ),
]
