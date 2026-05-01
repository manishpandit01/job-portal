from django.shortcuts import render
from django.views.generic import TemplateView
from jobportal.models import Category, JobPost, Testimonial, Company
from django.utils import timezone
from datetime import timedelta  # noqa: F401

# Create your views here.


class HomeView(TemplateView):
    template_name = "jobportal/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.all()

        context["featured_jobs"] = JobPost.objects.select_related(
            "company", "category"
        ).order_by("-published_at")[:6]

        context["testimonials"] = Testimonial.objects.order_by(
            "-created_at")[:3]

        context["companies"] = Company.objects.order_by("-created_at")[:6]

        return context
