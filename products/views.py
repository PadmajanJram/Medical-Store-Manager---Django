from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ProductForm()
    return render(request, 'create.html', {'form': form})

@login_required(login_url='/login/')
def product_read(request):
    product_list=Product.objects.all()
    return render(request,'retrieve.html',{'product_list':product_list})

@login_required(login_url='/login/')
def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ProductForm(instance=product)           
    return render(request, 'update.html', {'form': form})

@login_required(login_url='/login/')
def product_delete(request,pk):
    product=Product.objects.get(pk=pk)  
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    
    return render(request,'delete.html',{'product':product})

@login_required(login_url='/login/')
def search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query)
    return render(request,'search_results.html', {'results': results})