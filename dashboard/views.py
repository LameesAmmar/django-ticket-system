from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import User
from ticket.models import Ticket
from django.http import HttpResponse

# Create your views here.
@login_required
def dashboard(request):  
    if request.user.is_customer:  
        tickets = Ticket.objects.filter(customer=request.user).count 
        active_tickets = Ticket.objects.filter(customer=request.user, is_resloved=False).count
        colsed_tickets = Ticket.objects.filter(customer=request.user, is_resloved=True).count
        context = {'tickets':tickets,'colsed_tickets':colsed_tickets,'active_tickets':active_tickets}        
        return render(request,'dashboard/customer_dashboard.html')
    if request.user.is_engineer:
        tickets = Ticket.objects.filter(engineer=request.user).count 
        active_tickets = Ticket.objects.filter(engineer=request.user, is_resloved=False).count
        colsed_tickets = Ticket.objects.filter(engineer=request.user, is_resloved=True).count
        context = {'tickets':tickets,'colsed_tickets':colsed_tickets,'active_tickets':active_tickets}
        return render(request,'dashboard/engineer_dashboard.html',context)
    if request.user.is_superuser:
        tickets = Ticket.objects.count 
        active_tickets = Ticket.objects.filter(is_resloved=False).count
        colsed_tickets = Ticket.objects.filter(is_resloved=True).count       
        queue_tickets = Ticket.objects.filter(is_assigned_to_engineer=False).count   
        context = {'tickets':tickets,'colsed_tickets':colsed_tickets,'active_tickets':active_tickets , 'queue_tickets': queue_tickets}        
        return render(request,'dashboard/admin_dashboard.html')


