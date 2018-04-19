from django.db import models

# Create your models here.
class Users(models.Model):
    
#     用户的ID设置为主键
    id = models.IntegerField(primary_key = True)
    
#     用户的姓名
    userName = models.CharField(max_length = 6, blank = False)
    
#     用户的生日
    birthday = models.DateField()
    
#     用户的手机号码
    phone = models.CharField(max_length = 20, blank = False)
    
#     用户的密码
    password = models.CharField(max_length = 20, blank = False)
    
#     用户的头像暂未做
#     userImg = models.CharField()
    
#     获取该用户的所有的信息
    def getUsersAllInfo(self):
        list = {}
        list['id'] = self.id
        list['userName'] = self.userName
        list['birthday'] = self.birthday
        list['phone'] = self.phone
        list['password'] = self.password
#         list['userImg'] = self.userImg
        return list
    def __str__(self):
        return '{id:%d,userName:%s,birthday:%s,phone:%s,password:%s}' % (self.id,self.userName,self.birthday,self.phone,self.password)
    
    __repr__ = __str__