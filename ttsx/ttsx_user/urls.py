from django.conf.urls import url
import views

urlpatterns=[
    url(r'^register/$',views.register),
    url(r'^register_handle/$',views.register_handle),
    url(r'^register_valid/$',views.register_valid),
    url(r'^login/$',views.login),
    url(r'^login_handle/$',views.login_handle),

]