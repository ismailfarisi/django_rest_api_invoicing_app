from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns =[
    path('',views.getRoutes),
    path('invoices/',views.InvoiceListView.as_view()),
    path('invoices/<int:pk>/',views.InvoiceView.as_view()),
    path('companies/',views.CompanyListView.as_view()),
    path('companies/<int:pk>/',views.CompanyView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)