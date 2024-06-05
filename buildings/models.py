from django.db import models


class Ladder(models.Model):
    serial_number = models.CharField(max_length=30, verbose_name="Модель", unique=True)
    length = models.IntegerField(verbose_name="Длина")
    width = models.IntegerField(verbose_name="Ширина")
    height = models.IntegerField(verbose_name="Высота")

    def __str__(self) -> str:
        return f"{self.serial_number}"

    class Meta:
        verbose_name = "Лестница"
        verbose_name_plural = "Лестницы"
        ordering = "serial_number"


class Plate(models.Model):
    serial_number = models.CharField(max_length=30, verbose_name="Модель", unique=True)
    length = models.IntegerField(verbose_name="Длина")
    width = models.IntegerField(verbose_name="Ширина")
    height = models.IntegerField(verbose_name="Высота")

    def __str__(self) -> str:
        return f"{self.serial_number}"

    class Meta:
        verbose_name = "Плита"
        verbose_name_plural = "Плиты"
        ordering = "serial_number"


class Pillar(models.Model):
    serial_number = models.CharField(max_length=30, verbose_name="Модель", unique=True)
    length = models.IntegerField(verbose_name="Длина")
    width = models.IntegerField(verbose_name="Ширина")
    height = models.IntegerField(verbose_name="Высота")

    def __str__(self) -> str:
        return f"{self.serial_number}"

    class Meta:
        verbose_name = "Колонна"
        verbose_name_plural = "Колонны"
        ordering = "serial_number"


class Building(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name="Наименование")
    industrial = models.BooleanField(default=False, verbose_name="Промышленное")
    pillar = models.ForeignKey(Pillar, on_delete=models.CASCADE, verbose_name="Колонна")
    pillars_count = models.IntegerField(verbose_name="Кол-во колонн")
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE, verbose_name="Плита")
    plates_count = models.IntegerField(verbose_name="Кол-во плит")
    ladder = models.ForeignKey(
        Ladder, on_delete=models.CASCADE, verbose_name="Лестница"
    )
    ladders_count = models.IntegerField(verbose_name="Кол-во лестниц")
    length = models.IntegerField(verbose_name="Длина")
    width = models.IntegerField(verbose_name="Ширина")
    height = models.IntegerField(verbose_name="Высота")
    floors = models.IntegerField(verbose_name="Этажей")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Здание"
        verbose_name_plural = "Здания"
        ordering = "name"
