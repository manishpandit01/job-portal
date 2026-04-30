from django.db import models

# Create your models here.
class TimeStamp(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True
        
class Category(TimeStamp):
    name=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering=["name"]
        verbose_name="category"
        verbose_name_plural="Categories"
        
class Company(TimeStamp):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    website=models.URLField(blank=True)
    location=models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
        
class JobPost(TimeStamp):
    JOB_TYPE=(
        ("full_time","Full Time"),
        ("part_time","Part Time"),
        ("internship","Internship"),
        ("remote","Remote"),
    )
    
    title=models.CharField(max_length=140)
    logo=models.ImageField( upload_to="company_logo/",blank=False)
    location=models.CharField(max_length=150)
    job_type=models.CharField(max_length=100,choices=JOB_TYPE)
    salary=models.CharField(max_length=100,blank=True)
    description=models.TextField()
    responsibility=models.TextField()
    qualification=models.TextField()
    summary=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class JobAPplication(TimeStamp):
    job=models.ForeignKey(JobPost,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    portfolio_website=models.URLField(blank=True)
    resume=models.FileField(upload_to="resumes/")
    cover_letter=models.TextField()
    
    def __str__(self):
        return f"{self.name}"

