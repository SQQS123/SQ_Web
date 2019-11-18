from django import forms
from comics.models import Comics


class UploadPaintsForm(forms.Form):
    page = forms.IntegerField(max_value=1000, min_value=1, label="章节",
                               help_text="1-1000")
    paints = forms.ImageField(label="作品", required=True, error_messages={"required":"不能提交空文件"})