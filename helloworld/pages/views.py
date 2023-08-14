from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.views.generic import TemplateView
from django.views import View  

# Create your views here.

class HomePageView(TemplateView): 
    template_name = 'pages/home.html'

class AboutPageView(TemplateView): 
    template_name = 'pages/about.html' 

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Juan Camilo", 
        }) 
        return context

class ContactPageView(TemplateView): 
    template_name = 'pages/contact.html' 

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "Contact us - Online Store", 
            "subtitle": "Contact us", 
            "description": "This is a contact page ...", 
            "email": "email: email@email.com",
            "address": "address: park aveneu",
            "phone": "phone: 123456789",  
        }) 
        return context  

class Product: 
    products = [ 
        {"id":"1", "name":"TV", "description":"Best TV", "price": 1000}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":900}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": 99}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 80} 
    ] 

class ProductIndexView(View): 
    template_name = 'products/index.html' 

    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.products 
        return render(request, self.template_name, viewData) 

class ProductShowView(View): 
    template_name = 'products/show.html' 

    def get(self, request, id): 
        viewData = {} 
        try:
            product = Product.products[int(id)-1] 
        except:
            return HttpResponseRedirect("/")

        viewData["title"] = product["name"] + " - Online Store" 
        viewData["subtitle"] =  product["name"] + " - Product information" 
        viewData["product"] = product 
        return render(request, self.template_name, viewData)

class ProductForm(forms.Form): 
    name = forms.CharField(required=True)
    description = forms.CharField(required=True) 
    price = forms.FloatField(required=True) 

class ProductCreateView(View): 
    template_name = 'products/create.html' 

    def get(self, request): 
        form = ProductForm() 
        viewData = {} 
        viewData["title"] = "Create product" 
        viewData["form"] = form 
        return render(request, self.template_name, viewData) 

    def post(self, request): 
        form = ProductForm(request.POST) 

        if form.is_valid(): 
            #return redirect("form")
            return render(request, "products/created.html") 
        else: 
            viewData = {} 
            viewData["title"] = "Create product" 
            viewData["form"] = form 
            return render(request, self.template_name, viewData)
