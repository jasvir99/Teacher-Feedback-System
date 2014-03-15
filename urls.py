from django.conf.urls.defaults import *
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^hello', TemplateView.as_view(template_name='hello.html')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),   
)

