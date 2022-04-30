from django.urls import path
from . import views
#from signup.views import signupaction


urlpatterns = [
   path('', views.signupaction,name='home'),
    

]