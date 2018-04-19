from django.shortcuts import render
from django.http import HttpResponse
from index.models import Icon
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
# Create your views here.
# 进入页面调用该方法
'''
    code = 1为数据查询正常有数据
    code = -1 表示从数据库查询出来的时候没有数据
    code = -2 表示数据库查询出现异常
'''
def index(request):
    list = {}
    array = []
    try:
        icons = Icon.objects.filter(iconId = 1)
        if len(icons) > 0:
            list['code'] = 1
            list['message'] = '查询正常'
            for icon in icons:
                array.append(icons)
            list['data'] = array
        else:
            list['code'] = -1
            list['message'] = '暂无数据'
        icons.close()
        return render(request, 'pages/index.html', list)
    except:
        list['code'] = -2
        list['message'] = '数据查询异常'
        return render(request, 'pages/index.html', list)
  
'''
    获取首页的信息并且拼装成字典
'''
@csrf_exempt
@require_http_methods(["POST"])
def indexInfo(request):
    list = {}
    array = []
    try:
        icons = Icon.objects.filter(iconId = 1)
        if len(icons) > 0:
            list['code'] = 1
            list['message'] = '查询正常'
            for icon in icons:
                print(icon)
                array.append(Icon.getIconList(icon))
            list['data'] = array
        else:
            list['code'] = -1
            list['message'] = '查询失败'
        return HttpResponse(json.dumps(list), content_type="application/json")
    except Exception as e:
        list['code'] = -2
        list['message'] = '暂无数据'
        return HttpResponse(json.dumps(list), content_type="application/json")