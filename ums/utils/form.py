from ums import models
from django import forms
from ums.utils.bootstrap import BootstrapModelForm
class UserModelForm(BootstrapModelForm):
    username = forms.CharField(min_length=3, label="用户名")

    class Meta:
        model = models.UserInfo
        fields = ["username", "password", "age", 'salary', 'create_time', "gender", "dept"]
