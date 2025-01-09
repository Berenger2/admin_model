from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('logout/',views.logout_user, name='logout'),
    path('login/',views.login_user, name='login'),
    
    # Models
    path('models/',views.models, name='models'),
    path('model/add/',views.add_model, name='add_model'),
    path('model/edit/<str:slug>',views.model_edit, name='model_edit'),
    path('model/<str:slug>',views.model_view, name='model_view'),

    # Experiences
    path('experiences/',views.experiences, name='experiences'),
    path('experience/add/',views.add_experience, name='add_experience'),
    path('experience/edit/<str:slug>',views.experience_edit, name='experience_edit'),
    path('experience/<str:slug>',views.experience_view, name='experience_view'),
    
    # Deploiements
    path('deploiements/',views.deploiements, name='deploiements'),
    path('deploiement/add/',views.add_deploiement, name='add_deploiement'),
    path('deploiement/edit/<str:slug>',views.deploiement_edit, name='deploiement_edit'),
    path('deploiement/<str:slug>',views.deploiement_view, name='deploiement_view'),
    path('ajax/load-models/', views.load_models, name='ajax_load_models'),

    # path('model/<str:>',views.logout_user, name='logout'),
]