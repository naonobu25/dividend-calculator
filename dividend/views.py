from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import ForeignStock

def stock_manage(request):
    return render(request, 'dividend/stock_manage.html', {})
