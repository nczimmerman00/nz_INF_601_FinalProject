from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home page
    path('', views.home_view, name='home'),
    # Account registration page
    path("register", views.register_request, name="register"),
    # Login page
    path("login", views.login_request, name="login"),
    # Logout button
    path("logout", views.logout_request, name="logout"),
    # Submit article
    path("submit", views.submit_article, name="submit"),
    # Filtered articles
    path("search/<search>", views.search, name='search')
]

handler404 = views.error_404_view
