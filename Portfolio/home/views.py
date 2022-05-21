from django.shortcuts import render, HttpResponse
from home.models import Contact

def home(request):
    context = {'name':'Spoorthy', 'course': 'Django'}
    return render(request, 'home.html', context)

def about(request):
        # return HttpResponse("This is my aboutpage(/about)")
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse("This is my projectspage(/projects)")
    return render(request, 'projects.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("The data has been printed to the db")
    # return HttpResponse("This is my contactpage(/contact)")
    return render(request, 'contact.html')