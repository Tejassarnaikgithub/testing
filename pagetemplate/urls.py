from pagetemplate import views
from django.urls import path



urlpatterns = [
    path('', views.home),
    path('/scRNASeq_Report',views.scRNASeq_Report),
    path('display/', views.combined_display),
    path('display2/', views.display2),

    
    
    



]