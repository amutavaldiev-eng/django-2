from django.urls import path
from .views import *



urlpatterns = [
    path('ragister', register),
    path('python', python),
    path('c', c),
    path('c++', cpp),
    path('java', java),
    path('end', end)
 
]