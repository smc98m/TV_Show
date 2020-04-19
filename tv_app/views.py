from django.shortcuts import render, redirect
from .models import Show

def index(request):
    return redirect("/shows")

# methods that render templates:

def new(request):
    return render(request, "new.html")

def all_show(request):
    context = {
        'all_show': Show.objects.all()
    }
    return render(request, "shows.html", context)

def one_show(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, "one_show.html", context)

def edit(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

# methods that redirect:

def create_show(request):
    new_show = Show.objects.create(title = request.POST["title"], network = request.POST["network"], release_date = request.POST["release_date"], description = request.POST["description"])
    print(new_show.id)
    return redirect(f'/one_show/{new_show.id}')

def show(request, id):
    show = Show.objects.get(id=id)
    return redirect(f'/one_show/{show.id}')

def update(request, id):
    show = Show.objects.get(id=id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.save()
    return redirect(f'/one_show/{show.id}')

def destroy(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')