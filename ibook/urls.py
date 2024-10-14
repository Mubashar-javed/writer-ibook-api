from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ProjectListViewSet, WordsMeaningAPI

router = DefaultRouter()
router.register("projects", ProjectListViewSet, basename="project")

urlpatterns = [
    path("words/<str:word>/", WordsMeaningAPI.as_view(), name="words_meaning"),
] + router.urls
