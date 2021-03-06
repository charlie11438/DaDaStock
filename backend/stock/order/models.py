from django.db import models
from stockinf.models import Stockinf
from users.models import User
from django.utils import timezone

# Create your models here.
class Order(models.Model):
	id = models.AutoField(primary_key = True)
	orderno = models.CharField(max_length = 255,verbose_name = "委託單號")
	stockno = models.CharField(max_length = 255,verbose_name = "股票代號")
	stockinf = models.ForeignKey(Stockinf,on_delete = models.CASCADE,to_field="id")
	user = models.ForeignKey(User,on_delete = models.CASCADE,to_field="id")
	amount = models.IntegerField(verbose_name = "成交數量")
	orderType = models.CharField(max_length = 24,verbose_name = "成交種類")
	price = models.FloatField(verbose_name = "成交價")
	state = models.CharField(max_length = 255,verbose_name = "委託單狀態")
	date = models.DateTimeField(default=timezone.now,verbose_name = "委託時間")
	tradeCategory = models.CharField(max_length = 255,verbose_name = "交易種類",default="null")
	tradeType = models.CharField(max_length = 255,verbose_name = "交易類別",default="null")
	takeprice = models.CharField(max_length = 255,verbose_name = "取價類別",default="null")
	pendingType = models.CharField(max_length = 128,verbose_name = "掛單類別",default="null")

	class Meta:
		db_table = "stockorder"
