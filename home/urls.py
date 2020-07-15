from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = 'Blog Admin Panel'                    # default: "Django Administration"
admin.site.index_title = 'Site Administration Data'            # default: "Site administration"
admin.site.site_title = 'Blog-Admin Panel'                     # default: "Django site admin"
urlpatterns = [
    path('',views.index,name='home' ),
    path('contact/',views.contact,name='contactus' ),
    path('aboutus/',views.about,name='aboutus' ),
    path('data/',views.data,name='data' ),
    path('signup/',views.createuser,name='createuser'),
    path('handlelogin/',views.handlelogin,name='login'),
    path('handlelogout/',views.handlelogout,name='logout')
   
]