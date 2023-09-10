from django import forms
from . import models

# 애완 동물 추가 폼
class AddPetForm(forms.ModelForm):
    class Meta:
        model = models.Pet

        fields = ["name", "species"]

        labels = {
            "name":"이름 ",
            "species":"종류 "
        }

# 기록 폼
class RecordForm(forms.ModelForm):
    class Meta:
        model = models.Records

        fields = ["weight", "feeding", "feededWeight", "molting"]

        labels = {
            "weight":"무게(g)",
            "feeding":"피딩 (먹이 종류)",
            "feededWeight":"피딩 무게(g)",
            "molting":"탈피 여부",
        }
        label_suffix = ''  # 콜론(:) 제외
