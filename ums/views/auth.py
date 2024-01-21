from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from io import BytesIO
from ums import models
from ums.utils.code import check_code
from ums.utils.bootstrap import BootstrapForm


def edit_user_password(request):
    return render(request, 'edit_user_password.html')


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证码的校验
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'login.html', {'form': form})

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
    return render(request, 'login.html', {'form': form})


def image_code(request):
    """ 生成图片验证码 """

    # 调用pillow函数，生成图片
    img, code_string = check_code()

    # 写入到自己的session中（以便于后续获取验证码再进行校验）
    request.session['image_code'] = code_string
    # 给Session设置60s超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def logout(request):
    request.session.flush()
    return redirect('/login/')


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
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True
    )
