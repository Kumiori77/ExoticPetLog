from django.core.exceptions import ValidationError

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 6:
            raise ValidationError("비밀번호를 6글자 이상으로 설정해주세요")
