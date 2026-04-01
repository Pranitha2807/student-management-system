from django.shortcuts import render

def carousel_view(request):
    return render(request, 'carouselapp/carousel.html')