# Generated by Django 4.0.4 on 2022-08-11 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LsApp', '0003_alter_commentreply_comment_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentreply',
            name='comment_reply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LsApp.comment'),
        ),
    ]
