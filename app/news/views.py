from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from news.models import News
# Create your views here.
@csrf_exempt
@require_http_methods(["POST"])  
def defaultNews(request):
    list = {}
    if request.POST:
        name = request.POST['name']
        if name == 'newsInfo':
            list = newsInfo()
    return HttpResponse(json.dumps(list), content_type="application/json")

@csrf_exempt
@require_http_methods(["POST"])  
def newsInfo(request):
    list = {}
    array = []
    try:
        news = News.objects.filter(news_delete_id = 0)
        if len(news) > 0 :
            list['code'] = 1
            list['message'] = '查询成功'
            for new in news:
                array.append(News.getList(new))
            list['data'] = array
        else :
            list['code'] = -1
            list['message'] = '暂无信息'
        return HttpResponse(json.dumps(list), content_type="application/json")
    except:
        list['code'] = -2
        list['message'] = '查询失败'
        return HttpResponse(json.dumps(list), content_type="application/json")