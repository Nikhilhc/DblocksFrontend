from django.http import HttpResponse
from .blog_api import BlogApi

def post_wrapper(request):
    action = request.POST.get('action')
    if action=='blog':
        ret = BlogApi.blog_display(request)
        return HttpResponse(ret)