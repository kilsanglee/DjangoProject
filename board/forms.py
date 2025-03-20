from django import forms
from board.models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content']  # today 는 제외 하여야 한다.

