from django import forms
import datetime

'''
class MarketNameForm(forms.Form):
    market_name = forms.CharField(label='Market Name',max_length=100)
    print market_name
'''

class StartDateForm(forms.Form):
    start_date = forms.DateField(label='Start Date',required=False)
    print start_date
