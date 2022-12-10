from django.urls import path, include
from verification.views import Register
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('register', Register, basename='register')
urlpatterns = []+router.urls