from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from ticket.models import Ticket

urlpatterns =[
    path('dashboard/',views.dashboard,name='dashboard'),

]
