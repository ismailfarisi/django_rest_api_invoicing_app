from django.urls import path
from . import views

urlpatterns =[
    path('',views.getRoutes),
    path('invoice/',views.InvoiceList.as_view()),
]
