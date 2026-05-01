from django.contrib import admin
from jobportal.models import Category,Company,JobApplication,JobPost,Contact,Testimonial

# Register your models here.
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(JobPost)
admin.site.register(JobApplication)
admin.site.register(Testimonial)
admin.site.register(Contact)