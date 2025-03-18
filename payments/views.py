from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Ordem, Saldo

@login_required(login_url='login')  # Garante que apenas usuários logados acessem a página
def dashboard(request):
    ordens = Ordem.objects.filter(usuario=request.user)
    saldo = Saldo.objects.filter(usuario=request.user)

    return render(request, 'dashboard.html', {'ordens': ordens, 'saldo': saldo})
