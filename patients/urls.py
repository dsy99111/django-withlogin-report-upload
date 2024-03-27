from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('upload/', views.upload_report, name='upload_report'),
    path('view/', views.view_reports, name='view_reports'),
    path('delete/<int:report_id>/', views.delete_report, name='delete_report'),
    path('',views.home,name="home"),
    path('register/', views.patient_register, name='patient_register'),
    path('login/', views.patient_login, name='patient_login'),
    path('report_panel/', views.user_report_panel, name='user_report_panel'),
    path('logout/', views.patient_logout, name='logout'),

]
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
