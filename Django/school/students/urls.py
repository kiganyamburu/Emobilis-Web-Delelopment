from django.urls import path


from . import views

from school.urls import urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert, name='insert'),

]