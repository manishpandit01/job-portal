from django.contrib import messages

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from jobportal.models import AboutUs, Category, Contact, JobPost, Testimonial, Company
from django.utils import timezone
from datetime import timedelta  # noqa: F401
from django.db.models import Count
from jobportal.forms import ContactForm, JobApplicationForm
# Create your views here.


class HomeView(TemplateView):
    template_name = "jobportal/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.annotate(
            total_jobs=Count("jobpost"))
        
        # context["vacancy_count"]=JobPost.objects.count()

        context["featured_jobs"] = JobPost.objects.select_related(
            "company", "category").order_by("-created_at")[:3]

        context["testimonials"] = Testimonial.objects.order_by(
            "-created_at")[:3]

        context["companies"] = Company.objects.order_by("-created_at")[:4]

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
        return Category.objects.annotate(total_jobs=Count("jobpost"))
       
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
    
class PostDetailView(DetailView):
    model=JobPost
    template_name="jobportal/detail/detail.html"
    context_object_name="post"
    
    def get_queryset(self):
        return JobPost.objects.all().order_by("-created_at")

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["form"]=JobApplicationForm()
        return context
    
    def post(self,request,*args,**kwargs):
        self.object=self.get_object()
        form=JobApplicationForm(request.POST,request.FILES)
        
        if form.is_valid():
            application=form.save(commit=False)
            application.job=self.object
            application.save()
            
            messages.success(request,"Application submitted sucessfully.")
            return redirect("job_detail",pk=self.object.pk)
        
        context=self.get_context_data()
        context["form"]=form
        return self.render_to_response(context)
    
class CategoryJobListView(ListView):
    model=JobPost
    template_name="jobportal/category/job.html"
    context_object_name="posts"
    
    def get_queryset(self):
        return JobPost.objects.filter(category_id=self.kwargs["pk"]).select_related("company","category")
        