# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

pp_name = 'djangoapp'
urlpatterns = [
    # path for logout

    # path for registration
   
    # path for login
    path(route='login', view=views.login_user, name='login'),
    # path for get_dealerships
  
  
    # path for dealer reviews view

    # path for add a review view

    # path for reviews from dealer_id

    # path for get_cars view
    path(route='get_cars', view=views.get_cars, name='getcars'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)