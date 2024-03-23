from django.shortcuts import render, redirect
from .models import Shopping
from .forms import ShoppingForm
from django.http import HttpResponse


def create_order(request):
    template_name = "CRUD/create.html"
    form = ShoppingForm()
    if request.method == "POST":
        form = ShoppingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("ORDER PLACED!!!!!")
    context = {"form": form}
    return render(request, template_name, context)


def show_order(request):
    template_name = "CRUD/show.html"
    orders = Shopping.objects.all()
    context = {"orders": orders}
    return render(request, template_name, context)


def update_order(request, pk):
    template_name = "CRUD/create.html"
    obj = Shopping.objects.get(id=pk)
    form = ShoppingForm(instance=obj)
    if request.method == "POST":
        form = ShoppingForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def delete_order(request, pk):
    obj = Shopping.objects.get(id=pk)
    template_name = 'CRUD/confirm.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, template_name)




