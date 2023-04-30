from django.shortcuts import render


def index(request):
    return render(request, 'gold/index.html')


def plan(request):
    return render(request, 'gold/plan.html')
