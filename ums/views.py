from django.shortcuts import render, redirect
from django import forms

from ums import models
from ums.utils.pagination import Pagination
from ums.utils.form import UserModelForm
from ums.utils.bootstrap import BootstrapForm

def dept_list(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["name__contains"] = search_data

    queryset = models.Department.objects.filter(**data_dict)


    page_object = Pagination(request, queryset)

    context = {
        "search_data": search_data,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 页码
    }

    return render(request, 'dept_list.html', context)

def dept_add(request):
    if request.method == 'GET':
        return render(request, "dept_add.html")

    name = request.POST.get('name')
    # 入库
    models.Department.objects.create(name=name)
    return redirect('/dept/list')

def dept_delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/dept/list")

def dept_edit(request, nid):
    """ 修改部门 """
    if request.method == "GET":
        # 根据nid，获取他的数据 [obj,]
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, 'dept_edit.html', {"row_object": row_object})

    # 获取用户提交的部门名称
    name = request.POST.get("name")

    # 根据ID找到数据库中的数据并进行更新
    # models.Department.objects.filter(id=nid).update(name=name,其他=123)
    models.Department.objects.filter(id=nid).update(name=name)

    # 重定向回部门列表
    return redirect("/dept/list/")

def user_list(request):
    """ 用户管理 """

    # 获取所有用户列表 [obj,obj,obj]
    # queryset = models.UserInfo.objects.all()
    """
    # 用Python的语法获取数据
    for obj in queryset:
        print(obj.id, obj.name, obj.salary, obj.create_time.strftime("%Y-%m-%d"), obj.gender, obj.get_gender_display(), obj.depart_id, obj.depart.title)
        # print(obj.name, obj.depart_id)
        # obj.depart_id  # 获取数据库中存储的那个字段值
        # obj.depart.title  # 根据id自动去关联的表中获取哪一行数据depart对象。
    """
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["username__contains"] = search_data

    queryset = models.UserInfo.objects.filter(**data_dict).order_by("-create_time")

    page_object = Pagination(request, queryset)

    context = {
        "search_data": search_data,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 页码
    }

    return render(request, 'user_list.html', context)

def user_add(request):
    """ 添加用户（原始方式） """

    if request.method == "GET":
        context = {
            'gender_choices': models.UserInfo.gender_choices,
            "dept_list": models.Department.objects.all()
        }
        return render(request, 'user_add.html', context)

    # 获取用户提交的数据
    user = request.POST.get('username')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    salary = request.POST.get('salary')
    ctime = request.POST.get('ctime')
    gender = request.POST.get('gd')
    dept = request.POST.get('dp')

    # 添加到数据库中
    models.UserInfo.objects.create(username=user, password=pwd, age=age,
                                   salary=salary, create_time=ctime,
                                   gender=gender, dept_id=dept)

    # 返回到用户列表页面
    return redirect("/user/list/")

def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")

def user_edit(request, nid):
    # 如果是GET请求，进行数据回显并跳转到编辑页面
    if request.method == "GET":
        row_object = models.UserInfo.objects.filter(id=nid).first()
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {"form": form})

    # 如果是POST请求，先根据id获取对象然后修改数据并跳转到用户列表页面
    row_object = models.UserInfo.objects.filter(id=nid).first()
    form = UserModelForm(data=request.POST, instance=row_object)
    # 验证字段
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    # 验证失败返回错误提示并跳转到用户编辑页面
    return render(request, 'user_edit.html', {"form": form})

def edit_user_password(request):
    return render(request, 'edit_user_password.html')

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

    form = LoginForm(request.POST)
    # 表单字段验证
    if form.is_valid():
        # 查询数据库匹配用户名密码是否正确
        user_obj = models.UserInfo.objects.filter(**form.cleaned_data).first()
        print(user_obj)
        if not user_obj:
            form.add_error('password', '用户名或密码错误')
            return render(request, 'login.html', {'form': form})
        request.session['info'] = {'id': user_obj.id, 'username': user_obj.username}
        # 设置 session 过期时间为30分钟
        request.session.set_expiry(60 * 30)
        return redirect('/user/list/')
    return render(request, 'login.html', {'form', form})

def logout(request):
    request.session.flush()
    return redirect('/login/')


def user_model_form_add(request):
    """ 添加用户（ModelForm版本）"""
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {"form": form})

    # 用户POST提交数据，数据校验。
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        # {'username': '123', 'password': '123', 'age': 11, 'salary': Decimal('0'), 'create_time': datetime.datetime(2011, 11, 11, 0, 0, tzinfo=<UTC>), 'gender': 1, 'dept': <Department: IT运维部门>}
        # print(form.cleaned_data)
        # models.UserInfo.objects.create(..)
        form.save()
        return redirect('/user/list/')

    # 校验失败（在页面上显示错误信息）
    return render(request, 'user_model_form_add.html', {"form": form})


class LoginForm(BootstrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True,
    )
