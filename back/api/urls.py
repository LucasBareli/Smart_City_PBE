from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)  

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sensores', SensoresView.as_view(), name='sensores'),
    path('sensores/<int:pk>', SensoresAPIView.as_view(), name='sensores'),
    path('ambientes', AmbientesView.as_view(), name='ambientes'),
    path('ambientes/<int:pk>', AmbientesAPIView.as_view(), name='ambientes'),
    path('sensores', SensoresView.as_view(), name='historicos'),
    path('sensores/<int:pk>', SensoresAPIView.as_view(), name='historicos')
]
