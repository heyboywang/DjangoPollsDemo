from django.conf.urls import url
from . import views

app_name = "polls"

urlpatterns = [
    url(r'^pollslist/$',views.Pollslist,name='pollslist')

]