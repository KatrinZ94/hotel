from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    number_of_room = models.SmallIntegerField(
        unique=True,
        db_index=True,
        verbose_name="номер комнаты",
        help_text="первая цифра указывает на этаж"
    )

    choices_of_number_of_sleep_place = (
        ('2', 'двухместный'),
        ('3', 'трёхместный'),
        ('4', 'четырехместный')
    )
    number_of_sleep_place = models.CharField(
        max_length=3,
        verbose_name="количество спальных мест",
        choices=choices_of_number_of_sleep_place
    )

    choices_window_view = (
        ('sea', 'вид на море'),
        ('mountains', 'вид на горы'),
        ('town', 'вид на город')
    )

    window_view = models.CharField(
        max_length=128,
        verbose_name="описание вида из окна",
        choices=choices_window_view
    )
    air_conditioning = models.BooleanField(verbose_name="есть кондиционер?")
    refrigerator = models.BooleanField(verbose_name="есть холодильник?")
    balcony = models.BooleanField(verbose_name="есть балкон?")
    likes = models.ManyToManyField(User, related_name='liked_books')

    def __str__(self):
        return str(self.number_of_room)
