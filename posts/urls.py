from django.urls import path

from .views import HomepageWiev

urlpatterns = [
    path('',HomepageWiev.as_view(),name='home')
]