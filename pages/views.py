from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from pages.models import BestBuy
from pages.models import User
from hashlib import blake2b
from django.contrib import messages

# Create your views here.
def home_view(request):
    context ={}
    if(request.method == 'GET'): #checks if we can GET
        x = request.GET.get("product") #gets the product name if possible
        #print(x) #prints the product name the user enters (to check)
        if(x is not None): #checks if the values we're getting is not None
            all_enteries = BestBuy.objects.all().filter(Name__contains=x) #checks if any product name contains x
            context = {'all_enteries': all_enteries} #creates a dictionary with our enteries
            #print(all_enteries)
        else:
            all_enteries = BestBuy.objects.all() #just gets all products if there's no input
            context = {'all_enteries': all_enteries} #creates a dictionary with our enteries
        #for i in all_enteries: #prints each product
            #print(str(i.SKU) + " " + i.Name + " " + str(i.price) + " " + i.Status + " " + i.URL + " " + str(i.Reviews))
    return render(request, 'mainpage.html',context)

def login(request):
    if(request.method == 'POST'):
        login_email = request.POST.get("login_email")
        login_pass = request.POST.get("login_pass")
        signup_email = request.POST.get("signup_email")
        signup_pass = request.POST.get("signup_pass")
        if(login_email is not None and login_pass is not None):
            #print(blake2b(login_email.encode()).hexdigest())
            hash_login_mail = blake2b(login_email.encode()).hexdigest()
            salt = 'il0v3m3n'
            saltedpass = login_pass+salt
            #print(blake2b(saltedpass.encode()).hexdigest()) #hashes password
            hash_login_pass = blake2b(saltedpass.encode()).hexdigest()
            x = User.objects.all().filter(email=hash_login_mail,password=hash_login_pass)
            if( not x):
                #print("No such User")
                messages.error(request, "Email or password is incorrect", extra_tags='login')
                return redirect('/login?fail')
            else:
                request.session['email']=login_email
                return redirect('/')
        elif(signup_email is not None and signup_pass is not None):
            #print(blake2b(signup_email.encode()).hexdigest())
            hash_sign_mail = blake2b(signup_email.encode()).hexdigest()
            salt = 'il0v3m3n'
            saltedpass = signup_pass+salt
            #print(blake2b(saltedpass.encode()).hexdigest())
            hash_sign_pass = blake2b(saltedpass.encode()).hexdigest()
            x = User.objects.all().filter(email=hash_sign_mail,password=hash_sign_pass)
            if( not x):
                new_user = User(email=hash_sign_mail,password=hash_sign_pass)
                new_user.save()
                return redirect('/login?signup_success')
            else:
                #print("No")
                messages.error(request, "User exists already", extra_tags='signup')
                return redirect('/login?signup_fail')
    return render(request, 'login.html')

def signout(request):
    #print(request.session['email'])
    request.session['email']= '' #just changes the user that's currently using the page
    #print(request.session['email'])
    return home_view(request)