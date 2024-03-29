from django.shortcuts import render, HttpResponse
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myblogApp/post_list.html',{'posts':posts})


def index(request):
    return render(request, 'myblogApp/index.html', {'posts':posts})



