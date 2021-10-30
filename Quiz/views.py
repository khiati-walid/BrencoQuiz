from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from .filters import QuestionFilter
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    if request.method == 'POST':
        questions=QuesModel.objects.all()

        score= 0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        Result.objects.create(
            user = request.user,
            score = score,
            correct = correct,
            wrong = wrong,
            percent = percent,
            total = total
        )
        return render(request,'Quiz/result.html',context)
    else:
        questions=QuesModel.objects.all()
        category = Category.objects.all()
        context = {
            'questions':questions,
            'category':category
        }

        context['filter'] = QuestionFilter(request.GET,
                                           queryset= QuesModel.objects.all())
        return render(request,'Quiz/home.html',context)


def addQuestion(request):
    categories= Category.objects.all()
    if request.user.is_staff:
        form=QuestionForm()
        if(request.method=='POST'):
            form=QuestionForm(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('addQuestion')
            else:
                print('balabalajpdojd')
        context={
            'form':form,
            'categories':categories
        }
        return render(request,'Quiz/addQuestion.html',context)
    else: 
        return redirect('home') 


def question(request):
    question = QuesModel.objects.all()
    return render(request,'Quiz/questions.html',{'question':question})

def update(request, id):
    question = QuesModel.objects.get(id=id)
    category = Category.objects.all()
    form = QuestionForm(request.POST, instance=question)
    if form.is_valid():
        form.save()
        return redirect('questions')
    context={
        'question':question,
        'category':category
    }
    return render(request,'Quiz/updateQuestion.html',context)

def delete(request, id):
    form = QuesModel.objects.get(id=id)
    form.delete()
    return redirect('questions')


def showResult(request):
    if request.user.is_staff:
        result = Result.objects.all()
        return render(request, 'Quiz/showresult.html', {'result': result})
    else:
        return redirect('home')


def deleteresult(request, id):
    form = Result.objects.get(id=id)
    form.delete()
    return redirect('showresult')



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=createuserform()
        if request.method=='POST':
            form=createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'Quiz/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'Quiz/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/')

