from django.urls import path
# from app_users.views import login_view, AnotherLoginView, logout_view, AnotherLogoutView, register_view
from app_users.views import login_view, logout_view, register_view, another_register_view, restore_password



urlpatterns = [
    path('login/', login_view, name='login'),
    # path('another_login/', AnotherLoginView.as_view(), name='another_login'),
    path('logout/', logout_view, name='logout'),
    # path('another_logout/', AnotherLogoutView.as_view(), name='another_logout'),
    path('register/', register_view, name='register'),
    path('another_register/', another_register_view, name='another_register'),
    path('restore_password/', restore_password, name='restore_password'),
]