# Generated by Django 5.1 on 2024-12-02 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture_classification', '0005_loan_data_delete_logistic_predict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_data',
            name='age',
            field=models.PositiveIntegerField(verbose_name='年齢'),
        ),
        migrations.AlterField(
            model_name='loan_data',
            name='default',
            field=models.CharField(max_length=255, verbose_name='不履行歴'),
        ),
        migrations.AlterField(
            model_name='loan_data',
            name='education',
            field=models.CharField(max_length=255, verbose_name='学歴'),
        ),
        migrations.AlterField(
            model_name='loan_data',
            name='emp_exp',
            field=models.PositiveIntegerField(verbose_name='就業年数'),
        ),
        migrations.AlterField(
            model_name='loan_data',
            name='gender',
            field=models.CharField(max_length=255, verbose_name='性別'),
        ),
        migrations.AlterField(
            model_name='loan_data',
            name='home_ownership',
            field=models.CharField(max_length=255, verbose_name='家の所有形態'),
        ),
        migrations.AlterField(
            model_name='loan_data',
            name='income',
            field=models.PositiveIntegerField(verbose_name='年収'),
        ),
        migrations.AlterField(
            model_name='loan_data',
            name='loan_amount',
            field=models.PositiveIntegerField(verbose_name='融資額'),
        ),
        migrations.AlterField(
            model_name='loan_data',
            name='loan_intent',
            field=models.CharField(max_length=255, verbose_name='利用目的'),
        ),
        migrations.AlterField(
            model_name='loan_data',
            name='loan_status',
            field=models.CharField(max_length=255, verbose_name='ローンステータス'),
        ),
    ]