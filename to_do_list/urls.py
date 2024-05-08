from django.contrib import admin
from django.urls import path, include
from to_do import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/<int:id>', views.ToDoListRestAPI.as_view(), name="todo_list"),
    path('todo/', views.ToDoListRestAPI.as_view(), name="todo_detail"),
    path("gettoken/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refreshtoken/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verifytoken/", TokenVerifyView.as_view(), name="token_verify"),
    path("auth/", include("rest_framework.urls", namespace="rest_framework"))
]
