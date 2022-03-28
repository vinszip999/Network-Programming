from django.urls import path

from stayc import views

app_name = 'stayc'
urlpatterns = [
    path('j/', views.show_j, name='j'),
    path('yoon/', views.show_yoon, name='yoon'),
]
