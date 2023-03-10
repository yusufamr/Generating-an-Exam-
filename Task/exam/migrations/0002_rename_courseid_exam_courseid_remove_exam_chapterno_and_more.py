# Generated by Django 4.1.6 on 2023-02-13 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='courseID',
            new_name='CourseID',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='chapterNo',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='correctChoice',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='objective',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='question',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='wrongChoice1',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='wrongChoice2',
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.CreateModel(
            name='Question',
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
