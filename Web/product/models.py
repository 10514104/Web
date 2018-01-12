from django.db import models



class Product(models.Model):
    #產品資料
    name = models.CharField(max_length=128, unique=True)#產品名稱
    price = models.IntegerField()#產品價格
    title = models.CharField(max_length=128, unique=True)#產品標題
    Introduction = models.TextField()#產品簡介
    productimg = models.ImageField(height_field=500
                                   , width_field=500, max_length=100)#產品圖片
    titleimg = models.ImageField(height_field=375
                                   , width_field=372, max_length=100)#標題圖片
    #品飲紀錄
    colour = models.CharField(max_length=128, unique=True)#色澤
    smell = models.TextField()#嗅覺
    taste = models.TextField()#口感
    After = models.CharField(max_length=128, unique=True)#餘韻
    cask = models.TextField()#橡木桶資訊
    def __str__(self):
        return self.name
    
    
class Shop(models.Model):
    #購物車資料
    name = models.CharField(max_length=128, unique=True)#產品名稱
    price = models.IntegerField()#產品價格
    amount = models.IntegerField()#數量
    def __str__(self):
        return self.name
    
    
    

    
    
    
    
    
