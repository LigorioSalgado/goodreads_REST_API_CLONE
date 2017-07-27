from django.conf.urls import url,include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url(r'^authors/', include('modules.Authors.urls')),
    url(r'^books/', include('modules.Books.urls')),
    url(r'^auth/', obtain_jwt_token),
    url(r'^docs/', include_docs_urls(title = "Goodreads REST API")),

]