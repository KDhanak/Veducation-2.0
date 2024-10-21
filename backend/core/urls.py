from django.urls import path, include
from . import views

urlpatterns = [
    path("api/publication", views.GetPublication.as_view(), name="publication_view"),
    path("api/register",views.RegisterAPI.as_view(), name="register_view"),
    path("api/logout", views.LogoutView.as_view(), name="logout"),
    path("api/login", views.LoginView.as_view(), name="login"),
    path("api/token/refresh", views.CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("api/token", views.CustomTokenObtainPairView.as_view(), name="token_obtain_par"),
    path("api/user/me", views.AuthenticatedUser.as_view(), name="authenticated_user"),
]
