# Generated by Django 2.2.6 on 2019-12-09 03:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Kwitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_input', models.CharField(max_length=250)),
                ('post_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes', models.ManyToManyField(related_name='likes', to='Kwitter.KwitterUser')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Kwitter.KwitterUser')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seen', models.BooleanField(default=False)),
                ('kweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_kweet', to='Kwitter.Kweet')),
                ('kwitter_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_user', to='Kwitter.KwitterUser')),
            ],
        ),
    ]
