from django.db import models

class Department(models.Model):
    name = models.CharField(verbose_name='部门名称', max_length=32)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    salary = models.DecimalField(verbose_name='工资', max_digits=10, decimal_places=2)
    gender_choices =(
        (1, '男'),
        (2, '女')
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)
    create_time = models.DateTimeField(verbose_name='创建时间')

    # dept_id = models.ForeignKey(to=Department, to_field='id', null=True, blank=True, on_delete=models.SET_NULL)
    dept = models.ForeignKey(verbose_name="部门", to='Department', to_field="id", on_delete=models.CASCADE)