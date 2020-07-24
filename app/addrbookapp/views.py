# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from addrbookapp.models import Address
from django.http import HttpResponseRedirect, HttpResponse
from addrbookapp.forms import AddressBookForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def create(request):
    form = AddressBookForm()
    if request.method == 'POST':
        form = AddressBookForm(request.POST)
        if form.is_valid():
            form.save()
            t = "You have succesfully added your contact details" 
            return HttpResponseRedirect('/')
    return render(request, 'addressBook.html', {'form': form})  

def home(request):
    obj = Address.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(obj, 5)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', { 'contacts': contacts })
    
def delete_contact(request, id):
    obj=Address.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/')
    context={
    'username': Address.objects.get(id=id).user,
    'address': Address.objects.get(id=id).address,
    'email': Address.objects.get(id=id).email_id,
    'phone_number': Address.objects.get(id=id).phone_number,
     'addr_id': obj}     
    return render(request, 'update.html', context)

def update_contact(request,id):
    obj= Address.objects.get(id = id)
    form = AddressBookForm(instance=obj)
    print (form.instance.id)
    if request.method == 'POST':
        form = AddressBookForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print (form.errors)
    context={'form':form}     
    return render(request, 'update.html', context)
def update_page(request, id):
    if request.method == 'POST':
        form = AddressBookForm(request.POST)
        if form.is_valid():
            post = form.save()
            saveLogs(request,"You updated your Address Book")
            return HttpResponseRedirect('/')
        else:
            print (form.errors)