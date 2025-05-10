from django.shortcuts import render


def index(request):
    return render(request, 'main_page.html')

def page(request):
    return render(request, 'page.html')

def case1_page(request):
    return render(request, 'case1_page.html')
