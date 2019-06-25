"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings

from django.conf.urls.static import static
from blog import views

from django.contrib.auth import views as auth_views
# from blog.views import ArticleListView
# from blog.core import views as core_views



urlpatterns = [
    path('', views.Home.as_view(), name='home'), #for class based views

    path('admin/', admin.site.urls),
    # path('', ArticleListView.as_view(), name='home'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('detail_category/<int:id>', views.detail_category, name='detail_category'),
    # path('register/', views.register, name='register'),

    # path('signup/', views.SignUp, name='signup'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('contact/', views.ContactUs.as_view(), name='contact'),
    # path('login/', views.login_request, name='login'),
    # path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # url(r'^login/$', views.LoginView.as_view(template_name=template_name), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('logout/', auth_views.logout, {})

    path('business/', views.business, name='business'),
    path('technology/', views.technology, name='technology'),
    path('sport/', views.sport, name='sport'),
    path('politics/', views.politics, name='politics'),
    path('others/', views.others, name='others'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
