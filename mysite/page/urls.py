from django.conf.urls import url
from page.views import (MysitePageLayoutView,
         MysitePageFormView, 
        #  MysitePageCreateView, 
         MysitePageDetailView)

urlpatterns = [
    url(r'^page/', MysitePageLayoutView.as_view(), name='page-list'),
    url(r'^page_forum/', MysitePageFormView.as_view(), name='page-forum'),
    # url(r'^page_create/', MysitePageCreateView.as_view(), name='page-create'),
    url(r'^page_detail/', MysitePageDetailView.as_view(), name='page-detail'),
    
]