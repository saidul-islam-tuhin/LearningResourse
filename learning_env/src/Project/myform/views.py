from django.shortcuts import render,HttpResponse
from django.views.generic.edit import CreateView
from .forms import CommentForm,ContactForm,VerifiedPhoneForm
from django.conf import settings
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import random


# Create your views here.
#class CreateForm(CreateView):
 #   template_name = 'myform/check.html'
  #  form_class = CommentForm
def CreateForm(request):
    form = CommentForm(request.POST or None)
    form1= ContactForm()
    if form.is_valid():
        url = request.POST.get('url', None)
        #birth_year = request.POST.get('birth_year', None)
        #birth_year = form.cleaned_data['birth_year']
        birth_year = form.cleaned_data.get('birth_year', None)
        #favorite_colors = request.POST('favorite_colors', None)
        favorite_colors = form.cleaned_data['favorite_colors'] #request.POST.getlist('checks')
        print(url)
        print(birth_year)
        print(favorite_colors)
    return render(request, 'myform/check.html',{'form': form,'form1': form1,})

def VerifiedPhone(request):
    return render(request, 'myform/phone.html',{'form':VerifiedPhoneForm()})

def SmsSend(request):
    print(settings.TWILIO_ACCOUNT_SID)
    print(settings.TWILIO_AUTH_TOKEN)
    length=5
    pin_no=random.sample(range(10**(length-1), 10**length), 1)[0]
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    try:
        response = client.lookups.phone_numbers('+8801758885495').fetch(type="carrier")
        print("vaild")
    except TwilioRestException as e:
        if e.code == 20404:
            print("not vaild")
        else:
            raise e
    message = client.messages.create(
                        body="verification pin number :%s"%pin_no,
                        to='+8801755907799',
                        from_=settings.TWILIO_FROM_NUMBER,
                    )
    return HttpResponse("Message %s sent" % message.sid, mimetype='text/plain', status=200)
    #return HttpResponse("hi")
