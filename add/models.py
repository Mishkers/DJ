from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

# Заголовок
# Цена
# Описание
# Дата создания
# Дата обновления
# Возможен ли торг


User = get_user_model()


class Advert(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Полбзователь', on_delete=models.CASCADE)
    image = models.ImageField("Изображения", upload_to='adverts/')


    def date_of_creation(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    def __str__(self):
        return f"{self.title}, {self.price}"

    @admin.display(description='Фото')
    def get_image(self):
        return format_html('<img src = "{url}" style="max-width: 100px"; max-height: 100px; ">', url=self.image.url)
