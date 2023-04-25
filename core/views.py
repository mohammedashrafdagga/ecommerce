from django.shortcuts import render


# frontend page
def frontpage(request):
    return render(request, 'core/base.html')
