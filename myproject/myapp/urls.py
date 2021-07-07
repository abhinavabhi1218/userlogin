from django.urls import path, include
from . import views
from django.contrib.auth import  views as auth_views


urlpatterns = [
    path("", views.home, name='Home'),
    path('About/',views.About, name='About'),
    path('contact/',views.contact, name='contact'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('logout/',views.user_logout, name='logout'),
    path('signup/',views.user_signup, name='signup'),
    path('login/',views.user_login, name='login'),
    path('addpost/', views.add_post, name='addpost'),
    path('delete/<int:id>/', views.delete_post, name='delete'),
    path('update/<int:id>/', views.update_post, name='update'),
    path('searched',views.search_view, name='searched'),

    # path('accounts/',include('django.contrib.auth.urls'))
    path('password_reset/', auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password/done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_conmplete', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]
