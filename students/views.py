from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm,CreateRecordForm,UpdateRecordForm
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
# Create your views here.
def index(request):
    return render(request, "students/index.html")

def register(request):
    form=CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('my-login')
    context ={'form' : form}
    return render(request, "students/register.html", context=context)


#dashboard
@login_required(login_url='my-login')
def dashboard(request):
    my_records=Record.objects.all()
    context={'records': my_records}
    return render(request, "students/dashboard.html",context=context)


# login form 
def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form=LoginForm(request, data=request.POST)
    if form.is_valid():
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
    context={'form' : form}
    return render(request,'students/my-login.html',context=context)

#logout
def user_logout(request):
    auth.logout(request)
    return render(request,'students/my-login.html')

@login_required(login_url='my-login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context={'form' : form}
    return render(request,'students/create-record.html',context=context)
# Update Record
@login_required(login_url='my-login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'students/update-record.html', context)

# Delete Record
@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard')

    context = {'record': record}
    return render(request, 'students/delete-record.html', context)

