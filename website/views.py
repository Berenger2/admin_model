from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.utils.text import slugify
from .forms import *
from .models import *
from pprint import pprint
from django.http import JsonResponse

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
            state = 'DE'
            status = 'IN'
            slug = slugify(libelle, allow_unicode=True)
            save_by = request.user
            add_model = Model(slug=slug, libelle=libelle, description=description, score=score, path=path, state=state, status=status, saved_by=save_by)
            add_model.save()
            messages.success(request, 'The model was added successfully')
            return redirect('models')
        else:
            messages.success(request, 'An error has occurred')
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
                messages.success(request, 'An error has occurred')
                return render(request, 'pages/model/edit.html', {'form': form, 'model': current_model})
        else:
            return render(request, 'pages/model/edit.html', {'form': form, 'model': current_model})

### Experience
def experiences(request):
    if request.user.is_anonymous:
        messages.success(request, 'You need to connect to see this page')
        return redirect('home')
    else:
        experiences = Experience.objects.all()
        # dd(experiences)
        return render(request, 'pages/experiences/list.html', {'experiences': experiences})
    
def add_experience(request):
    if request.user.is_anonymous:
        messages.success(request, 'You need to connect to see this page')
        return redirect('home')
    else:
        form = AddExperinceForm(request.POST or None)
        
        if request.method == 'POST':
            if form.is_valid():
                libelle = form.cleaned_data['libelle']
                description = form.cleaned_data['description']
                slug = slugify(libelle, allow_unicode=True)
                save_by = request.user
                add_epx= Experience(slug=slug, libelle=libelle, description=description, saved_by=save_by)
                add_epx.save()
                messages.success(request, 'The Experience was added successfully')
                return redirect('experiences')
            else:
                messages.success(request, 'An error has occurred')
                return render(request, 'pages/experiences/add.html', {'form': form})
        return render(request, 'pages/experiences/add.html', {'form': form})

def experience_edit(request, slug):
    if request.user.is_anonymous:
        messages.success(request, 'You need to connect to see this page')
        return redirect('home')
    else:
        current_experience = Experience.objects.get(slug=slug)
        form = AddExperinceForm(request.POST or None, request.FILES or None, instance=current_experience)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'The experience has been successfully modified')
                return redirect('experiences')
            else:
                return render(request, 'pages/experiences/edit.html', {'form': form, 'experience': current_experience})
        else:
            return render(request, 'pages/experiences/edit.html', {'form': form, 'experience': current_experience})

def experience_view(request, slug):
    if request.user.is_anonymous:
        messages.success(request, 'You need to connect to see this page')
        return redirect('home')
    else:
        experience = Experience.objects.get(slug=slug)
        return render(request, 'pages/experiences/view.html', {'experience': experience})

### Deploiement
def deploiements(request):
    if request.user.is_anonymous:
        messages.success(request, 'You need to connect to see this page')
        return redirect('home')
    else:
        deploiements = Deploiement.objects.all()
        return render(request, 'pages/deploiements/list.html', {'deploiements': deploiements})
    
def load_models(request):
    experience_id = request.GET.get('experience')
    models = Model.objects.filter(experience_id=experience_id).all()
    return JsonResponse(list(models.values('id', 'libelle')), safe=False)

def add_deploiement(request):
    if request.user.is_anonymous:
        messages.success(request, 'You need to connect to see this page')
        return redirect('home')
    else:
        form = AddDeploiementForm(request.POST or None)
        
        if request.method == 'POST':
            if form.is_valid():
                deploiement = form.save(commit=False)
                deploiement.saved_by = request.user
                deploiement.save()
                messages.success(request, 'The Deploiement was added successfully')
                return redirect('deploiements')
            else:
                # dd(form.errors)
                return render(request, 'pages/deploiements/add.html', {'form': form})
        return render(request, 'pages/deploiements/add.html', {'form': form})
    
def deploiement_edit(request, slug):
    if request.user.is_anonymous:
        messages.success(request, 'You need to connect to see this page')
        return redirect('home')
    else:
        current_deploiement = Deploiement.objects.get(slug=slug)
        form = AddDeploiementForm(request.POST or None, request.FILES or None, instance=current_deploiement)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'The deploiement has been successfully modified')
                return redirect('deploiements')
            else:
                return render(request, 'pages/deploiements/edit.html', {'form': form, 'deploiement': current_deploiement})
        else:
            return render(request, 'pages/deploiements/edit.html', {'form': form, 'deploiement': current_deploiement})
        
def deploiement_view(request, slug):
    if request.user.is_anonymous:
        messages.success(request, 'You need to connect to see this page')
        return redirect('home')
    else:
        deploiement = Deploiement.objects.get(slug=slug)
        return render(request, 'pages/deploiements/view.html', {'deploiement': deploiement})

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