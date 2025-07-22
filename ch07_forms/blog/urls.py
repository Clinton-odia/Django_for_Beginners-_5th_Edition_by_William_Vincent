from django.urls import path

# from .views import post_list, post_detail
from .views import BlogDetail, BlogList, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", BlogDetail.as_view(), name="post_detail"),
    path("", BlogList.as_view(), name="home"),
]
