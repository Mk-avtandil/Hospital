from django.db import models
from django.forms import CharField, DecimalField, IntegerField


class Hospital(models.Model):
    okpo = models.CharField(max_length=4, db_index=True, verbose_name='ОКПО', unique=True)
    CHOICES = (
    ('Чуй', 'Чуй'),
    ('Иссык-Куль', 'Иссык-Куль'),
    ('Нарын', 'Нарын'),
    ('Талас', 'Талас'),
    ('Ош', 'Ош'),
    ('Жалал-Абад', 'Жалал-Абад'),
    ('Баткен', 'Баткен'))
    choice = models.CharField(max_length=255, choices=CHOICES)
    max_person = models.DecimalField(max_digits=2, decimal_places=0)
    CHOICE_HOSPITAL = (
        ('Государственная', 'Государственная'),
        ('Частная', 'Частная'))
    type_of_hospital = models.CharField(max_length=255, choices=CHOICE_HOSPITAL)
    main_doctor = models.OneToOneField('MainDoctor', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.okpo} {self.choice}'


class MainDoctor(models.Model):
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    pin_passport = models.IntegerField(verbose_name='ПИН КОД паспорта')
    age = models.IntegerField(verbose_name='Возраст')
    skill = models.CharField(max_length=255, verbose_name='Опыт работы')
    number = models.IntegerField(verbose_name='Номер телефона')
    image = models.FileField(upload_to='media/%Y/%m/%d')
    treat_doctor = models.ForeignKey('TreatDoctor', on_delete=models.CASCADE)
    nurse = models.ForeignKey('Nurse', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fio}'


class TreatDoctor(models.Model):
    CHOICES = (('Терапевт', 'Терапевт'), ('Хирург', 'Хирург'))
    choice = models.CharField(max_length=255, choices=CHOICES)
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    pin_passport = models.IntegerField(verbose_name='ПИН КОД паспорта')
    age = models.IntegerField(verbose_name='Возраст')
    skill = models.CharField(max_length=255, verbose_name='Опыт работы')
    number = models.IntegerField(verbose_name='Номер телефона')
    nurse = models.OneToOneField('Nurse', auto_created=True, on_delete=models.CASCADE)
    patient = models.ManyToManyField('Patient')
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fio}'


class Nurse(models.Model):
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    pin_passport = models.IntegerField(verbose_name='ПИН КОД паспорта')
    age = models.IntegerField(verbose_name='Возраст')
    number = models.IntegerField(verbose_name='Номер телефона')
    patient = models.ManyToManyField('Patient')

    def __str__(self):
        return f'{self.fio}'


class Patient(models.Model):
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    pin_passport = models.IntegerField(verbose_name='ПИН КОД паспорта')
    age = models.IntegerField(verbose_name='Возраст')
    number = models.IntegerField(verbose_name='Номер телефона')
    problem = models.TextField(verbose_name='Причина обращения в больницу')

    def __str__(self):
        return f'{self.fio}'