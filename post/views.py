from django.shortcuts import render, redirect, get_object_or_404
from post.forms import UserForm, SignUpForm, PostForm, CommentForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from post.models import Post, Comment,Advertisment
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.user_authenticate()
            if user:
                auth_login(request, user)
                return redirect('home')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'signup/login.html', context)


def logout_view(request):
    auth_logout(request)
    return redirect('login')


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'signup/registration.html', context)


def home(request):
    head_advertisement = Advertisment.objects.all().order_by('-id')[:1]
    post_data = Post.objects.exclude(image='')[:12]
    post_without_images = Post.objects.filter(image="")[:9]
    context = {
        'head_advertisement':head_advertisement,
        'post_without_images':post_without_images,
        'post_data': post_data,
    }
    return render(request, 'home.html', context)

def dashboard(request,username):
    return render(request,'dashboard.html')

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_text = Comment.objects.filter(comment_post=post_id).order_by('-date')[:5]
    comment_form = CommentForm()
    context = {
        'post': post,
        'comment': comment_form,
        'comment_text': comment_text,
    }
    return render(request, 'page.html', context)


def createpost(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_data = post_form.save(commit=False)
            post_data.created_by = request.user
            post_data.save()
            return redirect('post', post_id=post_data.post_id)
    else:
        postform = PostForm()
    context = {
        'form': postform,
    }
    return render(request,'ckeditor/postpage.html',context)

def makepost(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_data = post_form.save(commit=False)
            post_data.created_by = request.user
            post_data.save()
            return redirect('post', post_id=post_data.post_id)


def add_comment(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.comment_by = request.user
            comment.comment_post = post
            comment.save()
            return redirect('post', post_id)
        else:
            return redirect('post', post_id)
