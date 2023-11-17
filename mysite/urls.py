from django.contrib import admin
from django.urls import path
from catalog import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.site.site_header = 'Mercadona - Catalog Administration '
admin.site.site_title = 'Mercadona - Catalog Administration '
admin.site.index_title = 'Dashboard'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('filtered_products/<int:category_id>/', views.filtered_products, name='filtered_products'),
    path('about/', views.about, name='about'),
] 


urlpatterns += staticfiles_urlpatterns()