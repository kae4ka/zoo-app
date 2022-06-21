from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import connection
from .models import Cages, Animals
from .forms import CagesForm

# homepage
def index(request):
    return render(
        request,
        'index.html',
    )

# вывести форму для добавления клетки
def showform(request):
    form = CagesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect('../cages')

    context= {'form': form }
        
    return render(request, 'output.html', context)

# удалить клетку
def cage_row_delete(request):
    id=request.GET.get('id', None)
        # id=int(request.GET.get('id'))
    cursor = connection.cursor()
    sql = "DELETE FROM public.cages WHERE cage_id=%s"
    cursor.execute(sql,[id])

    return HttpResponseRedirect('../cages')    

# вывести все данные о клетках (экспозициях)
def cages_info(request):

    sql = "SELECT cages.*, string_agg(animal_name, ', ') FROM public.cages left join public.cage_animals on cages.cage_id=cage_animals.cage_id left join public.animals on animals.animal_id=cage_animals.animal_id group by cages.cage_id"
    posts = Cages.objects.raw(sql)[:]

    print(posts)
    return render(request, 'cages.html', {'data': posts})    

# вывести все данные о животных
def animals_list(request):

    sql = "SELECT animals.animal_id, animal_name, animal_species, animal_avatar, cage_name FROM public.animals JOIN cage_animals ON cage_animals.animal_id = animals.animal_id JOIN cages ON cage_animals.cage_id = cages.cage_id ORDER BY animal_name ASC"
    posts = Animals.objects.raw(sql)[:]

    print(posts)
    return render(request, 'animals.html', {'data': posts})

# вывести все данные о конкретном животном
def animal_info(request, animal_id):

    id = animal_id
    sql = "SELECT animals.animal_id, animal_name, animal_species, animal_avatar, cage_name, time_of_day, food, amount FROM public.animals JOIN cage_animals ON cage_animals.animal_id = animals.animal_id JOIN cages ON cage_animals.cage_id = cages.cage_id JOIN feeding_schedule ON feeding_schedule.animal_id = animals.animal_id WHERE animals.animal_id=%s"
    posts = Animals.objects.raw(sql, [id])[:]

    print(posts)
    return render(request, 'animal.html', {'data': posts})