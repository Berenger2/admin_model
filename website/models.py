from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.core.exceptions import ValidationError
import random
import string

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
    experience = models.ForeignKey(Experience, on_delete=models.PROTECT, blank=True, null=True)
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
    model = models.ForeignKey(Model, on_delete=models.PROTECT, blank=True, null=True)
    experience = models.ForeignKey(Experience, on_delete=models.PROTECT, blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS, default='IN')
    state = models.CharField(max_length=2, choices=STATE, default='DE')
    created_at = models.DateTimeField(default=timezone.now)
    saved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def clean(self):
        if self.status == 'AC' and self.state == 'PR':
            existing_deploiements = Deploiement.objects.filter(
                experience=self.experience,
                status='AC',
                state='PR'
            )
            if self.pk:
                existing_deploiements = existing_deploiements.exclude(pk=self.pk)
            if existing_deploiements.exists():
                raise ValidationError("An active and production deployment already exists for this experience.")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_random_slug()
        self.full_clean()  # Calls clean() method
        super(Deploiement, self).save(*args, **kwargs)

    def generate_random_slug(self):
        while True:
            slug = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
            if not Deploiement.objects.filter(slug=slug).exists():
                return slug

    def __str__(self):
        return (f"{self.model_id} - {self.experience_id}")