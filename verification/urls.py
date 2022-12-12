from django.urls import path, include
from verification.views import Register, Otp_checker
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('register', Register, basename='register')
router.register('otp', Otp_checker, basename='otp')
urlpatterns = []+router.urls