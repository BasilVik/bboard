import imp
from django.urls import path

from .views import index, other_page, profile, BBLoginView

app_name = 'main'
urlpatterns = [
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
