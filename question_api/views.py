import pytz
from rest_framework.views import APIView
from rest_framework.response import Response
from user_api.models import User
from user_api.serializers import UserLoginSerializer
from .serializers import QuestionSerializer
from .models import Question
from datetime import datetime, timedelta
from django.utils.timezone import now, localtime
from django.utils import timezone
# Create your views here.


class QuestionAPI(APIView):
    def post(self, request, uid):
        request.data._mutable = True
        request.data['user'] = uid
        serializer = QuestionSerializer(data=request.data)
        user = User.objects.get(id=uid)
        # print('user == ', user, user.total_question_added)
        total_question_added = Question.objects.filter(user=uid).count()
        if total_question_added < 5:
            if serializer.is_valid():
                serializer.save()
                user.total_question_added += 1
                user.save()
                # que = Question.objects.last()

                # expiry_time = que.date_time + timedelta(hours=24)
                # print('Expiry time = ', expiry_time)
                # Question.objects.select_for_update().filter(
                #     id=que.id).update(date_time=expiry_time)

                resp = {'resp': 'Question Added Successfully..!.',
                        'success_flag': True
                        }
            else:
                resp = {'resp': 'Invalid data.', 'success_flag': False}
                print('Serializer error = ', serializer.errors)
        else:
            resp = {'resp': 'You can only add at most 5 questions.',
                    'success_flag': False}
            print('Quetion limit exceeded.')
        serializer = UserLoginSerializer(user)
        resp.update({'user_data': serializer.data})
        return Response(resp)

    def delete(self, request):
        # User.objects.filter(question__date_time__lte=now().today()
        #                     .strftime('%Y-%m-%d %H:%M')).update(total_question_added=0)

        # count, _ = Question.objects.filter(
        #     date_time__lte=datetime.now(timezone.utc)
        # ).delete()
        last_24h = now() - timedelta(hours=24)
        count, _ = Question.objects.filter(date_time__lte=last_24h).delete()
        resp = {'Total question deleted': count}
        print(resp)
        return Response(resp)

    def get(self, request):
        questions = Question.objects.all().order_by('-id')
        serializer = QuestionSerializer(questions, many=True)
        resp = {'questions': serializer.data}
        return Response(resp)


class UserQuestion(APIView):
    def get(self, request, uid):
        questions = Question.objects.filter(user_id=uid).order_by('-id')
        serializer = QuestionSerializer(questions, many=True)
        resp = {'questions': serializer.data}
        return Response(resp)


class AddVote(APIView):
    def post(self, request, uid):
        attribute_name = request.data['attribute_name']
        question_id = request.data['question_id']
        que = Question.objects.get(id=question_id)
        if attribute_name == 'option1_vote':
            que.option1_vote += 1
        elif attribute_name == 'option2_vote':
            que.option2_vote += 1
        elif attribute_name == 'option3_vote':
            que.option3_vote += 1
        elif attribute_name == 'option4_vote':
            que.option4_vote += 1
        que.save()
        resp = {'resp': 'Vote added successfully..!'}
        return Response(resp)
