from django.db import models


class Planet(models.Model):
    """Планета"""
    name = models.CharField(max_length=100, default='', verbose_name='Название')

    class Meta:
        verbose_name = 'Планета'
        verbose_name_plural = 'Планеты'

    def __str__(self):
        return self.name


class Jedi(models.Model):
    """Джедай"""
    name = models.CharField(max_length=100, default='', verbose_name='Имя')
    planet = models.ForeignKey(Planet, on_delete=models.SET_NULL, null=True, verbose_name='Планета')

    class Meta:
        verbose_name = 'Джедай'
        verbose_name_plural = 'Джедаи'

    def __str__(self):
        return self.name

    # def add_padawan(self, candidate):
    #     candidate.jedi = self
    #     candidate.save()
    #     candidate.make_padawan()


class Candidate(models.Model):
    """ Кандидат """
    name = models.CharField(max_length=80)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()
    jedi = models.ForeignKey(Jedi, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'


class Questions(models.Model):
    """ Модель для вопросов """
    content = models.CharField(max_length=240)
    right_answer = models.BooleanField()

    def __str__(self):
        return self.content[:50]

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class PadawanTest(models.Model):
    """ Модель тестового испытания падавана """
    planet = models.OneToOneField(Planet, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Questions)

    def __str__(self):
        return "{} order challenge".format(self.planet)


class Answers(models.Model):
    """ Модель для ответов """
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    content = models.BooleanField()
