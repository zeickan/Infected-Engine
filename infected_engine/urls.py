from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'store.views.principal', name='home'),

    # Panel de control Store
    (r'^panel/', include('panel.urls')),

    # Store
    #url(r'^store/$', 'store.views.getProducts', name='store_getProducts'),
    #url(r'^store/checkout/$', 'store.views.basket', name='checkout'),
	#url(r'^store/checkout/(?P<step>\w{0,50})/$', 'store.views.basket', name='checkout_stepone'),
    #url(r'^store/(?P<slug>[-\w]+)/$', 'store.views.getProducts', name='store_getProducts'),
    #url(r'^store/product/(?P<slug>[-\w]+)/$', 'store.views.getProduct', name='store_getProduct'),
    #url(r'^store/color/(?P<slug>[-\w]+)/$', 'store.views.getProductByColor', name='store_getProductByColor'),

    #url(r'^debug/$', 'store.views.pruebas', name='pruebas'),

    # Seccion

    #url(r'^seccion/(?P<slug>[-\w]+)/$', 'store.views.seccion', name='seccion'),
    
    # API STORE    
    url(r'^api/addItem$', 'store.api.setBasket', name='api_additem'),
    url(r'^api/delItem$', 'store.api.delBasket', name='api_delitem'),
    url(r'^api/conekta$', 'store.api.conektaio', name='conekta_gateway'),
    
    
    # AUTH
    
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    (r'^accounts/',include('userprofile.urls')),
    url(r'^accounts/register/$', 'store.views.register', name='user_register'),

    #url(r'^accounts/profile/$', 'userprofile.views.userprofile', name='user_profile'),    
    #url(r'^accounts/login/registerSuccess$','userprofile.views.registersuccess'),

    # Basket
    
    url(r'^basket/$', 'store.views.basket', name='basket'),
    url(r'^basket/ipn$', 'store.views.ipn', name='ipn'),
    (r'^basket/request/ipn/notify/', include('paypal.standard.ipn.urls')),
    

    #url(r'^payment\.html$', 'store.views.payment', name='payment'),
    #url(r'^confirmation\.html$', 'store.views.confirmation', name='confirmation'),    
    #url(r'^payment-url/$', 'store.views.buy_my_item'),
    #url(r'^some/obscure/name/', include('paypal.standard.ipn.urls')),
    # url(r'^django_bootstrapping/', include('django_bootstrapping.foo.urls')),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Humans TXT & TinyMCE

    url(r'^humans\.txt$', 'humano.views.genTextFile', name='humanstxt' ),

    (r'^tinymce/', include('tinymce.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()