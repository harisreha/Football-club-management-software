from django.db.models import fields
from django.forms import ModelForm
from .models import Players,Members, Prihod,Staff,Rashod


class PlayersForm(ModelForm):
    class Meta:
        model = Players
        fields = '__all__'

class MembersForm(ModelForm):
    class Meta:
        model = Members
        fields = '__all__'

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

class PrihodForm(ModelForm):
    class Meta:
        model = Prihod
        fields = '__all__'

class RashodForm(ModelForm):
    class Meta:
        model = Rashod
        fields = '__all__'