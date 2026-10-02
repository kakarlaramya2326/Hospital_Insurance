from django.contrib import admin
from django.urls import path
from insurance import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('plans/', views.plans, name='plans'),

    path('apply/<int:plan_id>/',views.apply_insurance,name='apply_insurance'
    ),

    path('success/',views.application_success,name='application_success'
    ),
    path(
        'contact/',
        views.contact,
        name='contact'
    ),

    path(
        'contact-success/',
        views.contact_success,
        name='contact_success'
    ),
    path('about/', views.about, name='about'),

    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]