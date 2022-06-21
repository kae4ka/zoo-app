from django.db import models

class Animals(models.Model):
    animal_id = models.AutoField(primary_key=True)
    animal_name = models.CharField(max_length=20)
    animal_species = models.CharField(max_length=20)
    animal_sex = models.CharField(max_length=20)
    animal_date_of_birth = models.DateField(blank=True, null=True)
    animal_weight = models.FloatField(blank=True, null=True)
    animal_height = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animals'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CageAnimals(models.Model):
    cage_animals_id = models.AutoField(primary_key=True)
    cage_id = models.IntegerField(blank=True, null=True)
    animal_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cage_animals'


class Cages(models.Model):
    cage_id = models.AutoField(primary_key=True)
    cage_name = models.CharField(max_length=20)
    cage_type = models.CharField(max_length=20, blank=True, null=True)
    cage_square = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cages'

class FeedingSchedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    animal = models.ForeignKey(Animals, models.DO_NOTHING)
    time_of_day = models.CharField(max_length=20, blank=True, null=True)
    food = models.CharField(max_length=20)
    amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feeding_schedule'

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
