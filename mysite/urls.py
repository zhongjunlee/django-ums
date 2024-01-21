from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from ums.views import chart
from ums.views import dept, user, auth, city

urlpatterns = [
    path('dept/list/', dept.dept_list),
    path('dept/detail/', dept.dept_detail),
    path('dept/add/', dept.dept_add),
    path('dept/delete/', dept.dept_delete),
    path('dept/edit/', dept.dept_edit),
    path('dept/multi/', dept.dept_multi),

    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/model/form/add/', user.user_model_form_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/delete/<int:nid>', user.user_delete),


    path('user/<int:nid>/edit_user_password/', auth.edit_user_password),
    path('login/', auth.login),
    path('logout/', auth.logout),
    path('image/code/', auth.image_code),

    # 数据统计
    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),
    path('chart/pie/', chart.chart_pie),
    path('chart/line/', chart.chart_line),
    path('chart/highcharts/', chart.highcharts),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

    # 城市列表
    path('city/list/', city.city_list),
    path('city/add/', city.city_add),

]
