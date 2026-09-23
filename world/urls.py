from django.urls import path
from . import views

urlpatterns = [

     path("", views.home, name="home"),
    path("blogs/", views.blogs, name="blogs"),
    path("get-started/", views.get_started, name="get_started"),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "post/<int:id>/",
        views.post_detail,
        name="post_detail"
    ),

    path(
        "post/create/",
        views.create_post,
        name="create_post"
    ),

    path(
        "post/<int:id>/edit/",
        views.edit_post,
        name="edit_post"
    ),

    path(
        "post/<int:id>/delete/",
        views.delete_post,
        name="delete_post"
    ),

    path(
        "post/<int:id>/comment/",
        views.add_comment,
        name="add_comment"
    ),

    path(
        "post/<int:id>/like/",
        views.like_post,
        name="like_post"
    ),

    path(
        "register/",
        views.register,
        name="register"
    ),

    path(
        "login/",
        views.user_login,
        name="login"
    ),

    path(
        "logout/",
        views.user_logout,
        name="logout"
    ),
]