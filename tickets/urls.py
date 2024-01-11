from django.urls import path
from tickets import views

urlpatterns =[
    path('ticket_details/<int:pk>/', views.ticketDetails, name='ticketDetails'),
    path('create-ticket/', views.createTicket, name= 'createTicket'),
    path('update-ticket/<int:pk>/', views.update_ticket, name='update'),
    path('all-tickets/', views.all_tickets, name='all-tickets'),
    path('ticket-queue/', views.ticketQueue, name='ticket-queue'),
    path('accept-ticket/<int:pk>/', views.acceptTicket, name='accept-ticket'),
    path('close-ticket/<int:pk>/', views.closeTicket, name='close-tickets'),
    path('workspace/', views.workspace, name='workspace'),
    path('all-closed-ticket/', views.all_closed_tickets, name='all-closed-tickets'),
]