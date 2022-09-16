from django import forms
from vaccimo.models import user
from vaccimo.models import sideeffect

 
 
# creating a form
class userForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = user
 
        # specify fields to be used
        fields = [
           'id','file','username','email','password','name','contact_number','vaccination_brand','type',
          'vaccination_site','address', 'age','gender', 'contact_number','directory','file_name','full_path'
        ]

class sideeffectForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = sideeffect
 
        # specify fields to be used
        fields = [
        'muscle_ache','headache','fever','redness','swelling','tenderness','warmth','itch','induration',
        'feverish','chills','join_pain','fatigue','nausea','vomiting','id','name'
        ]        