from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index, name='index'),
    path('process_money/<str:place>', views.process_money),
    path('reset', views.reset),
    
]