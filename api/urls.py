from django.urls import path
from . import views
from .views import BlogPostList

urlpatterns = [
    path("blogposts/",views.BlogPostListCreate.as_view(),name="blogpost-view-create"),
    path("blogposts/<int:pk>/",views.BlogPOstRetrieveUpdateDestroy.as_view(),name="update"),
    path('blogpostslist/', BlogPostList.as_view(), name='blogpost-list'),
]