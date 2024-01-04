from django.urls import path
from . import views

urlpatterns = [
    path('ticket_details/<int:pk>/',views.ticket_details,name='ticket_details'),
    path('customer_tickets/',views.customer_tickets,name='customer_tickets'),
    path('assign_ticket/<int:pk>/',views.assign_ticket,name='assign_ticket'),
    path('create_ticket/',views.create_ticket,name='create_ticket'),
    path('update_ticket/<int:pk>/',views.update_ticket,name='update_ticket'),
    path('customer_resolved_tickets/',views.customer_resolved_tickets,name='customer_resolved_tickets'),
    path('customer_active_tickets/',views.customer_active_tickets,name='customer_active_tickets'),
    path('ticket_queue/',views.ticket_queue,name='ticket_queue'),
    path('resolved_ticket/<int:pk>/',views.resolved_ticket,name='resolved_ticket'),
#    path('colse_ticket/<int:pk>/',views.colse_ticket,name='colse_ticket'),
#    path('workspace/',views.workspace,name='workspace'),
    path('all_active_tickets/',views.all_active_tickets,name='all_active_tickets'),
    path('all_resolved_tickets/',views.all_resolved_tickets,name='all_resolved_tickets'),
    path('engineer_active_tickets/',views.engineer_active_tickets,name='engineer_active_tickets'),
    path('engineer_resolved_tickets/',views.engineer_resolved_tickets,name='engineer_resolved_tickets'),
    path('resolved_ticket/<int:pk>/',views.resolved_ticket,name='resolved_ticket'),


]