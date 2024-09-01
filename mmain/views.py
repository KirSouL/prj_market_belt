from django.shortcuts import render


def index(request):
    return render(request, 'mmain/index.html')


def login(request):
    if request.method == 'POST':
        first_name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        message = request.POST.get('message')
        print(first_name, email, password, message)
    return render(request, 'mmain/login.html')


def catalog(request):
    return render(request, 'mmain/catalog.html')


def basket(request):
    return render(request, 'mmain/basket.html')
