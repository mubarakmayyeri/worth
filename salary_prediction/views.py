from django.shortcuts import render

# Create your views here.


def prediction(request):
    if request.method == 'POST':
        domain = request.POST['domain']
        age = request.POST['age']
        designation = request.POST['designation']
        cs_bg = request.POST['cs_bg']
        experience = request.POST['experience']
        degree = request.POST['degree']
        avg_time = request.POST['avg_time']
        holidays = request.POST['holidays']
        week_back = request.POST['week_back']
        graduate = request.POST['graduate']
        skills = request.POST.getlist('skills')

        print(domain, age, designation, cs_bg, experience, degree, avg_time, holidays, week_back, graduate)
        print('Skills', skills)
        
    return render(request, 'prediction.html')