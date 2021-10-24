from django.shortcuts import render ,get_object_or_404
from .models import blog

def all_blog(request):
    all_blogs = blog.objects.order_by('-date_time')
    return render(request,'blog/all_blogs.html',{'all_blogs':all_blogs})

def detail(request,blog_id):
    BLOG = get_object_or_404(blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':BLOG})
