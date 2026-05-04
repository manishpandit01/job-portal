from django.urls import path
from jobportal import views
urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path('about/', views.AboutView.as_view(), name='about'),
    path("category-list/<int:category_id>/",views.CategoryListView.as_view(),name='category_list'),
]

