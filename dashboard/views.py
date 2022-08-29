from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
from django.views.decorators.csrf import csrf_protect
from home.forms import UserForm, AddQuestionForm
from user_api.models import User
from user_api.serializers import UserLoginSerializer
from question_api.models import Question

# Create your views here.


@csrf_protect
def add_question(request, uid):
    context = {}
    resp = {}
    if request.method == 'POST':
        try:
            resp = requests.post(
                f'http://127.0.0.1:8000/question_api/add_question/{uid}/', data=request.POST).json()
            context = resp
        except Exception as e:
            print(resp)
            print('Exception occured = ', e)
            resp = {'resp': 'Exception'}
            form = UserForm()
            context = {'error_message': e, 'form': form}
            return render(request, 'home/index.html', context)
    form = AddQuestionForm()
    context.update({'form': form})

    questions = requests.get(
        f'http://127.0.0.1:8000/question_api/get_questions/', data=request.POST).json()
    context.update(questions)
    total_que_added = Question.objects.filter(user=uid).count()
    context.update({'total_question_added':total_que_added})
    return render(request, 'dashboard/dashboard.html', context)


@csrf_protect
def add_vote(request, uid):
    context = {}
    if request.method == 'POST':
        try:
            resp = requests.post(
                f'http://127.0.0.1:8000/question_api/add_vote/{uid}/', data=request.POST).json()
        except Exception as e:
            print('Exception occured = ', e)
            resp = {'resp': 'Please select option to add vote.' , 'success_flag' : False}

        if resp.get('success_flag'):
            context.update({'resp': 'Your vote is added successfully..!'})
        questions = requests.get(
            f'http://127.0.0.1:8000/question_api/get_questions/', data=request.POST).json()
        context.update(resp)
        context.update(questions)
    form = AddQuestionForm()
    context.update({'form': form})
    user = User.objects.get(id=uid)
    serializer = UserLoginSerializer(user)
    context.update({'user_data': serializer.data})
    total_que_added = Question.objects.filter(user=uid).count()
    context.update({'total_question_added':total_que_added})
    return render(request, 'dashboard/dashboard.html', context)


@csrf_protect
def view_profile(request, uid):
    context = {}
    try:
        user_data = requests.get(
            f'http://127.0.0.1:8000/user_api/get_user_info/{uid}/',data={}).json()
        questions = requests.get(
            f'http://127.0.0.1:8000/question_api/get_questions/{uid}/', data=request.POST).json()
        context.update(user_data)
        context.update(questions)
    except Exception as e:
        print('Exception occured = ', e)
        context = {'error_message': 'exception occured..!'}
    return render(request,'dashboard/profile.html',context)
