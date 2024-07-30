from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import send_mail



# Create your views here.
class RegistrationView(View):
    def get(self,request):
        return render(request,'authentication/register.html')
    
    def post(self,request):
        #Get User Data
        #Validate User Data
        #Create User

        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        context={
            'fieldValues':request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<9:
                    messages.error(request,'Password Is Too Short!')
                    return render(request,'authentication/register.html',context)

                user=User.objects.create_user(username=username,email=email)
                user.set_password(password)
                user.save()
                email_subject="Successful Account "
                send_mail(
                    "Subject here",
                    "Here is the message.",
                    "from@example.com",
                    ["to@example.com"],
                    fail_silently=False,
                )
                messages.success(request,'Account Successfully Created!')

        response=render(request,'authentication/register.html');
        storage = messages.get_messages(request)
        list(storage)  # Access all messages to clear them
        storage.used = True
        return response;

class UserNameValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        username=data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphanumeric characters'},status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'sorry username entered is already choosen'}, status=400)
        return JsonResponse({'username_valid':True })
    

class EmailValidationView(View):
    def post(self,request):
        data=json.loads(request.body);
        email=data['email'];

        if not validate_email(email):
            return JsonResponse({"email_error":"email entered is invalid"},status=400);
        if User.objects.filter(email=email).exists():
            return JsonResponse({"email_error":"email entered already registered"},status=400);
        return JsonResponse({"email_valid":True})
        

