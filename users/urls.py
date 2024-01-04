from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns =[
    path('register_customer/',views.register_customer,name='register_customer'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)