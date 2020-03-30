from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import wishes

# Create your views here.

#def index(request):
#    return HttpResponse("main index.")
    

def index(request):
    listWishes = wishes.objects.all()
    context = {'listWishes':listWishes}
    return render(request, "main/wishesList.html", context)
    

def insert_wish(request):
    if request.method == 'POST':
        wish = wishes(wish=request.POST['content'])
        wish.save()
        return redirect('index')
    return render(request, 'main/wishes_add.html')

def delete(request, item_id):
    item = wishes.objects.get(id=item_id)
    item.delete()
    return redirect('index')