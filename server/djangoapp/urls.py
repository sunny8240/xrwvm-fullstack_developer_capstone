# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    path(route='login', view=views.login_user, name='login'),
    # path('logout/', views.logout_request, name='logout'), 
    path('logout', views.logout_user, name='logout'), 
    path('register/', views.registration, name='register'),
    path('get_cars', views.get_cars, name='getcars'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
