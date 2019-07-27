from django import forms # django 기본 기능임. import
from .models import Blog # Blog 모델 가져옴

                                    # 모델 기반 아닐시 Form
class BlogPost(forms.ModelForm):    #모델을 기반으로 한 입력공간
    class Meta:     # 메타클래스로 선언
        model = Blog # 어떤 모델을 기반으로 입력공간
        fields =['title', 'body']   # 어떤 필드 입력받을 건지

# # 임의의 입력공간
# class BlogPost(forms.Form):
#     email = forms.EmailField()
#     files = forms.FileField()
#     url = forms.URLField()
#     words = forms.CharField(max_length=200)
#     max_number = forms.ChoiceField(choices=[('1','one'), ('2','two'),('3','three')])
#     # 선택 항목과 값에 대해 선택 one에 대해선 1로 간주, one, two, three가 화면에 나옴