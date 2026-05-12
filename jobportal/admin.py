from django.contrib import admin
from jobportal import forms
from jobportal.models import Category,Company,JobApplication,JobPost,Contact,Testimonial
from unfold.admin import ModelAdmin

# Register your models here.
admin.site.register(Category)
admin.site.register(Company)
#admin.site.register(JobPost)
admin.site.register(JobApplication)
admin.site.register(Testimonial)
admin.site.register(Contact)

@admin.register(JobPost)
class JobAdmin(ModelAdmin):
   list_dsiplay=("title","company","location")