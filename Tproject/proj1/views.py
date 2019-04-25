from django.shortcuts import render
from proj1.models import USER_LOGIN,User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import make_password



def home(request):
    return render(request,'proj1/login.html',)
def test(request):
    return render(request,'proj1/test.html')
def questions_list(request):
    return render(request,'proj1/data.html',{})
def index(request):
    messages.info(request, 'successfully Registered!')
    return render(request,'proj1/login.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        print(username,password)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, "proj1/test.html",{'user':user})
            else:
                return HttpResponse("Account Not Active")

        else:
            print("some tried to login and failed")
           # print("email:{} and password :{}".format(username, password))
            # messages.warning(request, 'Invalid credentials!')
            return render(request, "proj1/login.html")
            # return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'proj1/login.html')
def user_register(request):

     registered=False
     if request.method =='POST':
         if request.POST.get('psw')==request.POST.get('psw-repeat'):

             print("srikar")
             user_name1 = request.POST.get('username')
             pass_word1 = request.POST.get('psw')
             enc_password = make_password(pass_word1)
             user = User(username=user_name1, password=enc_password)
             print(request.POST.get('First_Name'))
             print(request.POST.get('Last_Name'))
             print(user_name1,pass_word1,enc_password)
             print(request.POST.get('Gender'))
             user.email=request.POST.get('email')
             user.save()
             try:

                  user_obj=USER_LOGIN(first_name=request.POST.get('First_Name'),last_name=request.POST.get('Last_Name') ,user_name=request.POST.get('username'),
                            pass_word=request.POST.get('psw'),email_id=request.POST.get('email'),gender=request.POST.get('Gender')
                  )
                  user_obj.save()
                  
                  return render(request,'proj1/login.html')
             except:
                   return HttpResponse("sorry username or email already exist please try with other one!")
   
         else:

              return HttpResponse("both passwords are not matched!")

               
     else:
           return render(request,'proj1/register.html')

def results(request):
    if request.method == 'POST':
        answer = request.POST.get('answer')
        answer1 = request.POST.get('answer1')
        answer2 = request.POST.get('answer2')
        user1=request.user
        ans= answer +'?'+answer1+'?'+answer2
        print(answer,answer1,answer2)
        user_obj1=Data(user=user1,quest=ans)
        user_obj1.save()
        
        return HttpResponse("Hello")



        

    

           



                


            

 
         




  
    