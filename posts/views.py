from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    # If the mehod is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # yes, save
             form.save()
               
            # Redirect to Home
             return HttpResponseRedirect('/')
          
           
        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())
            
            
    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    form=PostForm()


    # show
    return render(request, 'posts.html',
                    {'posts':posts})


def delete(request, post_id): 
    # Find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')


def My_like(request, post_id):
    post = Post.objects.get(id=post_id)
    new_value = post.likes + 1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')    
    

def edit(request, post_id):
    posts = Post.objects.get(id=post_id)
    if request.method == 'GET':
        posts=Post.objects.get(id=post_id)
        return render(request, "edit.html", {"posts":posts})
    if request.method == 'POST':
        #editposts= posts.objects.get(id=post_id)
        form = PostForm(request.POST, request.FILES, instance=posts)

        # If the form is valid
        if form.is_valid():
            # yes, save
             form.save()
               
            # Redirect to Home
             return HttpResponseRedirect('/')
          
           
        else:
            # No, Show Error
            return HttpResponseRedirect('not valid')

            


    