from django.db.models import Count
from django.shortcuts import render
from django.http import JsonResponse


def chart_list(request):
    """ 数据统计页面 """
    return render(request, 'chart_list.html')


def chart_bar(request):
    """ 构造柱状图的数据 """
    # 数据可以去数据库中获取
    legend = ["Johnny", "Smith"]
    series_list = [
        {
            "name": 'Smith',
            "type": 'bar',
            "data": [15, 20, 36, 10, 10, 10]
        },
        {
            "name": 'Johnny',
            "type": 'bar',
            "data": [45, 10, 66, 40, 20, 50]
        }
    ]
    x_axis = ['1月', '2月', '4月', '5月', '6月', '7月']

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)



def chart_pie(request):
    """ 构造饼图的数据 """

    queryset = models.UserInfo.objects.values('dept__name').annotate(value=Count('id'))
    db_data_list = [
        {"value": item['value'], "name": f"{item['dept__name']}"}
        for item in queryset
    ]
    print(db_data_list)
    result = {
        "status": True,
        "data": db_data_list
    }
    return JsonResponse(result)


def chart_line(request):
    legend = ["上海", "广西"]
    series_list = [
        {
            "name": '上海',
            "type": 'line',
            "stack": 'Total',
            "data": [15, 20, 36, 10, 10, 10]
        },
        {
            "name": '广西',
            "type": 'line',
            "stack": 'Total',
            "data": [45, 10, 66, 40, 20, 50]
        }
    ]
    x_axis = ['1月', '2月', '4月', '5月', '6月', '7月']

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)


def highcharts(request):
    """ highcharts示例 """

    return render(request, 'highcharts.html')


from django.forms import ModelForm, Form
from ums import models


# class TTModelForm(Form):
#     name = forms.CharField(label="用户名")
#     ff = forms.FileField(label="文件")
#
#
# def tt(request):
#     if request.method == "GET":
#         form = TTModelForm()
#         return render(request, 'change.html', {"form": form})
#     form = TTModelForm(data=request.POST, files=request.FILES)
#     if form.is_valid():
#         print(form.cleaned_data)
#     return render(request, 'change.html', {"form": form})

class TTModelForm(ModelForm):
    class Meta:
        model = models.XX
        fields = "__all__"


def tt(request):
    instance = models.XX.objects.all().first()
    if request.method == "GET":
        form = TTModelForm(instance=instance)
        return render(request, 'tt.html', {"form": form})
    form = TTModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
    return render(request, 'tt.html', {"form": form})

