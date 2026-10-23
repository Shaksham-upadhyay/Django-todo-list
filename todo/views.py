from django.utils import timezone
from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    if request.method=="POST":
        data=request.POST
        title=data.get('title')
        if title:
            title=title[0].upper()+title[1:]
            Todo.objects.create(title=title)
        return redirect('home')
    sort = request.GET.get('sort')  
    data = Todo.objects.all()
    if sort == "title":
        data = data.order_by('title')
    elif sort == "date":
        data = data.order_by('-created') 
    elif sort == "completed":
        data = data.order_by('-iscompleted')

    # search
    search = request.GET.get('search')
         
    if  search:
        data=Todo.objects.filter(title__icontains=search) 
    else:
        print("Enter a name")

            # # 📄 Pagination       
    paginator =Paginator(data,5)
    page_number =request.GET.get('page')
    page_obj =paginator.get_page(page_number)
 
    return render(request,"home.html",{'sort':sort,'page_obj':page_obj,'search':search})

def update(request,id):
    if request.method=="POST":
         data=request.POST
         qr=Todo.objects.get(pk=id)
         if 'chck' in request.POST:
             qr.iscompleted = True
             qr.completed = timezone.now()
         else:
            qr.completed=None
            qr.iscompleted = False
         qr.save()
    return redirect("home")


def delete(req,id):
    qr=Todo.objects.get(pk=id)
    qr.delete()
    return redirect('home')
