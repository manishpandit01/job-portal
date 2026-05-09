from django.contrib import messages

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView
from jobportal.models import AboutUs, Category, Contact, JobPost, Testimonial, Company
from django.utils import timezone
from datetime import timedelta  # noqa: F401
from django.db.models import Count
from jobportal.forms import ContactForm
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
 
class JobCategoryView(ListView):
    model=Category
    template_name="jobportal/category/category.html"
    context_object_name="categories"
    
    def get_queryset(self):
       
        return Category.objects.annotate(job_count=Count("jobpost"))
       
    
    
class CategoryListView(ListView):
    model=JobPost
    template_name="jobportal/list/list.html"
    context_object_name="posts"
    
    def get_queryset(self):
        return JobPost.objects.all().order_by("-created_at")
    
class TestimonialView(ListView):
    model=Testimonial
    template_name="jobportal/testimonial/testimonial.html"
    context_object_name="testimonials"
    
class ContactCreateView(CreateView):
    model=Contact
    template_name="jobportal/contact.html"
    form_class=ContactForm
    success_url=reverse_lazy("contact")
    success_message="your message has been sent sucessfully"
    
    def form_invalid(self, form):
        messages.error(self.request,"There was an error sending your message.pleasecheck the form.")
        return super().form_invalid(form)