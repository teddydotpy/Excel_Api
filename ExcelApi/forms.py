from django import forms

gender_choices = (
    (1, 'Choose a Gender'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)

race_choices = (
    (1, 'Pick race'),
    ('African', 'African'),
    ('White', 'White'),
    ('Asian', 'Asian'),
    ('Indian', 'Indian'),
    ('Hispanic', 'Hispanic'),
    ('Other', 'Other'),
)

area_choices = (
    (1, 'Choose Area'),
    ('Gauteng', 'Gauteng'),
    ('Kwazulu_Natal', 'Kwazulu_Natal'),
    ('Limpopo', 'Limpopo'),
    ('Mpumalanga', 'Mpumalanga'),
    ('Western Cape', 'Western Cape'),
    ('North West', 'North West'),
    ('Eastern Cape', 'Eastern Cape'),
    ('Free State', 'Free State')
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