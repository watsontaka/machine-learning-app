from django.db import models

class Loan_Data(models.Model):
  name = models.CharField(default='氏名', max_length=255, verbose_name='氏名')
  age = models.PositiveIntegerField(verbose_name='年齢')
  gender = models.CharField(max_length=255, verbose_name='性別')
  education = models.CharField(max_length=255,verbose_name='学歴')
  income = models.PositiveIntegerField(verbose_name='年収')
  emp_exp = models.PositiveIntegerField(verbose_name='就業年数')
  loan_amount = models.PositiveIntegerField(verbose_name='融資額')
  home_ownership = models.CharField(max_length=255, verbose_name='家の所有形態')
  loan_intent = models.CharField(max_length=255, verbose_name='利用目的')
  default = models.CharField(max_length=255, verbose_name='不履行歴')
  loan_status = models.CharField(max_length=255, verbose_name='ローンステータス')

  def __str__(self):
        return str(self.name)