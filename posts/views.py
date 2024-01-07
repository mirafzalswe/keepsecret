from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Like, Hashtag
from .forms import PostForm, CommentForm, HashtagsForm
def home(request):
    form = Post.objects.all()
    return render(request, 'posts/home.html', {'form':form})




from django.shortcuts import render, get_object_or_404
from .models import Post, Like, Comment

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    likes = post.likes.all()
    comments = post.comments.all()
    context = {
        'post': post,
        'likes': likes,
        'comments': comments
    }
    return render(request, 'posts/post_detail.html', context)



@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('home-page')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'posts/comment.html', {'form': form})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    if Like.objects.filter(user=user, post=post).exists():
        Like.objects.filter(user=user, post=post).delete()
    else:
        Like.objects.create(user=user, post=post)
    return redirect('home-page')

@login_required
def create_hashtag(request):
    if request.method == 'POST':
        form = HashtagsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_post-page')
    else:
        form = HashtagsForm()
    return render(request, 'posts/add_hashtag.html', {'form': form})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user == request.user:
        comment.delete()

    return redirect('post-detail', post_id=comment.post.id)


def search_product(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(content__icontains=query)
    else:
        results = []

    return render(request, 'base.html', {'results': results, 'query': query})

def hashtag(request, hashtag):
    posts = Hashtag.objects.filter(name=hashtag)
    return render(request, 'posts/home.html', {'hashtag': posts})
