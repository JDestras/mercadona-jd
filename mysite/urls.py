from django.contrib import admin
from django.urls import path, include
from catalog import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'Mercadona - Catalog Administration '
admin.site.site_title = 'Mercadona - Catalog Administration '
admin.site.index_title = 'Dashboard'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/', permanent=True)),
    path('home/', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('filtered_products/<int:category_id>/', views.filtered_products, name='filtered_products'),
    path('about/', views.about, name='about'),
] 

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)