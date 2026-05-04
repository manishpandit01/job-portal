from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from jobportal.models import AboutUs, Category, JobPost, Testimonial, Company
from django.utils import timezone
from datetime import timedelta  # noqa: F401

# Create your views here.


class HomeView(TemplateView):
    template_name = "jobportal/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.all()
        
        context["vacancy_count"]=JobPost.objects.count()

        context["featured_jobs"] = JobPost.objects.select_related(
            "company", "category").order_by("-created_at")[:6]

        context["testimonials"] = Testimonial.objects.order_by(
            "-created_at")[:3]

        context["companies"] = Company.objects.order_by("-created_at")[:6]

        return context

class AboutView(TemplateView):
    template_name="jobportal/about.html"
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["about_us"]=AboutUs.objects.all()
        return context
 
class CategoryListView(ListView):
    model=JobPost
    template_name="jobportal/list/list.html"
    context_object_name="posts"
    
    def get_queryset(self):
        category_id=self.kwargs.get('category_id')
        if category_id:
            return JobPost.objects.filter(category_id=category_id).order_by("-created_at")
    
        return JobPost.objects.all().order_by("-created_at")
    