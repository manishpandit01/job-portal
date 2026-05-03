from django.urls import path
from jobportal import views
from django.views.generic import TemplateView

urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path('about/', views.HomeView.as_view(), name='about'),
]

