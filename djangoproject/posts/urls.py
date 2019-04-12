from django.urls import path
from . import views

urlpatterns = [
    path('^$', views.index, name='index') # '^' --> Starts with; '$' --> ends with just '^$' means starts and ends with nothing

]

