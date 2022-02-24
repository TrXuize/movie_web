from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'movie_name',
            'discription',
            'total_time',
            'img'
        ]

class RawMovieForm(forms.Form):
    movie_name = forms.CharField()
    discription = forms.CharField(widget=forms.Textarea())
    release_time = forms.DateField()
    total_time = forms.CharField()
    img = forms.ImageField()

class SeatForm(forms.Form):
    seat1 = forms.IntegerField(required= False)
    seat2 = forms.IntegerField(required= False)
    seat3 = forms.IntegerField(required= False)
    seat4 = forms.IntegerField(required= False)
    
    def clean_seat1(self, *arg, **kwargs):
        seat1 = self.cleaned_data.get("seat1")
        if seat1 is None:
            return seat1
        elif (seat1<0)|(seat1>49):
            raise forms.ValidationError("BAD")
        return seat1
    def clean_seat2(self, *arg, **kwargs):
        seat2 = self.cleaned_data.get("seat2")
        if seat2 is None:
            return seat2
        elif (seat2<0)|(seat2>49):
            raise forms.ValidationError("BAD")
        return seat2
    def clean_seat3(self, *arg, **kwargs):
        seat3 = self.cleaned_data.get("seat3")
        if seat3 is None:
            return seat3
        elif (seat3<0)|(seat3>49):
            raise forms.ValidationError("BAD")
        return seat3
    def clean_seat4(self, *arg, **kwargs):
        seat4 = self.cleaned_data.get("seat4")
        if seat4 is None:
            return seat4
        elif (seat4<0)|(seat4>49):
            raise forms.ValidationError("BAD")
        return seat4