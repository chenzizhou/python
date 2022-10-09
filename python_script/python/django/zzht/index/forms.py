from tkinter import PhotoImage, Widget
from django import forms
from .models import employee
# class  EmployeeForm(forms.Form):
#     name=forms.CharField(label='姓名',widget=forms.TextInput(
#         attrs={
#             'placeholder':'请输入姓名',
#         }
#     ))
#     age=forms.IntegerField(label='年龄')
#     job=forms.CharField(label='工作')
#     sal=forms.FloatField(label='薪水')
#     address=forms.CharField(label='地址')
#     photo=forms.ImageField(label='照片')
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'
        labels={
            'name':'姓名',
            'age':'年龄',
            'job':'工作',
            'sal':'薪水',
            'address':'地址',
            'photo':'照片',
        }
        widgets={
            'name':forms.TextInput(
                attrs={
                    'placeholder':'请输入姓名',
                }
            )
        }