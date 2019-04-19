from django.conf.urls import url
from . import views

app_name = "polls"

urlpatterns = [
    url(r'^pollslist/$',views.Pollslist,name='pollslist'),
    url(r'^choice/(\d+)/$',views.Choice,name='choice'),
    url(r'^choicetool/(\d+)$',views.ChoiceTool,name='choicetool')

]