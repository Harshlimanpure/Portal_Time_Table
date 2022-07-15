from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sem8(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Program = models.CharField(max_length= 50)
    subject_code = models.CharField(max_length=50,null=True)
    subject = models.CharField(max_length=50)
    Faculty = models.CharField(max_length=50,null=True)
    time = models.TimeField(null=True)

    class Meta:
        verbose_name = 'Sem8'
        verbose_name_plural = 'Sem8'
class Sem7(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Program = models.CharField(max_length= 50)
    subject_code = models.CharField(max_length=50,null=True)
    subject = models.CharField(max_length=50)
    Faculty = models.CharField(max_length=50,null=True)
    time = models.TimeField(null=True)

    class Meta:
        verbose_name = 'Sem7'
        verbose_name_plural = 'Sem7'
class Sem6(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Program = models.CharField(max_length= 50)
    subject_code = models.CharField(max_length=50,null=True)
    subject = models.CharField(max_length=50)
    Faculty = models.CharField(max_length=50,null=True)
    time = models.TimeField(null=True)

    class Meta:
        verbose_name = 'Sem6'
        verbose_name_plural = 'Sem6'

class Sem5(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Program = models.CharField(max_length= 50)
    subject_code = models.CharField(max_length=50,null=True)
    subject = models.CharField(max_length=50)
    Faculty = models.CharField(max_length=50,null=True)
    time = models.TimeField(null=True)

    class Meta:
        verbose_name = 'Sem5'
        verbose_name_plural = 'Sem5'

class Sem4(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Program = models.CharField(max_length= 50)
    subject_code = models.CharField(max_length=50,null=True)
    subject = models.CharField(max_length=50)
    Faculty = models.CharField(max_length=50,null=True)
    time = models.TimeField(null=True)

    class Meta:
        verbose_name = 'Sem4'
        verbose_name_plural = 'Sem4'

class Sem3(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Program = models.CharField(max_length= 50)
    subject_code = models.CharField(max_length=50,null=True)
    subject = models.CharField(max_length=50)
    Faculty = models.CharField(max_length=50,null=True)
    time = models.TimeField(null=True)

    class Meta:
        verbose_name = 'Sem3'
        verbose_name_plural = 'Sem3'

class Sem2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Program = models.CharField(max_length= 50)
    subject_code = models.CharField(max_length=50,null=True)
    subject = models.CharField(max_length=50)
    Faculty = models.CharField(max_length=50,null=True)
    time = models.TimeField(null=True)

    class Meta:
        verbose_name = 'Sem2'
        verbose_name_plural = 'Sem2'

class Sem1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Program = models.CharField(max_length= 50)
    subject_code = models.CharField(max_length=50,null=True)
    subject = models.CharField(max_length=50)
    Faculty = models.CharField(max_length=50,null=True)
    time = models.TimeField(null=True)

    class Meta:
        verbose_name = 'Sem1'
        verbose_name_plural = 'Sem1'

