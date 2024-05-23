from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.utils.text import slugify
from .forms import AddModelForm
from .models import Model
from pprint import pprint

### DASH
def home(request):

    if request.user.is_anonymous:
        return render(request, 'pages/auth/login.html')
    else:
        return render(request, 'home.html')

### MODELS

def model_view(request, slug):
    if request.user.is_anonymous:
        messages.success(request, 'You need to connect to see this page')
        return redirect('home')
    else:
        model = Model.objects.get(slug=slug)
        return render(request, 'pages/model/view.html', {'model': model})

def models(request):
    if request.user.is_anonymous:
        messages.success(request, 'You need to connect to see this page')
        return redirect('home')
    else:
        models = Model.objects.all()
        return render(request, 'pages/model/list.html', {'models': models})

def add_model(request):
    form = AddModelForm(request.POST or None, request.FILES or None)
    
    if request.method == 'POST':
        if form.is_valid():
            
            libelle = form.cleaned_data['libelle']
            description = form.cleaned_data['description']
            score = 100
            path = form.cleaned_data['path']
            state = False
            status = False
            slug = slugify(libelle, allow_unicode=True)

            add_model = Model(slug=slug, libelle=libelle, description=description, score=score, path=path, state=state, status=status)
            add_model.save()
            messages.success(request, 'The model was added successfully')
            return redirect('models')
        else:
            # Form is not valid, return a response
            return render(request, 'pages/model/add.html', {'form': form})
    else:
        if request.user.is_anonymous:
            messages.success(request, 'You need to connect to see this page')
            return redirect('home')
        else:
            return render(request, 'pages/model/add.html', {'form': form})

def model_edit(request, slug):
    if request.user.is_anonymous:
        messages.success(request, 'You need to connect to see this page')
        return redirect('home')
    else:
        current_model = Model.objects.get(slug=slug)
        form = AddModelForm(request.POST or None, request.FILES or None, instance=current_model)
        if request.method == 'POST':
            if form.is_valid():
            
                form.save()
                messages.success(request, 'The model has been successfully modified')
                return redirect('models')
            else:
                # Form is not valid, return a response
                return render(request, 'pages/model/edit.html', {'form': form, 'model': current_model})
        else:
            return render(request, 'pages/model/edit.html', {'form': form, 'model': current_model})

### USER
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now connected')
            return redirect('home')
        else:
            messages.error(request, 'Incorrect username or password')
            return render(request, 'pages/auth/login.html')
    else:
        return redirect('home')
    


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect('home')
    