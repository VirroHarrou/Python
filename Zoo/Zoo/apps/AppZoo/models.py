from django.db import models

class Animal(models.Model):

    animal_name = models.CharField('Имя животного', max_length=200)
    animal_description = models.TextField('Описание животного', max_length=2000)
    animal_features = models.TextField('Особенности животного', max_length=2000)
    animal_habitat = models.TextField('Места обитания животного', max_length=1500)
    animal_intresting = models.TextField('Интересные факты о животном', max_length=1500)
    animal_photo = models.ImageField('Фото животного', upload_to='image/%d-%m-%Y/')

    class Meta:
        verbose_name = ("Animal")
        verbose_name_plural = ("Animals")

    def __str__(self):
        return self.animal_name

    # def get_absolute_url(self):
    #     return reverse("Animal_detail", kwargs={"pk": self.pk})