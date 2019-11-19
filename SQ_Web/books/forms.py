from django import forms
from comics.models import Comics


class UploadPaintsForm(forms.ModelForm):
    bookname = forms.CharField(max_length=20, min_length=1, label="书名",error_messages={"required":"书名不能为空"},
                               help_text="最小1位，最长20位")
    page = forms.IntegerField(max_value=1000, min_value=1, label="章节",
                               help_text="1-1000")
    paints = forms.ImageField(label="作品", required=True, error_messages={"required":"不能提交空文件"})
    class Meta:
        model = Comics
        fields = ['bookname', 'paints']