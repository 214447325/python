from django.db import models
# Create your models here.
'''
此类用作主页的新闻
'''
class News(models.Model):
    
#     新闻的Id
    news_id = models.IntegerField(primary_key = True)
    
#     新闻的名称，不能为空值
    news_name = models.CharField(max_length = 200,blank = False)
    
#     新闻的创建时间，不能为空值
    news_create_date = models.DateField(auto_now_add = True, blank = False)
    
#     新闻的删除时间，可以为空值
    news_delete_date = models.DateField(auto_now_add = True, blank = True)
    
#     判断该新闻是否应经被删除0表示该新闻还有效1表示该新闻已经被删除，不能为空值
    news_delete_id = models.IntegerField(default = 0, blank = False)
    
#     帖子的内容
    news_content = models.CharField(max_length = 300,blank = False)
    

    def getList(self):
        list = {}
        list['newsId'] = self.news_id
        list['newsName'] = self.news_name
        list['newsCreateDate'] = str(self.news_create_date)
        list['newsDeleteDate'] = str(self.news_delete_date)
        list['newsDeleteId'] = self.news_delete_id
        list['newsContent'] = self.news_content
        return list

    def __str__(self):
        return '{newsId:%d,newsName:%s,newsCreateDate:%s,newsDeleteDate:%s,newsDeleteId:%d,newsContent:%s}' % (self.news_id,self.news_name,self.news_create_date,self.news_delete_date,self.news_delete_id,self.news_content)
    __repr__ = __str__