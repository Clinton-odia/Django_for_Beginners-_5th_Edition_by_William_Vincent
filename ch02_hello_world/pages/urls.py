from django.urls import path
from .views import home_page_view, test_new_page

urlpatterns = [path("", home_page_view), path("second", test_new_page)]
