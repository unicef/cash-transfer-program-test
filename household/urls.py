from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Individual", api.IndividualViewSet)
router.register("IndividualRoleInHousehold", api.IndividualRoleInHouseholdViewSet)
router.register("Household", api.HouseholdViewSet)
router.register("BankInfo", api.BankInfoViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("household/Individual/", views.IndividualListView.as_view(), name="household_Individual_list"),
    path("household/Individual/create/", views.IndividualCreateView.as_view(), name="household_Individual_create"),
    path("household/Individual/detail/<int:pk>/", views.IndividualDetailView.as_view(), name="household_Individual_detail"),
    path("household/Individual/update/<int:pk>/", views.IndividualUpdateView.as_view(), name="household_Individual_update"),
    path("household/Individual/delete/<int:pk>/", views.IndividualDeleteView.as_view(), name="household_Individual_delete"),
    path("household/IndividualRoleInHousehold/", views.IndividualRoleInHouseholdListView.as_view(), name="household_IndividualRoleInHousehold_list"),
    path("household/IndividualRoleInHousehold/create/", views.IndividualRoleInHouseholdCreateView.as_view(), name="household_IndividualRoleInHousehold_create"),
    path("household/IndividualRoleInHousehold/detail/<int:pk>/", views.IndividualRoleInHouseholdDetailView.as_view(), name="household_IndividualRoleInHousehold_detail"),
    path("household/IndividualRoleInHousehold/update/<int:pk>/", views.IndividualRoleInHouseholdUpdateView.as_view(), name="household_IndividualRoleInHousehold_update"),
    path("household/IndividualRoleInHousehold/delete/<int:pk>/", views.IndividualRoleInHouseholdDeleteView.as_view(), name="household_IndividualRoleInHousehold_delete"),
    path("household/Household/", views.HouseholdListView.as_view(), name="household_Household_list"),
    path("household/Household/create/", views.HouseholdCreateView.as_view(), name="household_Household_create"),
    path("household/Household/detail/<int:pk>/", views.HouseholdDetailView.as_view(), name="household_Household_detail"),
    path("household/Household/update/<int:pk>/", views.HouseholdUpdateView.as_view(), name="household_Household_update"),
    path("household/Household/delete/<int:pk>/", views.HouseholdDeleteView.as_view(), name="household_Household_delete"),
    path("household/BankInfo/", views.BankInfoListView.as_view(), name="household_BankInfo_list"),
    path("household/BankInfo/create/", views.BankInfoCreateView.as_view(), name="household_BankInfo_create"),
    path("household/BankInfo/detail/<int:pk>/", views.BankInfoDetailView.as_view(), name="household_BankInfo_detail"),
    path("household/BankInfo/update/<int:pk>/", views.BankInfoUpdateView.as_view(), name="household_BankInfo_update"),
    path("household/BankInfo/delete/<int:pk>/", views.BankInfoDeleteView.as_view(), name="household_BankInfo_delete"),
)
