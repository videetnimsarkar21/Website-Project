from django.shortcuts import render

# Create your views here.
#views.py
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
import pandas as pd
data = pd.read_csv("data.csv")

def assign(arr):
    if len(arr)==1:
        price_source = arr[0][0]
        cab = arr[0][1]
        return(price_source,cab)
    else:
        price_source = arr[0][0]
        cab = arr[0][1]
        travel_price = arr[1][0]
        mode = arr[1][1]
        price_destination = arr[2][0]
        cab1 = arr[2][1]
        price = int(price_source)+ int(travel_price) + int (price_destination)
        return(price_source,cab,travel_price,mode,price_destination,cab1,price)
        
def getprice(source,destination,mode):
    for i in range(len(data['Source'])):
        if data['Source'][i] == source and data['Destination '][i]== destination:
            source_airport = min(data['Ola-1'][i],data['Uber-1'][i])
            if source_airport == data['Ola-1'][i]:
                a = [source_airport,'Ola']
            else:
                a = [source_airport,'Uber']
                
            if mode=='Flight':
                ft = data['Flight '][i]
                b = [ft,'Flight']
            elif mode=='Train':
                ft = data['Train'][i]
                b = [ft,'Train']
            else:
                ft = 0
            
            
            airport_destination = min(data['Ola-2'][i],data['Uber-2'][i])
            if airport_destination == data['Ola-2'][i]:
                c = [airport_destination,'Ola']
            else:
                c = [airport_destination,'Uber']
            
            if ft==0:
                return(assign([a]))
            else:
                return assign([a,b,c])
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def login_page(request):
    logout(request)
    return (render_to_response('registration/login.html'))

def search(request):
    flighttype = request.GET.get("flight-type")
    source = request.GET.get("source")
    destination = request.GET.get("destination ")
    mode = request.GET.get("mode")
    if mode=='Road':
        a,b = getprice(source,destination,mode)
        variables = RequestContext(request, {
        'source':source,
        'a': a,
        'b':b,
        'mode':mode,
        'destination':destination,
        })
        return (render_to_response('search1.html',variables))
    else:
        a,b,c,d,e,f,p = (getprice(source,destination,mode))
        if d=='Flight':
            variables = RequestContext(request, {
            'source':source,'a': a,'b':b,'c':c,
            'd':'Airport','destination':destination,'e':e,'f':f,'mode':mode,'p':p})
            return (render_to_response('search.html',variables))
        else:
            variables = RequestContext(request, {
            'source':source,'a': a,'b':b,'c':c,
            'd':'Railway Station','destination':destination,'e':e,'f':f,'mode':mode,'p':p})
            return (render_to_response('search.html',variables))
        
    
@login_required(login_url='accounts/login')
def home(request):
    return render_to_response(
    'index.html',
    { 'user': request.user }
    )
