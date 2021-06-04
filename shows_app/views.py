from django.shortcuts import redirect, render, HttpResponse
from .models import Show
from django.contrib import messages

# Create your views here.
def index(request):
    return redirect('/shows')

def add_show(request):
    return render(request, "add_show.html")

def process_new_show(request):
    if request.method == 'POST':
        errors = Show.objects.add_validator(request.POST)
        if len(errors) > 0:
            for error in errors.values():
                messages.error(request, error)
            return redirect("/shows/new")
        else:
            new_show = Show.objects.create(
                title = request.POST['title'], 
                network = request.POST['network'], 
                release_date = request.POST['release_date'], 
                desc = request.POST['desc']
            )
            return redirect(f'/shows/{new_show.id}')
    else:
        return redirect('/shows/new')

def display_show(request, show_id):
    context = {
        "this_show": Show.objects.get(id=show_id)
    }
    return render(request, "display_show.html", context)

def shows(request):
    context = {
        "all_the_shows": Show.objects.all()
    }
    return render(request, "shows.html", context)

def edit_show(request, show_id):
    context = {
        "show_to_edit": Show.objects.get(id=show_id)
    }
    return render(request, "edit_show.html", context)

def process_edit(request, show_id):
    if request.method == 'POST':
        errors = Show.objects.edit_validator(request.POST)
        if len(errors) > 0:
            for error in errors.values():
                messages.error(request, error)
            return redirect(f"/shows/{show_id}/edit")
        else:
            edit_show = Show.objects.get(id=show_id)
            edit_show.title = request.POST['title']
            edit_show.network = request.POST['network']
            edit_show.release_date = request.POST['release_date']
            edit_show.desc = request.POST['desc']
            edit_show.save()
            return redirect(f'/shows/{edit_show.id}')        
    else:
        return redirect('/shows')

def delete_show(request, show_id):
    delete_show = Show.objects.get(id=show_id)
    delete_show.delete()
    return redirect('/shows')