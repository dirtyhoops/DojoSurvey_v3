from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if 'name' not in request.session:
        request.session['name'] = ''
    if 'location' not in request.session:
        request.session['location'] = ''
    if 'language' not in request.session:
        request.session['language'] = ''
    if 'comment' not in request.session:
        request.session['comment'] = ''

    return render(request,'first_app/index.html')

def process(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
    
    return redirect('/result')

def result(request):
    request.session['counter'] += 1

    formresult = {
        "counter": request.session['counter'],
        "name": request.session['name'],
        "location": request.session['location'],
        "language": request.session['language'],
        "comment": request.session['comment']
    }

    return render(request,'first_app/result.html', formresult)   

def back(request):
    if request.method == 'POST':
        return redirect('/')
