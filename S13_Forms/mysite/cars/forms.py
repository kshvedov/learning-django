from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label="First Name", max_length=100)
#     last_name = forms.CharField(label="Last Name", max_length=100)
#     email = forms.EmailField(label="Email")
#     review = forms.CharField(label="Please write your review here",
#                              widget=forms.Textarea(attrs={"class":"myform"}))


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        #fields = ["first_name", "last_name", "stars"]
        fields = "__all__" # pass in all fields as model fields

        labels = {
            "first_name": "YOUR FIRST NAME",
            "last_name": "Last Name, I MEAN FAMILY",
            "stars": "Rating"
        }

        error_messages = {
            "stars": {
                "min_value": "VALUE BELOW 1, HAS TO BE >= 1 AND <= 5",
                "max_value": "VALUE ABOVE 5, HAS TO BE >= 1 AND <= 5"
            }
        }