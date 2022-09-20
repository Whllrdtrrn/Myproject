from django.shortcuts import render,redirect
from django.template import loader
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import user
from .models import sideeffect
from .models import questioner



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
        username = request.POST.get('username',None)
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        confirm_password = request.POST.get('password_confirmation',None)

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
        prod = user()
        prod.name = request.POST.get('name')
        prod.contact_number= request.POST.get('contact_number')
        prod.vaccination_brand = request.POST.get('vaccination_brand')
        prod.vaccination_site = request.POST.get('vaccination_site')
        prod.address = request.POST.get('address')
        prod.age = request.POST.get('age')
        prod.bday = request.POST.get('bday')
        prod.gender = request.POST.get('gender')
        if len(request.FILES) !=0:     
            prod.file = request.FILES['file']
        prod.save()    
        # item = user (name=names,contact_number=contact_numbers,
        # vaccination_brand=vaccination_brands,vaccination_site=vaccination_sites,address=addresss,
        # age=ages,bday=bdays,gender=genders)
        # item.save()
        return redirect('server')

    else:
    
        return render (request,'information.html')


def sideeffect_page(request):
    
    if request.method == 'POST':
        muscle_ached = request.POST.get('muscle_ache',False)
        headached = request.POST.get('headache',False)
        feverd= request.POST.get('fever',False)
        rednessd = request.POST.get('redness',False)
        swellingd = request.POST.get('swelling',False)
        tendernessd = request.POST.get('tenderness',False)
        warmthd = request.POST.get('warmth',False)
        itchd = request.POST.get('itch',False)
        indurationd= request.POST.get('induration',False)
        feverishd = request.POST.get('feverish',False)
        chillsd= request.POST.get('chills',False)
        join_paind = request.POST.get('join_pain',False)
        fatigued= request.POST.get('fatigue',False)
        nausead= request.POST.get('nausea',False)
        vomitingd = request.POST.get('vomiting',False)
        
        items = sideeffect (muscle_ache=muscle_ached,headache=headached,
        fever=feverd,redness=rednessd,swelling=swellingd,tenderness=tendernessd,
        warmth=warmthd,itch=itchd,induration=indurationd,feverish=feverishd,chills=chillsd,
        join_pain=join_paind,fatigue=fatigued,nausea=nausead,vomiting=vomitingd)
        items.save()
        return redirect('success')
    else:             
      return render (request,'sideeffect.html')

   

def server_form(request):
    if request.method == 'POST':
        Q0 = request.POST['Q0']
        Q1 = request.POST['Q1']
        Q2 = request.POST['Q2']
        Q3 = request.POST['Q3']
        Q4 = request.POST['Q4']
        Q5 = request.POST['Q5']
        Q6 = request.POST['Q6']
        Q7 = request.POST['Q7']
        Q8= request.POST['Q8']
        Q9 = request.POST['Q9']
        Q10= request.POST['Q10']
        Q11 = request.POST['Q11']
        Q12= request.POST['Q12']
        Q13= request.POST['Q13']
        Q14 = request.POST['Q14']
        Q15= request.POST['Q15']
        Q16 = request.POST['Q16']
        Q17= request.POST['Q17']
        Q18= request.POST['Q18']
        Q19 = request.POST['Q19']
        Q20 = request.POST['Q20']
        Q21 = request.POST['Q21']
        Q22 = request.POST['Q22']
        allergy = request.POST['allergy']
        Q23 = request.POST['Q23']
        Q24 = request.POST['Q24']
        item = questioner(Q0=Q0,Q1=Q1,Q2=Q2,Q3=Q3,Q4=Q4,Q5=Q5,Q6=Q6,Q7=Q7,Q8=Q8,Q9=Q9,Q10=Q10,Q11=Q11,
        Q12=Q12,Q13=Q13,Q14=Q14,Q15=Q15,Q16=Q16,Q17=Q17,Q18=Q18,Q19=Q19,Q20=Q20,Q21=Q21,Q22=Q22,allergy=allergy,
        Q23=Q23,Q24=Q24)
        item.save()
        return redirect('sideeffect')
    else:   
        return render (request,'serverform.html')  

def success_page(request):
    template = loader.get_template('success.html')
    return HttpResponse(template.render()) 


def dashboard (request):
     item_list = user.objects.all()
     item_lists = sideeffect.objects.all()
     userAccount = User.objects.all()
     total_user = userAccount.count()
     context = {
        'item_list': item_list,
        'item_lists': item_lists,
        'userAccount': userAccount,
        'total_user':total_user
    }
   
     return render (request,'system/dashboard.html',context)

    # template = loader.get_template('system/dashboard.html')
    # return HttpResponse(template.render()) 
     


