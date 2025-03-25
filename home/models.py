from django.db import models
from django.utils import timezone


class GlazingFrameless(models.Model):
    """
    Модель для хранения информации о безрамном остеклении.

    Содержит основные характеристики остекления, такие как название,
    описание, изображение и текстовый контент.

    Также фиксируется дата создания записи.
    """

    class Meta:
        db_table = 'glazing_frameless'
        verbose_name = 'Безрамное остекление'
        verbose_name_plural = verbose_name

    # **

    image_name = models.CharField(max_length=100, verbose_name='основная картинка', default='none.jpg')
    image_additional_1 = models.CharField(max_length=100, verbose_name='доп картинка №1', default='none.jpg')
    image_additional_2 = models.CharField(max_length=100, verbose_name='доп картинка №2', default='none.jpg')
    image_additional_3 = models.CharField(max_length=100, verbose_name='доп картинка №3', default='none.jpg')

    title = models.CharField(max_length=70, verbose_name='заголовок')
    description = models.CharField(max_length=250, verbose_name='описание', default='')
    text = models.TextField(verbose_name='описание')

    created_timestamp = models.DateTimeField(default=timezone.now, editable=False, verbose_name='дата создания')

    def __str__(self):
        return 'id: {} | {}'.format(
            self.id,
            self.title
        )


class GlazingAdvantage(models.Model):
    """
    Модель для хранения информации о преимуществах безрамного остекления.

    Каждое преимущество связано с конкретным объектом остекления
    (GlazingFrameless), имеет название и описание.

    Также фиксируется дата создания записи.

    related_name='glazing_advantage' - для связи в glazing_frameless_detail.html
    """

    class Meta:
        db_table = 'glazing_advantage'
        verbose_name = 'Безрамное остекление - преимущества'
        verbose_name_plural = 'Безрамные остекления - преимущества'

    # **

    glazing = models.ForeignKey(GlazingFrameless, on_delete=models.CASCADE, related_name='glazing_advantage')
    title = models.CharField(max_length=70, verbose_name='преимущество')
    description = models.CharField(max_length=250, verbose_name='описание')

    created_timestamp = models.DateTimeField(default=timezone.now, editable=False, verbose_name='дата создания')

    # см. admin.py
    # def __str__(self):
    #     return f'id: {self.id} -> {self.glazing} | {self.title}'


# **


class GlazingType(models.Model):
    """
    Модель для хранения информации о типе остекления.

    Содержит заголовок, изображение, описание, видеофайл и JSON-словарь
    характеристик.
    """

    class Meta:
        db_table = 'glazing_type'
        verbose_name = 'Тип остекления'
        verbose_name_plural = 'Типы остеклений'

    # **

    title = models.CharField(max_length=70, verbose_name='заголовок')
    image_name = models.CharField(max_length=100, verbose_name='изображение', default='none.jpg')
    description = models.TextField(verbose_name='описание')

    video_name = models.CharField(max_length=100, verbose_name='видео', default='none.mp4')
    characteristics = models.JSONField(default=dict, verbose_name='характеристики')

    created_timestamp = models.DateTimeField(default=timezone.now, editable=False, verbose_name='дата создания')

    def __str__(self):
        return 'id: {} | {}'.format(
            self.id,
            self.title
        )


class GlazingTypeMovement(models.Model):
    """
    Модель для хранения вариантов перемещения панели.

    Связана с конкретным типом остекления, имеет заголовок и изображение.

    Каждое поле типа перемещения связано с конкретным объектом типа остекления
    (GlazingType), имеет название и картинку.

    Также фиксируется дата создания записи.

    related_name='glazing_type_movement - для связи в ?.html
    """

    class Meta:
        db_table = 'glazing_type_properties'
        verbose_name = 'Тип остекления - вариант перемещения панели'
        verbose_name_plural = 'Типы остеклений - варианты перемещения панелей'

    # **

    glazing_type = models.ForeignKey(GlazingType, on_delete=models.CASCADE, related_name='glazing_type_movement')

    title = models.CharField(max_length=200, verbose_name='заголовок')
    image_name = models.CharField(max_length=100, verbose_name='изображение', default='none.jpg')

    created_timestamp = models.DateTimeField(default=timezone.now, editable=False, verbose_name='дата создания')

    def __str__(self):
        return f'id: {self.id} -> {self.glazing_type.title} | {self.title[:50]}...'
