from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('<str:page>/', views.other_page, name='other'),
    path('', views.IndexView.as_view(), name='index'),
]
