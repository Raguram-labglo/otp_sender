from django.urls import path, include
from verification.views import Register, Otp_checker,Wether_report
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('register', Register, basename='register')
# router.register('otp', Otp_checker, basename='otp')
urlpatterns = [path('otp/', Otp_checker.as_view(), name = 'otp'),
               path('wether/', Wether_report.as_view(), name = 'weather')]+router.urls