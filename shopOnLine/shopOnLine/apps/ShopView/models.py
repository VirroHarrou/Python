import datetime
from django.db import models
from django.utils import timezone

class product(models.Model):
	product_title = models.CharField('наименование товара', max_length=255)
	product_description = models.TextField('описание товара')
	product_picture = models.ImageField('картинка товара', upload_to='image/%Y-%m-%d/')
	pub_date = models.DateTimeField('Дата публикации')

	def __str__(self):
		return self.product_title
	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))
	def matches_the_request(self):
		if was_published_recently(self):
			pass 
	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'

class Comment(models.Model):
	article = models.ForeignKey(product, on_delete = models.CASCADE)
	avtor_name = models.CharField('имя автора', max_length = 70)
	comment_text_positive = models.CharField('положительные стороны', max_length = 500)
	comment_text_negative = models.CharField('недостатки', max_length = 500)
	comment_text = models.CharField('текст комментария', max_length = 500)

	def __str__(self):
		return self.avtor_name
	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'

class user(models.Model):
	name = models.CharField('Ник',max_length=50)
	password = models.CharField('Пароль',max_length=50)
	email = models.EmailField('Почта', max_length=100)
	Likes = models.ManyToManyField(product)

	def __str__(self):
		return self.name

class product_features(models.Model):
	

	def __str__(self):
		return self.Avtor_name
	class Meta:
		verbose_name = 'Описание продукта'
		verbose_name_plural = 'Описание продуктов'