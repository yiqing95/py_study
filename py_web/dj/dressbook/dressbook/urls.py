from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import contacts.views

urlpatterns = patterns('',
    url(r'^$',contacts.views.ContactListView.as_view(),name='contacts-list'),
    url(r'^new$',contacts.views.CreateContactView.as_view(),name='contacts-new'),
    url(r'^edit/(?P<pk>\d+)/$',contacts.views.UpdateContactView.as_view(),
        name='contacts-edit'),
    url(r'^delete/(?P<pk>\d+)/$',contacts.views.DeleteContactView.as_view(),
        name='contacts-delete'),

    url(r'^contact/(?P<pk>\d+)/$',contacts.views.ContactView.as_view(),
        name='contacts-view'),
    # Examples:
    # url(r'^$', 'dressbook.views.home', name='home'),
    # url(r'^dressbook/', include('dressbook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
