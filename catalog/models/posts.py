# from django.db import models
#
# NULLABLE = {'blank':True, 'null': True}
#
#
# class Owner(models.Model):
#     pass
#
#
# class Comment(models.Model):
#     title = models.CharField(max_length=50, verbose_name='название')
#     slug = models.CharField(max_length=200, unique=True, verbose_name='URL')
#     description = models.TextField(verbose_name='Описание')
#     image = models.ImageField(upload_to='images/', verbose_name='Изображение', **NULLABLE)
#     create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
#     is_published = models.BooleanField(default=False)
#     views_count = models.IntegerField(default=0)
#
#     def __str__(self):
#         return f"{self.title}"
#
#     def Meta:
#         verbose_name = 'комментарий'
#         verbose_name_plural = 'комментарии'
