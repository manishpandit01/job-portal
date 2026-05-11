from django.urls import path
from jobportal import views
urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path('about/', views.AboutView.as_view(), name='about'),
    path("job-category/",views.JobCategoryView.as_view(),name='category'),
    path("job-catgeory/<int:pk>/",views.CategoryJobListView.as_view(),name="category_jobs"),
    path("testimonial/",views.TestimonialView.as_view(),name="testimonial"),
    path("contact/",views.ContactCreateView.as_view(),name="contact"),
    path("job-list/",views.CategoryListView.as_view(),name="job_list"),
    path("job-detail/<int:pk>",views.PostDetailView.as_view(),name="job_detail"),
]

