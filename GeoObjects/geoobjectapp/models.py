from django.contrib.auth.models import User
from django.db import models
from servis import get_path_upload_photos


class GeoObjectCoords(models.Model):
    latitude = models.FloatField(verbose_name='широта', blank=True, null=True)
    longitude = models.FloatField(verbose_name='долгота', blank=True, null=True)
    height = models.FloatField(verbose_name='высота', blank=True, null=True)

    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'

    class Meta:
        verbose_name = "Координата"
        verbose_name_plural = "Координаты"

class GeoObjectLevel(models.Model):
    winter = models.CharField(max_length=64, verbose_name='зимой', blank=True, null=True)
    spring = models.CharField(max_length=64, verbose_name='весной', blank=True, null=True)
    summer = models.CharField(max_length=64, verbose_name='летом', blank=True, null=True)
    autumn = models.CharField(max_length=64, verbose_name='осенью', blank=True, null=True)

    def __str__(self):
        return f'{self.winter} {self.spring} {self.summer} {self.autumn}'

    class Meta:
        verbose_name = "Уровень сложности"
        verbose_name_plural = "Уровни сложности"

class GeoObject(models.Model):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'
    STATUS = [
        (new, "новый"),
        (pending, "на рассмотрении"),
        (accepted, "проверка состоялась"),
        (rejected, "проверка состоялась, но информация не принята"),
    ]

    title_object = models.CharField(max_length=128, verbose_name='Название объекта')
    coords_object = models.ForeignKey(GeoObjectCoords, on_delete=models.CASCADE)
    level_object = models.ForeignKey(GeoObjectLevel, on_delete=models.CASCADE, blank=True, null=True)
    date_add_object = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    connect = models.TextField(blank=True, null=True)

    status = models.CharField(max_length=16, choices=STATUS, default=new)

    def __str__(self):
        return f'{self.pk} {self.title_object}'

    class Meta:
        verbose_name = "географический объект"
        verbose_name_plural = "географические объекты"

class GeoObjectImage(models.Model):
    image_object = models.ForeignKey(GeoObject, on_delete=models.CASCADE, related_name='image',
                                     blank=True, null=True)
    data_image_object = models.ImageField(upload_to=get_path_upload_photos,
                                          verbose_name='изображение', blank=True, null=True)
    title_object = models.CharField(max_length=64, verbose_name='название', blank=True, null=True)
    date_create_object = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk} {self.title_object}'

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
