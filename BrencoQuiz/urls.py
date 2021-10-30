from django.contrib import admin
from django.urls import path, include
from Quiz.views import *
from knox import views as knox_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', home,name='home'),
    path('addQuestion/', addQuestion,name='addQuestion'),
    path('question/', question,name='questions'),
    path('question/update/<int:id>',update,name='update'),
    path('question/delete/<int:id>',delete,name='delete'),
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    path('register/', registerPage,name='register'),
    path('showresult/', showResult,name='showresult'),
    path('showresult/delete/<int:id>', deleteresult, name='delete'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

