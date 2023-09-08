from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='HCHome'),
    path('draft/', views.draft, name='HCDraft'),
]
