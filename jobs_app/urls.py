from django.urls import path
from . import views

app_name='jobs_app'
urlpatterns=[
path('',views.HomePage.as_view(),name='home'),
path('list/',views.ListProfile.as_view(),name='list'),
path('create/',views.CreateProfile.as_view(),name='create'),
path('delete/<int:pk>',views.DeleteProfile.as_view(),name='delete'),
path('update/<int:pk>',views.UpdateProfile.as_view(),name='update'),
path('detail/<int:pk>',views.DetailProfile.as_view(),name='detail'),
]
