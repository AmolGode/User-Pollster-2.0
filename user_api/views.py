
from django.shortcuts import redirect, render
from rest_framework.views import APIView

from question_api.models import Question
from .serializers import *
from rest_framework.response import Response

# Create your views here.


class UserAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            resp = {'resp': 'User saved successfully..!', 'success_flag': True}
        else:
            resp = {'resp': serializer.errors, 'success_flag': False}
            print(serializer.errors, 'invalid data')
        return Response(resp)


class UserLogin(APIView):
    def post(self, request):
        try:
            user = User.objects.get(email=request.data.get(
                'email'), password=request.data.get('password'))
            serializer = UserLoginSerializer(user)
            total_que_added = Question.objects.filter(user=user.id).count()
            resp = {'resp': 'User logged in successfully..!',
                    'logged_in': True, 
                    'user_data': serializer.data,
                    'total_question_added':total_que_added
                    }
        except:
            resp = {'resp': 'Invalid email id or password', 'logged_in': False}
        return Response(resp)

    def get(self,request,uid):
        try:
            user = User.objects.get(id=uid)
            serializer = UserLoginSerializer(user)
            resp = {'user_data':serializer.data}
        except:
            return redirect('/home/')
        return Response(resp)