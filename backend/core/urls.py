from django.urls import path, include
from . import views
from django.conf import settings
from dj_rest_auth.views import LoginView, LogoutView

urlpatterns = [
    path("api/publication", views.getData),
    path("authmanagement/", include("dj_rest_auth.urls")),
    path("authmanagement/registration",
         include("dj_rest_auth.registration.urls")),
    path("accounts/", include("allauth.urls")),
    path('authmanagement/login/', LoginView.as_view(), name='rest_login'),
    path('authmanagement/logout/', LogoutView.as_view(), name='rest_logout'),
]
