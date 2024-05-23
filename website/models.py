from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.utils import timezone

ext_validator = FileExtensionValidator(allowed_extensions=['h5', 'pkl'])

class Experience(models.Model):
    STATUS = (
        ('IN', 'Inactive'),
        ('AC', 'Active'),
        ('AR', 'Archived'),
        )
    
    STATE = (
        ('PR', 'Production'),
        ('TR', 'Training'),
        ('DE', 'Development'),
        ('AR', 'Archived')
    )
    
    slug = models.SlugField(max_length=30, unique=True)
    libelle = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=2, choices=STATE, default='DE')
    status = models.CharField(max_length=2, choices=STATUS, default='IN')
    created_at = models.DateTimeField(default=timezone.now)
    saved_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.libelle} - {self.description}")
    

class Model(models.Model):
    STATUS = (
        ('IN', 'Inactive'),
        ('AC', 'Active'),
        ('AR', 'Archived'),
        )
    
    STATE = (
        ('PR', 'Production'),
        ('TR', 'Training'),
        ('DE', 'Development'),
        ('AR', 'Archived')
    )
    
    slug = models.SlugField(max_length=30, unique=True)
    libelle = models.CharField(max_length=100, unique=True)
    experience_id = models.ForeignKey(Experience, on_delete=models.PROTECT, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    score = models.IntegerField(default=0)
    path = models.FileField(upload_to='models/', validators=[ext_validator])
    state = models.CharField(max_length=2, choices=STATE, default='DE')
    status = models.CharField(max_length=2, choices=STATUS, default='IN')
    created_at = models.DateTimeField(default=timezone.now)
    saved_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.libelle} - {self.description}")

class Deploiement(models.Model):
    STATUS = (
        ('IN', 'Inactive'),
        ('AC', 'Active'),
        ('AR', 'Archived'),
        )
    STATE=(
        ('PR', 'Production'),
        ('TR', 'Training'),
        ('DE', 'Development'),
        ('AR', 'Archived')
        )
    
    slug = models.SlugField(max_length=30, unique=True)
    model_id = models.ForeignKey(Model, on_delete=models.PROTECT, blank=True, null=True)
    experience_id = models.ForeignKey(Experience, on_delete=models.PROTECT, blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS, default='IN')
    state = models.CharField(max_length=2, choices=STATE, default='DE')
    created_at = models.DateTimeField(default=timezone.now)
    saved_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.model_id} - {self.experience_id}")