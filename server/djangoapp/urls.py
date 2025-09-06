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
     # Dealers list
    path('get_dealers', views.get_dealerships, name='get_dealers'),
    path('get_dealers/<str:state>', views.get_dealerships, name='get_dealers_by_state'),

    # Dealer details
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='dealer_details'),

    # Dealer reviews
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='dealer_reviews'),
    path('add_review', views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
