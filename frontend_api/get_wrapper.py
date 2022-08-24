from django.http import HttpResponse
from .blog_api import BlogApi

def get_wrapper(request):
    action = request.GET.get('action')
    if action=='blog':
        ret = BlogApi.blog_display(request)
        return HttpResponse(ret)