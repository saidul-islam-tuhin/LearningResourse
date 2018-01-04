from django.shortcuts import render,redirect
from .forms import BlogForm,AuthorForm,EntryForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from django.http import HttpResponse
from bs4 import BeautifulSoup

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return render(request, 'grade/home.html')


def input_json(request):
    return render(request, 'grade/json.html',)


def test_json(request):
    input_value = request.GET.get('value', None)
    print(input_value)
    data = {'foo': 'bar', 'hello': 'world','input_value': input_value,}
    # json_data = json.dumps(data)  # convert dictionary into json data
    context = {'foo': 'bar',
               'investments': {'one': 1, 'two': 2},  # dictionary
               'json_data': JsonResponse(data)
               }
    #return render(request, 'grade/json.html', context)
    return JsonResponse(data)


def result_ajax(request):
    print("result_ajax")
    if request.method == 'POST':
        value = request.POST['post_value']
        print(value)
        return render(request, 'grade/ajax.html', {'value': value,})
    else:
        return render(request, 'grade/ajax.html',)

#1st
class SignUpView(CreateView):
    template_name = 'grade/signup.html'#2nd
    form_class = UserCreationForm

#4th
def validate_username(request):
    username = request.GET.get('username', None)
    password1 = request.GET.get('password1', None)
    # print(username)
    # print(password1)
    datas = {
        'is_taken': User.objects.filter(username__iexact=username).exists(),  # if exit the value is true
        'password': password1
    }
    print(datas['is_taken'])
    if datas['is_taken']:
        datas['error'] = 'A user with this username already exists.'
    print(datas)  # datas is dictionary
    return JsonResponse(datas)  # here datas convert into json data /json.dumps()

# <------- BeautifulSoup  ------->


def create_blog(request):
    form = BlogForm(request.post or None)
    if form.is_valid():
        form.save()
        redirect()

def web_scraping(request):
    with open("grade/ajax.html") as fp:
        soup = BeautifulSoup(fp)

    soup = BeautifulSoup("<html>data</html>")
    print(soup)


def show(request, one, two):
    print(one)
    print(two)
    return HttpResponse('name is:'+one+'and age is:'+two)


def question_details(request, pk):
    return HttpResponse('number is:' + pk)

"""def result(request):
    information_list = Amenity.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(information_list, 4)
    try:
        information = paginator.page(page)
    except PageNotAnInteger:
        information = paginator.page(1)
    except EmptyPage:
        information = paginator.page(paginator.num_pages)


    return render(request, 'grade/result.html', {'information': information})
    #information = Student.objects.all().order_by('std_name')
    #return render(request, 'grade/result.html', {'information': information})


def details(request,student_id):
    student = Student.objects.get(std_id=student_id)
    subject = Subject.objects.all()
    point = Point.objects.filter(std_id=student_id)
    return render(request, 'grade/details.html', {
        'student': student ,
        'subject':subject,
        'point':point
    })"""
