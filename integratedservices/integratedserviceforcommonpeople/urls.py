from django.urls import path
from . import views
from .views import service_registration, service_list
urlpatterns = [
    path('', views.index, name=''),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('home/', views.home, name='home'),
    path('service/register/', service_registration, name='service_registration'),
    path('service/list/', service_list, name='service_list'),
    path('profile/', views.profile, name='profile'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('logout', views.logout_view, name='logout'),

]
