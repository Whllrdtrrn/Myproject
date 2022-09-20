from django.shortcuts import render,redirect
from django.template import loader
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import user
from .models import sideeffect


# Create your views here.

def home_page(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render()) 

def login_page(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username']  ,password = request.POST['password'])
        if user is not None:
                auth.login(request,user)
                return redirect('information')
        else:
                return render (request,'login_page.html', {'error':'Invalid Username or Password'}) 
    else:
     return render(request,'login_page.html')
    

def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password_confirmation']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register_page)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register_page)
            else:
                user = User.objects.create_user(username=username, password=password, 
                email=email)
                user.save()
                
                return redirect('loginpage')

        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect('register_page')
            
    else:
        return render(request, 'register_page.html')  

  
        
def information_page (request):
    if request.method == 'POST':
        names = request.POST['name']
        emails = request.POST['email']
        contact_numbers = request.POST['contact_number']
        vaccination_brands = request.POST['vaccination_brand']
        vaccination_sites = request.POST['vaccination_site']
        addresss = request.POST['address']
        ages = request.POST['age']
        bdays = request.POST['bday']
        genders = request.POST['gender']
        
        item = user (name=names,email=emails,contact_number=contact_numbers,
        vaccination_brand=vaccination_brands,vaccination_site=vaccination_sites,address=addresss,
        age=ages,bday=bdays,gender=genders)
        item.save()
        return redirect('server')

    else:
    
        return render (request,'information.html')


def sideeffect_page(request):
    
    if request.method == 'POST':
        muscle_ached = request.POST['muscle_ache']
        headached = request.POST['headache']
        feverd= request.POST['fever']
        rednessd = request.POST['redness']
        swellingd = request.POST['swelling']
        tendernessd = request.POST['tenderness']
        warmthd = request.POST['warmth']
        itchd = request.POST['itch']
        indurationd= request.POST['induration']
        feverishd = request.POST['feverish']
        chillsd= request.POST['chills']
        join_paind = request.POST['join_pain']
        fatigued= request.POST['fatigue']
        nausead= request.POST['nausea']
        vomitingd = request.POST['vomiting']
        
        items = sideeffect (muscle_ache=muscle_ached,headache=headached,
        fever=feverd,redness=rednessd,swelling=swellingd,tenderness=tendernessd,
        warmth=warmthd,itch=itchd,induration=indurationd,feverish=feverishd,chills=chillsd,
        join_pain=join_paind,fatigue=fatigued,nausea=nausead,vomiting=vomitingd)
        items.save()
        return redirect("success")
    else:             
      return render (request,'sideeffect.html')

   

def server_form(request):
    template = loader.get_template('serverform.html')
    return HttpResponse(template.render())     

def success_page(request):
    template = loader.get_template('success.html')
    return HttpResponse(template.render()) 


def dashboard (request):
     item_list = user.objects.all()
     item_lists = sideeffect.objects.all()
     userAccount = User.objects.all()

     context = {
        'item_list': item_list,
        'item_lists': item_lists,
        'userAccount': userAccount
    }
   
     return render (request,'system/dashboard.html',context)

    # template = loader.get_template('system/dashboard.html')
    # return HttpResponse(template.render()) 
     


