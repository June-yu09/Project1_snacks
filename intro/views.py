from django.shortcuts import render

from .models import SnacksIntro
from .forms import SnacksModelForm


def snack_view(request):
    snacks = SnacksIntro.objects.all()


    context = {'snacks':snacks}
    return render(request, 'intro/snack.html', context)

def add_snacks_view(request):
    form = SnacksModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save()
        image = request.FILES.get('image')
        if image:
            obj.image = image
        obj.save()
        form = SnacksModelForm()
    context = {'form': form}

    return render(request, 'intro/add.html', context)
    
