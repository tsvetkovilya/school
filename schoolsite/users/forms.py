from django import forms
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from school.models import CustomUser
from users.models import Attendance_of_classes, Lesson


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=100,
        required = True,
        help_text='Email',
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email', 'id':'InputEmail', 'style':'height: 55px'}),
    )
    phone_number = forms.CharField(
        max_length=100,
        required=True,
        help_text='Имя',
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Номер', 'id': 'InputNumber', 'style': 'height: 55px'}),
    )
    wishes = forms.CharField(
        max_length=300,
        required=True,
        help_text='Имя',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваши пожелания к обучению', 'id': 'InputWishes', 'style': 'height: 100px;'}),
    )
    first_name = forms.CharField(
        max_length=100,
        required = True,
        help_text='Имя',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Имя', 'id':'InputFirstName', 'style':'height: 55px'}),
    )
    last_name = forms.CharField(
        max_length=100,
        required = True,
        help_text='Фамилия',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Фамилия', 'id':'InputLastName', 'style':'height: 55px'}),
    )
    username = forms.CharField(
        max_length=200,
        required = True,
        help_text='Никнейм',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Никнейм', 'id':'InputUsername', 'style':'height: 55px'}),
    )
    password1 = forms.CharField(
        help_text='Пароль',
        required = True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Пароль', 'id':'InputPassword1', 'style':'height: 55px'}),
    )
    password2 = forms.CharField(
        required = True,
        help_text='Повторите пароль',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Повторите пароль', 'id':'InputPassword2', 'style':'height: 55px'}),
    )
    labels = {
        'grade': 'Выбор'
    }
    grade = forms.ChoiceField(
        choices=CustomUser.grade_number,
        widget=forms.Select(
            attrs={'class': 'form-select', 'id':'InputGrade'}),
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2', 'wishes', 'phone_number', 'grade']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Никнейм', 'id':'InputUsername', 'style':'height: 55px'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Пароль', 'id':'InputPassword', 'style':'height: 55px'}))

class AttendanceOfClassesAdminForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='слушатели'
    )

    class Meta:
        model = Attendance_of_classes
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['students'].initial = self.instance.students.all()

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        if instance.pk:
            instance.students.set(self.cleaned_data['students'])
            self.save_m2m()
        return instance

class LessonAdminForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='слушатели'
    )

    class Meta:
        model = Lesson
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['students'].initial = self.instance.students.all()

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        if instance.pk:
            instance.students.set(self.cleaned_data['students'])
            self.save_m2m()
        return instance

@admin.register(Attendance_of_classes)
class AttendanceOfClassesAdmin(admin.ModelAdmin):
    filter_horizontal  = ('students',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    filter_horizontal  = ('students',)