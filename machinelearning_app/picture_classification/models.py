from django.db import models

class Sex(models.IntegerChoices):
  male = 0
  female = 1

class Education(models.IntegerChoices):
  high_school = 0
  college = 1
  graduate_school = 2

class Occupation(models.IntegerChoices):
  government_worker = 0
  private_sector = 1
  unemployed = 2

class Loan_History(models.IntegerChoices):
  yes = 0
  no = 1

class Logistic_Predict(models.Model):
  name = models.CharField(default='氏名', max_length=255, verbose_name='氏名')
  age = models.PositiveIntegerField(default=0, verbose_name='年齢')
  sex = models.IntegerField(default=0, choices=Sex, verbose_name='性別')
  education = models.IntegerField(default=0, choices=Education, verbose_name='学歴')
  occupation = models.IntegerField(default=0, choices=Occupation, verbose_name='職業')
  income = models.PositiveIntegerField(default=0, verbose_name='年収')
  loan = models.PositiveIntegerField(default=0, verbose_name='借入額')
  loan_history = models.IntegerField(default=0, choices=Loan_History, verbose_name='過去の借入')
  default_pred = models.IntegerField(default=0, verbose_name='デフォルトリスク')

  def __str__(self):
        return str(self.name)