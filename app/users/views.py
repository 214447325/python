# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.decorators import csrf
from users.models import Users
import time
# Create your views here.
# @csrf_exempt
# @require_http_methods(["POST"])
# def defaultUsers(request):
#     print('-----')
#     list = {}
#     if request.POST:
#         name = request.POST['name']
#         print(name)
#         if name == 'addUser':
#             map = {}
#             map['userName'] = request.POST['userName']
#             map['birthday'] = request.POST['birthday']
#             map['phone'] = request.POST['phone']
#             map['password'] = request.POST['password']
#             list = addUser(map)
#     return HttpResponse(json.dumps(list), content_type="application/json")

# def usersInit(request):
#     list = {}
#     list['user'] = ''
#     return render(request, 'pages/user.html', list)

def addUser(request):
    list = {}
    t = time.strftime("%Y-%m-%d", time.localtime())
    try:
        user = Users(userName = request.GET['userName'], phone = request.GET['phone'], password = request.GET['password'])
        user.save()
        list['code'] = 1
        list['message'] = '用户注册成功'
    except:
        list['code'] = -2
        list['message'] = '用户注册失败'


# 修改用户的数据
def upadate(request):
    list = {}
    try:
        user = Users.objects.get(id=5)
        user.userName = 'vvvv'
        user.save()
        list['code'] = 1
        list['message'] = '用户修改成功'
    except:
        list['code'] = -1
        list['message'] = '用户修改失败'
    return HttpResponse(json.dumps(list,ensure_ascii=False), content_type="application/json,charset=utf-8")

# 删除用户
def deleteUser(request):
    cache.set('bb', '22', timeout=None)
    print(cache.get('bb'))
    list = {}
    try:
        user = Users.objects.get(id=10)

        user.delete()
        list['code'] = 1
        list['message'] = '用户删除成功'
    except:
        list['code'] = -1
        list['message'] = '用户删除失败'
    return HttpResponse(json.dumps(list,ensure_ascii=False),content_type='application/json,charset=utf-8')