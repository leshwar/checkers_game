from django.urls import path
from checkers.views import *

app_name='checkers'

urlpatterns = [
    path('',CheckerView.as_view(), name='checkers'),
]
