from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from empapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('profile/',views.ProfileView.as_view()),
    path('api/auth/', views.CustomAuthToken.as_view()),   
    path('employee/',views.employeeApi),
    path('employee/<int:id>/',views.employeeApi),
    path('leave/',views.leaveApi),
    path('leave/<int:id>/',views.leaveApi),
    path('savefile', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)