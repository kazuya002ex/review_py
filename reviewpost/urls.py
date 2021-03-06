from django.contrib import admin
from django.urls import path
from .views import signupview, loginview, listview, detailview, logoutview, evaluationview

urlpatterns = [
  path('admin/', admin.site.urls),
  path('signup/', signupview, name='signup'),
  path('login/', loginview, name='login'),
  path('list/', listview, name='list'),
  path('detail/<int:pk>/', detailview, name='detail'),
  path('logout/', logoutview, name='logout'),
  path('evaluation/<int:pk>/', evaluationview, name='evaluation'),
]
