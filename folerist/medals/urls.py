from django.urls import path, re_path, register_converter

from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.about, name='add_page'),
    path('contact/', views.about, name='contact'),
    path('login/', views.about, name='login'),
    path('post/<int:post_id>', views.show_post, name='post')
]
