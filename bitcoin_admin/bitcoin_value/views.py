from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from .forms import StartDateForm


def index(request):
    return render(request,
                  'bitcoin_value/home.html')

'''
def get_name(request):
    # if this is a POST request we need to process the form data
    print request.method
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MarketNameForm(request.POST)
        # check whether it's valid:
        print form.is_valid()
        return redirect('http://www.quandl.com/api/v3/datasets/BCHARTS/')
        #return render(request,'http://www.quandl.com/api/v3/datasets/BCHARTS/')
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'http://www.quandl.com/api/v3/datasets/BCHARTS/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MarketNameForm()

    return render(request, 'name.html', {'form': form})
'''
    
def get_name(request):
    form = StartDateForm(request.POST)
    print form.is_valid()
    return redirect('http://www.quandl.com/api/v3/datasets/BCHARTS/BITSTAMPUSD')
    
