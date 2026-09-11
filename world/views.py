from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

from .models import Post, Category, Comment, Like


def home(request):
    query = request.GET.get("q", "")

    posts = Post.objects.all().order_by("-created_at")

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    categories = Category.objects.all()

    context = {
        "posts": posts,
        "categories": categories,
        "query": query,
    }

    return render(request, "blog/home.html", context)


@login_required
def dashboard(request):
    posts = Post.objects.filter(
        author=request.user
    ).order_by("-created_at")

    total_posts = posts.count()
    total_comments = Comment.objects.filter(
        post__author=request.user
    ).count()
    total_likes = Like.objects.filter(
        post__author=request.user
    ).count()

    context = {
        "posts": posts,
        "total_posts": total_posts,
        "total_comments": total_comments,
        "total_likes": total_likes,
    }

    return render(request, "blog/dashboard.html", context)


@login_required
def create_post(request):

    categories = Category.objects.all()

    if request.method == "POST":

        title = request.POST.get("title")
        content = request.POST.get("content")
        category_id = request.POST.get("category")
        image = request.FILES.get("image")

        category = None

        if category_id:
            category = Category.objects.get(id=category_id)

        Post.objects.create(
            author=request.user,
            title=title,
            content=content,
            category=category,
            image=image
        )

        return redirect("dashboard")

    return render(
        request,
        "blog/post_form.html",
        {"categories": categories}
    )


@login_required
def edit_post(request, id):

    post = get_object_or_404(
        Post,
        id=id,
        author=request.user
    )

    categories = Category.objects.all()

    if request.method == "POST":

        post.title = request.POST.get("title")
        post.content = request.POST.get("content")

        category_id = request.POST.get("category")

        if category_id:
            post.category = Category.objects.get(id=category_id)

        if request.FILES.get("image"):
            post.image = request.FILES.get("image")

        post.save()

        return redirect("dashboard")

    return render(
        request,
        "blog/post_form.html",
        {
            "post": post,
            "categories": categories
        }
    )


@login_required
def delete_post(request, id):

    post = get_object_or_404(
        Post,
        id=id,
        author=request.user
    )

    if request.method == "POST":
        post.delete()
        return redirect("dashboard")

    return render(
        request,
        "blog/post_confirm_delete.html",
        {"post": post}
    )


def post_detail(request, id):

    post = get_object_or_404(Post, id=id)

    comments = post.comments.all().order_by("-created_at")

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments
        }
    )


@login_required
def add_comment(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == "POST":

        text = request.POST.get("text")

        if text:
            Comment.objects.create(
                post=post,
                user=request.user,
                text=text
            )

    return redirect("post_detail", id=id)


@login_required
def like_post(request, id):

    post = get_object_or_404(Post, id=id)

    like, created = Like.objects.get_or_create(
        post=post,
        user=request.user
    )

    if not created:
        like.delete()

    return redirect("post_detail", id=id)


def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "blog/register.html",
                {"error": "Username already exists"}
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "blog/register.html")


def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        return render(
            request,
            "blog/login.html",
            {"error": "Invalid username or password"}
        )

    return render(request, "blog/login.html")


def user_logout(request):

    logout(request)

    return redirect("home")


# Create your views here.
def index(request):
    return render(request, "world/index.html")
