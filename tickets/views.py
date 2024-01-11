import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ticket
from .forms import CreateTicketForm, UpdateTicketForm

#view ticket details
def ticketDetails(request, pk):
    tickets =ticket.objects.get(pk=pk)
    context = {'tickets': tickets}
    return render(request, 'tickets/ticket_details.html', context)
    

"""Customers"""

#Create ticket
def createTicket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.users
            var.tickect_status = 'Pending'
            var.save()
            messages.info(request, 'Submission is successful, An engineer will be assigned soon.')
            return redirect('dashboard')
        else:
            form = CreateTicketForm()
            context = {'form':form}
            return render(request, 'ticket/create_ticket.html', context)
        
#Update ticket

def update_ticket(request, pk):
    tickets= ticket.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateTicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Ticket info has been update')
            return redirect('dashboard')
        else:
           messages.warning(request,'Something went wrong, please check inputs')

    else:
        form = UpdateTicketForm(instance=ticket)
        context = {'form': form}
        return render(request, 'tickets/update_ticket.html', context)
    
#View all tickets

def all_tickets(request):
    tickets = ticket.objects.filter(created_by=request.users)
    context = {'tickets': tickets}
    return render(request, 'ticket/all_tickets.html', context)

"""Admin"""

#ticket queue
def ticketQueue(request):
    tickets = ticket.objects.filter(ticket_status='pending')
    context = {'tickets': tickets}
    return render(request, 'ticket/ticketQueue.html', context)

#accepting ticket from queue
def acceptTicket(request, pk):
    tickets = ticket.objects.get(pk=pk)
    ticket.assigned_to = request.users
    ticket.ticket_status = 'Active'
    ticket.accepted_date =datetime.datetime.now()
    ticket.save()
    messages.info(request, 'Ticket has been accepted.')
    return redirect('ticket-queue')

#close ticket
def closeTicket(request, pk):
    tickets = ticket.objects.get(pk=pk)
    ticket.ticket_status = 'Completed'
    ticket.closed_date =datetime.datetime.now()
    ticket.save()
    messages.info(request, 'Ticket has been resolved.')
    return redirect('ticket-queue')

#tickets being worked on
def workspace(request):
    tickets = ticket.objects.filter(assigned_to=request.users, is_resolved=False)
    context = {'tickets': tickets}
    return render(request, 'ticket/workspace.html', context)

#all closed/resolved tickets
def all_closed_tickets(request):
    tickets = ticket.objects.filter(assigned_to=request.users , is_resolved=True)
    context = {'tickets': tickets}
    return render (request, 'tickets/all_closed_tickets.html', context)