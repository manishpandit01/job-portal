from django.urls import path
from jobportal import views

urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
]

