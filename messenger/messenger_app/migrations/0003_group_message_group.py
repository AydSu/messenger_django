# Generated by Django 4.0.5 on 2022-06-27 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messenger_app', '0002_alter_message_options_alter_message_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Название беседы')),
            ],
            options={
                'verbose_name': 'Беседа',
                'verbose_name_plural': 'Беседы',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='messenger_app.group'),
        ),
    ]