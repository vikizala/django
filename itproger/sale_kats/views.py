from django.shortcuts import render
from .models import Articles
# Create your views here.
def sale_kats(request):
    # return render(request, 'main/test.html')
    sale_kats = Articles.objects.all()
    return render(request, 'main/test.html', {'sale_kats' : sale_kats})