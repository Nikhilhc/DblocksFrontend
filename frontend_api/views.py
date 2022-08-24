from django.shortcuts import render
from django.template.loader import render_to_string
# Create your views here.


def HomePage(request):
    return render(request,'blog/index.html')

def posts(request):
    return render(request,'blog/all_posts.html')

def post_details(request,slug):
    return render(request,"blog/post_detail.html")