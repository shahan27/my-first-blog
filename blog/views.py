from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
                        
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
                                    
def user_post_list(request, pk):
    posts = Post.objects.filter(author__pk=pk, published_date__lte=timezone.now()).order_by('published_date')
    author = User.objects.get(pk=pk)
    return render(request, 'blog/user_detail.html', {'posts': posts, 'author': author})
                                                    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
                                                                
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
            return render(request, 'blog/post_edit.html', {'form': form})
                                                                                                        
                                                                                                        
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        return render(request, 'blog/post_detail.html', {'post': post})