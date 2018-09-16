from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.render_home, name='render_home'),
    url(r'^get_chart_data/$',views.get_chart_data,name='get_chart_data'),
]