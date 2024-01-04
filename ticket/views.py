import datetime
from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Ticket
from .form import CreateTicketForm,UpdateTicketForm,AssignTicketForm,solvedTicketForm
from users.models import User
from django.contrib.auth.decorators import login_required


User= get_user_model()
# view ticket details
@login_required
def ticket_details(request,pk):
    ticket = Ticket.objects.get(pk=pk)
    context = {'ticket': ticket}
    return render(request,'ticket/ticket_details.html',context)




'''For custoumers'''
@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            #var.created_by=request.users
            var.customer=request.user
            var.status='Pending'
            var.save()
            messages.info(request,'Your massage has been successfully submitted, An eng will be assigned soon')
            return redirect('dashboard')
        else:
            messages.warning(request,'something went wrong. Please check form input')
            return redirect('created-ticket')
    else:
        form = CreateTicketForm()
        context = {'form':form}   
        return render(request,'ticket/create_ticket.html', context)
    


#updating ticket 
@login_required
def update_ticket(request,pk):
    ticket = get_object_or_404(Ticket, pk=pk)
   # ticket = Ticket.objects.get(pk=pk) 
    if request.method == 'POST':
        form = UpdateTicketForm(request.POST,instance=ticket)
        if form.is_valid():
            form.save()
            messages.info(request,'Your massage has been successfully updated')
            return redirect('customer_active_tickets')
        else:
            messages.warning(request,'something went wrong. Please check form input')
            return redirect('update_ticket')
    else:
        form = UpdateTicketForm(instance=ticket)
        context = {'form':form}   
        return render(request,'ticket/update_ticket.html', context)
    


@login_required
def customer_tickets(request):
    tikcets = Ticket.objects.filter(customer=request.user)
    context = {'tickets': tikcets}
    return render(request,'ticket/customer_tickets.html',context)

@login_required
def customer_resolved_tickets(request):
    tikcets = Ticket.objects.filter(customer=request.user , is_resloved=True).order_by('-created_on')
    context = {'tickets': tikcets}
    return render(request,'ticket/customer_resolved_tickets.html',context)

@login_required
def customer_active_tickets(request):
    tikcets = Ticket.objects.filter(customer=request.user, is_resloved=False)
    context = {'tickets': tikcets}
    return render(request,'ticket/customer_active_tickets.html',context)

'''For eng'''
#view  all active ticket queue---------------------------
@login_required
def engineer_active_tickets(request):
    tikcets = Ticket.objects.filter(engineer=request.user, is_resloved=False)
    context = {'tickets': tikcets}
    return render(request,'ticket/engineer_active_tickets.html',context)
#view  all resolved ticket queue

@login_required
def engineer_resolved_tickets(request):
    tikcets = Ticket.objects.filter(engineer=request.user , is_resloved=True).order_by('-created_on')
    context = {'tickets': tikcets}
    return render(request,'ticket/engineer_resolved_tickets.html',context)



@login_required
def ticket_queue(request):
    tickets = Ticket.objects.filter(is_assigned_to_engineer=False)
    context = {'tickets':tickets}
    return render(request, 'ticket/ticket_queue.html',context)


@login_required
def resolved_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = solvedTicketForm(request.POST,instance=ticket)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_resloved =True
            var.status= 'Resolved'
            var.save()
            messages.success(request , 'Ticket has been Resolved')
            return redirect('engineer_resolved_tickets')
        else:
            messages.warning(request,'something went wrong. Please check form input')
            return redirect('engineer_resolved_tickets')
    else:
        form = solvedTicketForm(instance=ticket)
        context = {'form':form}   
        return render(request,'ticket/resolved_ticket.html', context)
    


#For admin-----------------------------------------------
    
#all closed/ resolved ticket 
@login_required
def all_resolved_tickets(request):
    tickets=Ticket.objects.filter( is_resloved=True)
    context = {'tickets': tickets}
    return render(request,'ticket/all_resolved_tickets.html',context)


@login_required
def all_active_tickets(request):
    tickets=Ticket.objects.filter( is_resloved=False)
    context = {'tickets': tickets}
    return render(request,'ticket/all_active_tickets.html',context)


@login_required
def assign_ticket(request,pk):
    ticket = Ticket.objects.get(pk=pk) 
    if request.method == 'POST':
        form = AssignTicketForm(request.POST,instance=ticket)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_assigned_to_engineer = True 
            var.status = 'Active'
            var.save()
            messages.success(request,f'Ticket has been assigned to {var.engineer}')
            return redirect('ticket_queue')
        else:
            messages.warning(request,'something went wrong. Please check form input')
            return redirect('assign_ticket')
    else:
        form =AssignTicketForm(instance=ticket)
        form.fields['engineer'].queryset = User.objects.filter(is_engineer=True)
        context= {'form':form , 'ticket':ticket}
        return render(request,'ticket/assign_ticket.html', context)

