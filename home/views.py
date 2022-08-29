from django.shortcuts import redirect, render
from .forms import AddQuestionForm, UserForm
from django.views.decorators.csrf import csrf_protect
import requests
from question_api.models import Question


# Create your views here.


@csrf_protect
def home_page(request):
    context = {}
    if request.method == 'POST':
        resp = requests.post(
            'http://127.0.0.1:8000/user_api/save_user/', data=request.POST).json()
        if resp.get('success_flag'):
            context = {'success_message': resp.get('resp')}
        else:
            context = {'error_message': resp.get('resp')}
    form = UserForm()
    context.update({'form': form})
    return render(request, 'home/index.html', context)


@csrf_protect
def dashboard(request,uid=0):
    context = {}
    if request.method == 'POST':
        try:
            # data = {'email' : request.POST.get('email'), 'password': request.POST.get('password')}
            resp = requests.post(
                'http://127.0.0.1:8000/user_api/login_user/', data=request.POST).json()
        except Exception as e:
            print(request.POST)
            print('Exception occured = ', e)
            resp = {'resp': 'Exception'}

        if resp.get('logged_in'):
            uid = resp.get('user_data').get('id')
            questions = requests.get(
                f'http://127.0.0.1:8000/question_api/get_questions/', data=request.POST).json()
            context.update(resp)
            context.update(questions)
        else:
            form = UserForm()
            context = {'error_message': resp.get('resp'), 'form': form}
            return render(request, 'home/index.html', context)
    elif uid > 0:
        resp = requests.get(
            f'http://127.0.0.1:8000/user_api/get_user_info/{uid}/',data={}).json()
        questions = requests.get(
                f'http://127.0.0.1:8000/question_api/get_questions/', data=request.POST).json()
        context.update(questions)
        context.update(resp)
        total_que_added = Question.objects.filter(user=uid).count()
        context.update({'total_question_added':total_que_added})
    else:
        return redirect('/home/')
    form = AddQuestionForm()
    context.update({'form': form})
    return render(request, 'dashboard/dashboard.html', context)



