# Generated by Django 4.1.6 on 2023-02-09 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('noOfChapters', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('correctChoice', models.CharField(max_length=50)),
                ('wrongChoice1', models.CharField(max_length=50)),
                ('wrongChoice2', models.CharField(max_length=50)),
                ('difficulty', models.CharField(choices=[('0', 'Difficult'), ('1', 'Simple')], default='1', max_length=2)),
                ('objective', models.CharField(choices=[('0', 'Reminding'), ('1', 'Understanding'), ('2', 'Creativity')], default='0', max_length=2)),
                ('chapterNo', models.IntegerField()),
                ('courseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.course')),
            ],
        ),
    ]
