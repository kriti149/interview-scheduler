# Generated by Django 3.1 on 2020-08-22 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling_interview', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interviewcreation',
            old_name='email',
            new_name='interviewee_email',
        ),
        migrations.RemoveField(
            model_name='interviewcreation',
            name='participation',
        ),
        migrations.RemoveField(
            model_name='interviewee',
            name='participation',
        ),
        migrations.RemoveField(
            model_name='interviewer',
            name='participation',
        ),
        migrations.AddField(
            model_name='interviewcreation',
            name='interviewer_email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='interviewee',
            name='interview_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling_interview.interviewcreation'),
        ),
        migrations.AlterField(
            model_name='interviewer',
            name='interview_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling_interview.interviewcreation'),
        ),
        migrations.DeleteModel(
            name='InterviewDetail',
        ),
    ]
