from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("api/publication", views.GetPublication.as_view(), name="publication_view"),
    path("register/",views.RegisterAPI.as_view(), name="register_view"),
    # path("api/token/", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("api/csrf-token", views.get_csrf_token, name='csrf-tpken')
]
