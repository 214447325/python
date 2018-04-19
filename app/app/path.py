"""
用一个方法来控制请求的地址
"""
from django.conf.urls import url
from django.contrib import admin
from index import views as index
from news import views as news
from users import views as users
def path():
    urlpatterns = [
#         主方法
#        url(r'^$', views.index),
#        url(r'index.html$', views.index),
       url(r'^admin/', admin.site.urls),
#        获取新闻的标题
       url(r'newsInfo$', news.newsInfo),
#        用户中心
#        url(r'user.html$', users.usersInit),
# #        用户信息
#        url(r'users/', users.defaultUsers),
#        首页信息
       url(r'indexInfo$',index.indexInfo),
        # 添加用户的信息
       url(r'addUser',users.addUser),
        # 修改用户的信息
       url(r'upadate',users.upadate),
        # 删除用户
       url(r'deleteUser',users.deleteUser),
    ]
    return urlpatterns