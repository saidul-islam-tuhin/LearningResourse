from django import forms
from django.forms.utils import ErrorList

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)
class CustomizeErrorList(ErrorList):
    def __str__(self):
        return self.as_custo()
    def as_custo(self):
        if not self:
            return 'success'
        return '<div class="errorlist">%s</div>'% ''.join(['<div class="myerror">%s</div>' % e for e in self])

class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special','id':'my'}))
    url = forms.URLField()
    #comment = forms.CharField(widget=forms.Textarea)
    #birth_year1 = forms.DateTimeField()
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors1 = forms.MultipleChoiceField(
        required=False,
        #widget=forms.CheckboxInput(check_yest = is_checked)
        #choices=FAVORITE_COLORS_CHOICES,
    )
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #choices=FAVORITE_COLORS_CHOICES,
    )

class ContactForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class VerifiedPhoneForm(forms.Form):
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'special','id':'my'}))
    pin_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'special','id':'my'}))
