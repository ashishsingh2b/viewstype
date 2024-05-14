from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
# Create your views here.

def func(request):
    return HttpResponse('<h1>This is function based view<h1>')

class Myview(View):
    def get(self,request):
        return HttpResponse('<h1>This is class based view</h1>')
    
class My(View):
    def get(self,request):
        return HttpResponse("<h1>Hello this is my class based view </h1>")

class Mythird(View):
    name= "Ashish"
    def get(self,request):
        #return HttpResponse("<h1>This is my third view</h1>")
        return HttpResponse(self.name)

class Myforth(Mythird):
    def get(self,request):
        return HttpResponse(self.name)
class home(View):
    def get (self,request):
        return render(request,'home.html')
    
def homef(request):
    context = {'msg':'Welcome to geeky shows'}
    return render(request,'home.html',context)


class homev(View):
    def get(self,request):
        context = {'Intro':'Hello Sir my name is ashish singh'}
        return render(request,'home.html',context)

def contact(request):
    #post method
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("Thank u for Submitted")
        #get method
    else:
        form = ContactForm()
        return render(request,'contact.html',{'form':form})
    
class con(View):
    def get(self,request):
        form =ContactForm()
        return render(request,'contact.html',{'form':form})
    
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("<h1>Thanks for sharing</h1>")
        
def cont(request):
    temp = "contact.html"
    context = {'msg2':'this is my template attribute store in another file'}
    return render(request,temp,context)

def conta(request,template_name):
    template_name = template_name
    context = {'msg2':'this is my template attribute store in another file'}
    return render(request,template_name,context)