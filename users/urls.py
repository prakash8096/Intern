from django.urls import path
from .views import basefile,register,home,profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', basefile,name='base' ),
    path('register', register,name='register' ),
    # path('home', home,name='home' ),
    path('login',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('passwordreset/',auth_views.PasswordResetView.as_view(template_name='passwordreset.html'),name='passwordreset'),
    path('passwordresetdone/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('passwordresetconfirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('passwordresetcomplete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

    path('profile',profile,name='profile'),

    
]