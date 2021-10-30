from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.name

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(null=True,default=0)
    wrong = models.FloatField(null=True,default=0)
    correct = models.FloatField(null=True,default=0)
    total = models.FloatField(null=True,default=0)
    percent = models.FloatField(null=True,default=0)

    def __str__(self):
        return f"user:{self.user}, id:{self.pk} "

    def get_questions(self):
        return self.questions.all()

class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='questions',null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question



#class Answer(models.Model):
#    text = models.CharField(max_length=200)
#    correct = models.BooleanField(default=False)
#    question = models.ForeignKey(QuesModel, on_delete=models.CASCADE, related_name='answers')

#    def __str__(self):
#        return f"question: {self.question.question}, answer: {self.text}," \
#               f" correct: {self.correct}"

