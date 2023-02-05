from django.urls import path
from api import views   ## to access the views in the url pattern

urlpatterns = [
    path('registrants/', views.registrant_list ),
    path('registrant_detail/<str:pk>/', views.registrant_detail),


]