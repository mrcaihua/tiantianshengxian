from django.conf.urls import include, url
import views
urlpatterns = [
    url('^register/$',views.register)

]
