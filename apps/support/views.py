from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Ticket

@login_required
def create_ticket_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        Ticket.objects.create(
            user=request.user,
            subject=subject,
            description=description
        )
        return redirect('support:ticket_list')
    return render(request, 'support/create_ticket.html')


@login_required
def ticket_list_view(request):
    tickets = Ticket.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'support/ticket_list.html', {'tickets': tickets})

def is_staff_user(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_staff_user)
def admin_ticket_list_view(request):
    # Wszystkie zgłoszenia, posortowane od najnowszego
    tickets = Ticket.objects.all().order_by('-created_at')
    return render(request, 'support/admin_ticket_list.html', {'tickets': tickets})

@user_passes_test(is_staff_user)
def admin_resolve_ticket_view(request, ticket_id):
    # Oznaczamy zgłoszenie jako rozwiązane
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.is_resolved = True
    ticket.save()
    return redirect('support:admin_ticket_list')

@login_required
def my_ticket_list_view(request):
    """ Wyświetla listę zgłoszeń danego użytkownika """
    tickets = Ticket.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'support/my_ticket_list.html', {'tickets': tickets})
