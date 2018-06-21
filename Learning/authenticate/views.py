from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from .forms import SignUpForm,EditUserForm,AcceptFile,WriteCode
from . import functions,Python_to_java
import sys,os
# Create your views here.
def home(request):
    return render(request,'authenticate/home.html',{})

def run_ide(request):
    if(request.method=='POST'):
        form = WriteCode(request.POST)
        #print (request.POST['results'])
        file_name,file_classname = functions.write_temp_file(request.POST['results'])
        sys.path.insert(0, "G:\Romu\PycharmProjects")  # Define The Directory To Look For The File
        os.chdir("G:\Romu\PycharmProjects")
        parameter_value = request.POST['parameters']
        try:
            Python_to_java.compile_java('C:\\Program Files\\Java\\jdk-9.0.1\\bin\\javac', file_name)
            display = Python_to_java.execute_java('C:\\Program Files\\Java\\jdk-9.0.1\\bin\\java', file_name,
                                                  parameter_value)
            print(display)
            return render(request, "authenticate/display_java.html", {'display': display})
        except:
            display = "Code has errors. Cannot Execute"
            return render(request, "authenticate/display_java.html", {'display': display})
        finally:
            os.remove(file_name)
            print(file_classname)
            os.remove(file_classname)
    else:
        form = WriteCode()
    return render(request, 'authenticate/run_ide.html',{'form':form})

def display_java(request):
    return render(request, 'authenticate/display_java.html', {})
def run_java(request):
    if(request.method=='POST'):
        file = AcceptFile(request.POST,request.FILES)
        parameters = AcceptFile(request.POST['parameters'])
        if(file.is_valid()):
            functions.handle_uploaded_file(request.FILES['file'])
            messages.success(request, 'File Uploaded Successfully')
            #sys.path.insert(0, "G:\Romu\Internship\In Time Tec")
            #os.chdir("G:\Romu\Internship\In Time Tec")

            sys.path.insert(0, "G:\Romu\PycharmProjects")           #Define The Directory To Look For The File
            os.chdir("G:\Romu\PycharmProjects")
            file_name = request.FILES['file'].name
            parameter_value = request.POST['parameters']
            file_classname, ext = os.path.splitext(file_name)
            file_classname = file_classname+".class"
            try:
                Python_to_java.compile_java('C:\\Program Files\\Java\\jdk-9.0.1\\bin\\javac', file_name)
                display = Python_to_java.execute_java('C:\\Program Files\\Java\\jdk-9.0.1\\bin\\java', file_name,parameter_value)
                print(display)
                return render(request, "authenticate/display_java.html", {'display': display})
            except:
                display = "Code has errors. Cannot Execute"
                return render(request, "authenticate/display_java.html", {'display': display})
            finally:
                os.remove(file_name)
                os.remove(file_classname)
    else:
        file = AcceptFile()
    return render(request, "authenticate/run_java.html", {'form': file})

def login_user(request):

    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Logged in successfully')
            return redirect('home')
        else:
            messages.success(request,'Failed to Log in! Try again...')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})
def logout_user(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('home')

def register_user(request):
    if(request.method=='POST'):
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request, 'Successfully registered')
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request, 'authenticate/register.html', context)

def edit_profile(request):
    if (request.method == 'POST'):
        form = EditUserForm(request.POST,instance=request.user)
        if (form.is_valid()):
            form.save()
            messages.success(request, 'You have successfully edited your profile')
            return redirect('home')
    else:
        form = EditUserForm(instance=request.user)
    context = {'form': form}
    return render(request, 'authenticate/edit_profile.html', context)
def change_password(request):
    if (request.method == 'POST'):
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if (form.is_valid()):
            form.save()
            messages.success(request, 'You have successfully changed your password')
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)