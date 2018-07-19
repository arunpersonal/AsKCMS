from django.conf.urls import url
from page.views import MysitePageListView, MysitePageFormView

urlpatterns = [
    url(r'^pages/', MysitePageListView.as_view(), name='page-list'),
    url(r'^create/', MysitePageFormView.as_view(), name='page-create'),
]