from django import forms
from vaccimo.models import user
from vaccimo.models import sideeffect
from vaccimo.models import questioner

 
 
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

class questionerForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = questioner
 
        # specify fields to be used
        fields = [
        'id','Q0','Q1','Q2','Q3','Q4','Q5','Q6','Q7',
        'Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15',
        'Q16','Q17','Q18','Q19','Q20','Q21','Q22','allergy','Q23','Q24'
        ]                   