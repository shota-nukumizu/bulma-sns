# Generated by Django 3.2.9 on 2021-12-08 10:56

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('title', models.CharField(choices=[('danger', '重要'), ('warning', '連絡'), ('info', 'イベント'), ('success', 'その他')], max_length=100)),
                ('content', mdeditor.fields.MDTextField()),
                ('created_at', models.DateField(auto_now=True, verbose_name='作成日')),
            ],
        ),
    ]
