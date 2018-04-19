from django.db import models
#首页显示
# Create your models here.
class Icon(models.Model):
#     主题的ID
    iconId = models.IntegerField()
#     主题名
    iconName = models.CharField(max_length = 6)
#     该主题用于哪个页面
    iconImage = models.CharField(max_length = 200)
    
#     def __init__(self,iconId,iconName,iconPage):
#         self.iconId = iconId
#         self.iconName = iconName
#         self.iconPage = iconPage
        
    def getIconList(self):
        list = {}
        list['id'] = self.id
        list['iconId'] = self.iconId
        list['title'] = self.iconName
        list['icon'] = self.iconImage
        return list
        
    def __str__(self):
        return '{id:%d,iconId:%d,iconName:%s,iconImage:%s}' % (self.id,self.iconId,self.iconName,self.iconImage)
     
    __repr__ = __str__
        

#     保存页面的信息
#     def saveIcon(self,iconId,iconName,iconPage):
#         print('------')
#         self.iconId = iconId
#         self.iconName = iconName
#         self.iconPage = iconPage
#         test1 = Icon(iconId = self.iconId, iconName = self.iconName, iconPage = self.iconPage)
#         test1.save()
