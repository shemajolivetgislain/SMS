from django.shortcuts import render, redirect
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm
from .models import Stock


def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title": title,
    }
    return render(request, "home.html", context)


def list_item(request):
    title = 'List of Items'
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Stock.objects.filter(category__icontains=form['category'].value(),
                                        item_name__icontains=form['item_name'].value()
                                        )
        context = {
            "form": form,
            "title": title,
            "queryset": queryset,
        }
    return render(request, "list_item.html", context)


def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_item')
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "add_items.html", context)


def update_items(request, pk):
    queryset= Stock.objects.get(id=pk)
    form = StockCreateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_item')
    context = {
        'form': form
    }

    return render(request, "add_items.html", context)


def delete_items(request, pk):
    queryset= Stock.objects.get(id=pk)
    form = StockCreateForm(instance=queryset)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/list_item')

    return render(request, "delete_items.html")
