from django.urls import path
from . import views

app_name='recruitor'
urlpatterns=[


path('list1/',views.ListCompany.as_view(),name='list1'),
path('create1/',views.CreateCompany.as_view(),name='create1'),
path('delete1/<int:pk>',views.DeleteCompany.as_view(),name='delete1'),
path('update1/<int:pk>',views.UpdateCompany.as_view(),name='update1'),
path('detail1/<int:pk>',views.DetailCompany.as_view(),name='detail1'),

]
