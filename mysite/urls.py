from django.contrib import admin
from django.urls import path
from ums import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('dept/list/', views.dept_list),
    path('dept/add/', views.dept_add),
    path('dept/delete/', views.dept_delete),
    path('dept/<int:nid>/edit/', views.dept_edit),

    path('user/list/', views.user_list),
    path('user/add/', views.user_add),

    path('user/model/form/add/', views.user_model_form_add),
    path('user/<int:nid>/edit/', views.user_edit),
    path('user/delete/<int:nid>', views.user_delete),
    path('user/<int:nid>/edit_user_password/', views.edit_user_password),
    path('login/', views.login),
    path('logout/', views.logout),
]
