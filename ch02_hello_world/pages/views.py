from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page_view(request):
    return HttpResponse("Hello world")


def test_new_page(request):
    return HttpResponse("Second page")
