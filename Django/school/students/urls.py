from django.urls import path


from .

from school.urls import urlpatterns

urlpatterns = [
    path('', views.index, name='index'),

]