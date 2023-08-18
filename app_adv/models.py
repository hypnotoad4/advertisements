from django.db import models
from django.utils.html import format_html
from django.contrib import admin

class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    auction = models.BooleanField("Торг", default=False, help_text="Выберите, будет ли торг уместен")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата изменения", auto_now=True)

    def __str__(self):
        return f"id = {self.title} | title = {self.title} | price = {self.price}"

    class Meta:
        db_table = "advertisements"
    
    @admin.display(description = "Дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color:green; font-weight: bold">Сегодня в {}</span>', created_time)
        else:
            return self.created_at.strftime("%d.%m.%Y %H:%M:%S")