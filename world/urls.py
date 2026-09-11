from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path("", views.home, name="home"),

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