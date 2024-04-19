from django.urls import path
from base import views  
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
    path('applied-interns/', views.applied_interns, name='applied_interns'),
    path('success/', views.success_page, name='success'),
    path('', views.apply, name='apply'),
    path('register/', views.register_intern, name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)