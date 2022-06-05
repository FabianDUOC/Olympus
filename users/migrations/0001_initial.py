# Generated by Django 4.0.4 on 2022-06-04 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.AutoField(primary_key=True, serialize=False, verbose_name='Código de la Región')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de la Región')),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idComuna', models.AutoField(primary_key=True, serialize=False, verbose_name='Código de la Comuna')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de la Comuna')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.region', verbose_name='Region de pertenencia')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidoPa', models.CharField(max_length=100)),
                ('apellidoMa', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('foto', models.ImageField(default='users/default.png', upload_to='users/', verbose_name='foto de perfil')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
