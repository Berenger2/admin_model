from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('logout/',views.logout_user, name='logout'),
    path('login/',views.login_user, name='login'),
    path('models/',views.models, name='models'),
    path('model/add/',views.add_model, name='add_model'),
    path('model/edit/<str:slug>',views.model_edit, name='model_edit'),
    path('model/<str:slug>',views.model_view, name='model_view'),


    # path('model/<str:>',views.logout_user, name='logout'),
]
