from django.contrib import admin
from django.urls import path
from insurance import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('apply/<int:plan_id>/', views.apply_insurance, name='apply_insurance'),
    path('success/', views.application_success, name='application_success'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
]