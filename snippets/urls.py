from django.conf.urls import url
from snippets import views_3_mixins
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views_3_mixins.api_root),
    url(r'^snippets/$', views_3_mixins.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views_3_mixins.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^users/$', views_3_mixins.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views_3_mixins.UserDetail.as_view(), name='user-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views_3_mixins.SnippetHighlight.as_view(), name='snippet-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
