from django import forms
from user_api.models import User 
from question_api.models import Question


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name','last_name','phone','email','password']


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text','option1','option2','option3','option4']