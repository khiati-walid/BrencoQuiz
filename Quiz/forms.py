from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username']



class QuestionForm(ModelForm):
    class Meta:
        model = QuesModel
        fields = ['question','category','op1','op2','op3','op4','ans']

class ResultForm(ModelForm):
    class Meta:
        model= Result
        exclude=['user']