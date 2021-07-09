from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
            path("", views.first_page, name='dashboard'),
            path("home/", views.index_view, name='home'),
            path('storage/', views.product_form_view, name='storage'),
            path('update/<int:id>', views.update_product, name='update'),
            path('delete/<int:id>', views.delete_product, name='delete'),
            path('signup/', views.user_signup_view, name='signup'),
            path('login/', views.user_login_view, name='login'),
            path('logout/', views.page_lought_view, name='logout'),
            path('product/<int:id>/', views.view_products, name='product'),
            path('sort/', views.order_by_name, name='sort'),
            path('sort1/', views.order_by_name1, name='sort1'),
            path('sort2/', views.order_by_cost_high, name='sort2'),
            path('sort3/', views.order_by_cost_low, name='sort3'),
            path('sort4/', views.order_by_rating, name='sort4'),
            path('search/', views.search_products, name='search'),


            # path('login/', auth_views.LoginView.as_view(template_name='dongo/login.html'))
]
