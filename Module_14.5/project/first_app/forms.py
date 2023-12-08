from django import forms
from django.core import validators
from first_app.models import StudentModel

class ExampleForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years='BIRTH_YEAR_CHOICES'))
    value = forms.DecimalField( required = False)
    message = forms.CharField(max_length =10,)
    email_address = forms.EmailField( 
    label="Please enter your email address",)
    first_name = forms.CharField(label="First Name", initial='Your name')
    
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)

    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    password = forms.CharField(widget = forms.PasswordInput()) 

    field_name = forms.FileField()
    img_name = forms.ImageField()
    GIPAddress = forms.GenericIPAddressField()
    nullboolean = forms.NullBooleanField()
    Slug_Field = forms.SlugField(max_length = 200) 
    time_field = forms.TimeField( ) 
    URL_field = forms.URLField( ) 
    uuidf_field = forms.UUIDField( ) 
    help_field = forms.CharField(help_text = "Enter your Name", required=False)

    error_field = forms.CharField( 
                  error_messages = { 
                 'required':"Please Enter your Nameeeeeeeeeee"
                 }) 
    disable_field = forms.CharField(disabled = True) 



class StudentForm(forms.ModelForm):
    class Meta: 
        model = StudentModel
        fields = '__all__'

    widget={'date_field':forms.NumberInput(attrs={'type': 'date'})}