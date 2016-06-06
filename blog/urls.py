from django.conf.urls import include, url
from . import views

urlpatterns = [
		       url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
               url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
               url(r'^$', views.post_list, name='post_list'),
               url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
               url(r'^post/new/$', views.post_new, name='post_new'),
               url(r'^user/(?P<pk>\d+)/$', views.user_post_list, name='user_post_list'),
			   url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
			   url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
               ]