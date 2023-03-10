from django.urls import path
from api import views   ## to access the views in the url pattern

urlpatterns = [
    path('registrants/', views.registrant_list ),
    path('registrant_detail/<str:pk>/', views.registrant_detail),
    path('registrant_create/', views.register_registrant ),
    path('registrant_update/<str:pk>/', views.registrant_update),
    path('registrant_delete/<str:pk>/', views.registrant_delete),


]