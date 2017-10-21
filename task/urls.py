from django.conf.urls import url
from . import views
from django.core.urlresolvers import reverse

#Patterns used in this application
urlpatterns =[ 
    url(r'^login/$','django.contrib.auth.views.login', name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
	url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^password-change/$','django.contrib.auth.views.password_change', name='password_change'),
	url(r'^password-change/done/$','django.contrib.auth.views.password_change_done',name='password_change_done'),
	url(r'^password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
	url(r'^password-reset/done/$','django.contrib.auth.views.password_reset_done', name='password_reset_done'),
	url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$','django.contrib.auth.views.password_reset_confirm',name='password_reset_confirm'),
	url(r'^password-reset/complete/$','django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
	url(r'^register/$',views.register,name='register'),
	url(r'^edit/$', views.edit,name='edit'),
	url(r'^(?P<id>\d+)/$', views.detail, name='detail'), # Shows selected company materials
	url(r'^(?P<id>\d+)/(?P<material_id>\d+)/$', views.material_detail, name='material_detail'), # Shows selected material
	url(r'^materialedit/(?P<id>\d+)/$', views.material_edit, name='materialedit'), # This pattern is used to editing materials detail
	url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'), # This pattern delete selected material

]