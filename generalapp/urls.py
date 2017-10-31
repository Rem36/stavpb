from django.conf.urls import url
from generalapp import views
import generalapp

app_name = 'generalapp'

urlpatterns = [
	url(r'^$', generalapp.views.index, name='index'),
	url(r'^post/new/$', generalapp.views.post_add, name='post_add'),
	url(r'^posts/(?P<post_id>[0-9]+)/$', generalapp.views.show_post, name='show_post')
]