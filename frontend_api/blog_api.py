from django.http import JsonResponse

class BlogApi:
    def __init__(self,request,blog_id=None,blog_name=None):
        self.request = request
        self.blog_id = blog_id
        self.blog_name=blog_name

    def blog_display(self):
        return JsonResponse({'ret':True,'result':True})