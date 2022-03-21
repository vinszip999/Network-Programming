from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    return HttpResponse("Hello, World!")


def say_hello_html(request):
    return render(request, 'playground/hello.html')  # 만들고서 웹페이지를 보이게 할 때 쓰임


def say_bye_html(request):
    return render(request, 'playground/bye.html')
