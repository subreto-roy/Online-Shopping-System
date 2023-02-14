
from django.contrib import admin
from django.urls import path, include

#To show media files

from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
#from django.templatetags.static import static
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('App_Shop.urls')),
    path('account/' ,include('App_Login.urls')),
    path('shop/',include('App_Order.urls')),
    path('payment/',include('App_Payment.urls'))

]
#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
