# Generated by Django 2.1.5 on 2019-02-10 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('age', models.PositiveSmallIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Кандидат',
                'verbose_name_plural': 'Кандидаты',
            },
        ),
        migrations.CreateModel(
            name='Jedi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Джедай',
                'verbose_name_plural': 'Джедаи',
            },
        ),
        migrations.CreateModel(
            name='PadawanTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Планета',
                'verbose_name_plural': 'Планеты',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=240)),
                ('right_answer', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.AddField(
            model_name='padawantest',
            name='planet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jedi_manager.Planet'),
        ),
        migrations.AddField(
            model_name='padawantest',
            name='questions',
            field=models.ManyToManyField(to='jedi_manager.Questions'),
        ),
        migrations.AddField(
            model_name='jedi',
            name='planet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jedi_manager.Planet', verbose_name='Планета'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='jedi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jedi_manager.Jedi'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedi_manager.Planet'),
        ),
        migrations.AddField(
            model_name='answers',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedi_manager.Candidate'),
        ),
        migrations.AddField(
            model_name='answers',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedi_manager.Questions'),
        ),
    ]