# Generated by Django 4.2 on 2023-05-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationConnectionDtls',
            fields=[
                ('DestId', models.AutoField(primary_key=True, serialize=False)),
                ('DestType', models.CharField(max_length=50)),
                ('DestNm', models.CharField(max_length=100)),
                ('DestUname', models.CharField(max_length=100)),
                ('DestPwd', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SourceConnectionDtls',
            fields=[
                ('SrcId', models.AutoField(primary_key=True, serialize=False)),
                ('SrcType', models.CharField(max_length=50)),
                ('SrcNm', models.CharField(max_length=100)),
                ('BigQueryProjectId', models.CharField(max_length=100)),
                ('BigQueryServiceAccountKeyFileLocation', models.CharField(max_length=500)),
            ],
        ),
    ]
