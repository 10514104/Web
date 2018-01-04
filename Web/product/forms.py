from django import forms
from product.models import Product,Shop


class ProductForm(forms.ModelForm):
    name = forms.CharField(label='標題')
    price = forms.IntegerField(label='價格')
    title = forms.CharField(label='產品標題',widget=forms.Textarea)#產品標題
    Introduction = forms.CharField(label='產品簡介',widget=forms.Textarea)#產品簡介
    #品飲紀錄
    colour = forms.CharField(label='色澤',widget=forms.Textarea)#色澤
    smell = forms.CharField(label='嗅覺',widget=forms.Textarea)#嗅覺
    taste = forms.CharField(label='口感',widget=forms.Textarea)#口感
    After = forms.CharField(label='餘韻',widget=forms.Textarea)#餘韻
    cask = forms.CharField(label='橡木桶資訊',widget=forms.Textarea)#橡木桶資訊
    class Meta:
        model = Product
        fields = ['name', 'price','title', 'Introduction',
                  'colour', 'price','smell', 'taste','After', 'cask']
        
        
        
class ShopForm(forms.ModelForm):
    amount = forms.IntegerField(label='數量')
    name = forms.CharField(label='標題')
    price = forms.IntegerField(label='價格')
    class Meta:
        model = Shop
        fields = ['amount','name','price']




        