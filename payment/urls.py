from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Program", api.ProgramViewSet)
router.register("Payment", api.PaymentViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("payment/Program/", views.ProgramListView.as_view(), name="payment_Program_list"),
    path("payment/Program/create/", views.ProgramCreateView.as_view(), name="payment_Program_create"),
    path("payment/Program/detail/<int:pk>/", views.ProgramDetailView.as_view(), name="payment_Program_detail"),
    path("payment/Program/update/<int:pk>/", views.ProgramUpdateView.as_view(), name="payment_Program_update"),
    path("payment/Program/delete/<int:pk>/", views.ProgramDeleteView.as_view(), name="payment_Program_delete"),
    path("payment/Payment/", views.PaymentListView.as_view(), name="payment_Payment_list"),
    path("payment/Payment/create/", views.PaymentCreateView.as_view(), name="payment_Payment_create"),
    path("payment/Payment/detail/<int:pk>/", views.PaymentDetailView.as_view(), name="payment_Payment_detail"),
    path("payment/Payment/update/<int:pk>/", views.PaymentUpdateView.as_view(), name="payment_Payment_update"),
    path("payment/Payment/delete/<int:pk>/", views.PaymentDeleteView.as_view(), name="payment_Payment_delete"),
)
