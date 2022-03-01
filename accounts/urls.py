from django.urls import path

from . import views
from django.contrib.auth.views import LogoutView

app_name='accounts'
urlpatterns=[
path('login1/',views.CompanyLoginView.as_view(),name='login1'),
path('login/',views.CustomLoginView.as_view(),name='login'),

path('logout/',views.CustomLogoutView.as_view(),name='logout'),
path('logout1/',views.CLogoutView.as_view(),name='logout1'),
path('signup/',views.SignUp.as_view(),name='signup'),
path('signup1/',views.CSignUp.as_view(),name='signup1'),
]
