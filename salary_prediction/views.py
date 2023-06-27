from django.shortcuts import render
import pandas as pd
from .ml_model import preprocessing as preproc
from .ml_model import predictions as pred

# Create your views here.


def prediction(request):
    salary = None

    if request.method == 'POST':
        domain = request.POST.get('domain')
        age = request.POST.get('age')
        designation = request.POST.get('designation')
        cs_bg = request.POST.get('cs_bg')
        experience = request.POST.get('experience')
        degree = request.POST.get('degree')
        avg_time = request.POST.get('avg_time')
        holidays = request.POST.get('holidays')
        week_back = request.POST.get('week_back')
        graduate = request.POST.get('graduate')
        skills = request.POST.getlist('skills')

        if domain and age and designation and cs_bg and experience and degree and avg_time and holidays and week_back and graduate and skills:
            df = preproc.make_df(domain, age, designation, cs_bg, experience, degree, avg_time, holidays, week_back, graduate, skills)
            output = pred.make_perdiction(df)
            salary = output[0]
            salary = f'{salary:.2f}'
            
        else:
            print("Please provide the requested details!!")

    context = {'salary': salary}
    return render(request, 'prediction.html', context)
