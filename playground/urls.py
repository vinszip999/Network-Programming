from django.urls import path

from playground import views

app_name = 'playground'
urlpatterns = [
    path('hello/', views.say_hello, name='hello'),  # playground:hello
    path('hello_html/', views.say_hello_html, name='hello_html'),  # views.say_hello_html 뒤에 괄호 없어야 하고, 문장 끝날때 꼭 , 넣어주기
    path('bye_html/', views.say_bye_html, name='bye_html'),
]
