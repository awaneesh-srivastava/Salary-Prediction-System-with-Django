from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Rahman Is Land on Home Page")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("Rahman Is Land on About Page")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("Rahman Is Land on Contact Us Page")


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("Rahman Is Land on Services Page")