from django.contrib import messages
from django.shortcuts import render, redirect
from myapp.models import *
from django.db.models import Q


def show_about_page(request):
    print("about page request")
    name="ABC"
    link="https://www.youtube.com/watch?v=wHiAXBVJIuw"

    data={
        "name":name,
        "link":link
    }
    return render(request,"about.html",data)

def show_home_page(request):

    cats=Category.objects.all()
    images=Image.objects.all()

    data={"images":images, "cats":cats}
    return render(request,'home.html',data)

def show_category_page(request,cid):
    print(cid)
    cats=Category.objects.all()

    category=Category.objects.get(pk=cid)
    images=Image.objects.filter(cat=category)

    data={"images":images, "cats":cats}
    return render(request,'home.html',data)

def search(request):
    if request.method=='GET':
        keywords=request.GET.get('keywords')
        images = Image.objects.filter(Q(title__icontains=keywords))
        if keywords:
            if images:
                images = Image.objects.filter(Q(title__icontains=keywords))
            else:
                messages.warning(request, 'No Result Found')

    return render(request,'result.html',{'keywords':keywords,'images':images})

def home(request):
    return redirect('/home')
