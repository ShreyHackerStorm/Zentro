from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('set-allowance/', views.set_allowance, name='set_allowance'),
    path('add-expenses/', views.add_expenses, name='add_expenses'),
    path('view-spending/', views.view_spending, name='view_spending'),
]