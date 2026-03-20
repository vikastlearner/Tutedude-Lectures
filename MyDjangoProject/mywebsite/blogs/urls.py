from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home_page"), # 127.0.0.1/blogs
    path('allposts', views.blogposts, name="allpost"), # 127.0.0.1/blogs/allposts
    # path('allposts/python-intro', views.python_intro),
    # path('allposts/django-intro', views.django_basic),
    # path('allposts/books', views.python_oops)
# Dynamic Response
    # path('allposts/<int:blog>', views.blogpost_number),
    # path('allposts/<str:blog>', views.blog_post) # 127.0.0.1/blogs/allposts/<anything>
    path('allposts/<slug:blog>', views.blog_post, name="blog_post")
]
