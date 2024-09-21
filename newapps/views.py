from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(f'{name} {email} {message}')
    return render(request, 'newapps/index.html')