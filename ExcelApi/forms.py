from django import forms

gender_choices = (
    (1, 'Choose a Gender'),
    (2, 'Male'),
    (3, 'Female'),
    (4, 'Other')
)

race_choices = (
    (1, 'Pick race'),
    (2, 'African'),
    (3, 'White'),
    (4, 'Asian'),
    (5, 'Indian'),
    (6, 'Hispanic'),
    (7, 'Other')
)

area_choices = (
    (1, 'Choose Area'),
    (2, 'Gauteng'),
    (3, 'Kwazulu_Natal'),
    (4, 'Limpopo'),
    (5, 'Mpumalanga'),
    (6, 'Western Cape'),
    (7, 'North West'),
    (8, 'North West'),
    (9, 'Eastern Cape'),
    (10, 'Eastern Cape'),
    (11, 'Free State')
)

class Userform(forms.Form):
    Name = forms.CharField(max_length=30, required=True)
    Surname = forms.CharField(max_length=30, required=True)
    Age = forms.IntegerField(required=True)
    Gender = forms.ChoiceField(choices=gender_choices, widget=forms.Select())
    Race = forms.ChoiceField(choices=race_choices, widget=forms.Select())
    Area = forms.ChoiceField(choices=area_choices, widget=forms.Select())
    Contact_Number = forms.IntegerField(required=True)
    Email = forms.EmailField(required=True)