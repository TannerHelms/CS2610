from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('archive/', views.archive, name='archive'),
    path('about/', views.about, name='about'),
    path('techtips+css/', views.techtipscss, name='techtipscss'),
    path('techtips-css/', views.techtips, name='techtips'),
    path('plan/', views.plan, name='plan'),
    path('<int:blog_id>/comment/', views.comment, name='comment'),
    path('<int:blog_id>/detail/', views.detail, name='detail'),
]
