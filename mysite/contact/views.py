
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

from contact.forms import ContactForm


def thanks(request):
    return render(request, 'thanks_email.html')


'''
def contact(request):
    error_types = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            error_types.append('Enter a subject.')
        if not request.POST.get('message', ''):
            error_types.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            error_types.append('Enter a valid e-mail address.')
        if not error_types:
            send_mail(request.POST['subject'], request.POST['message'],
                      request.POST.get('email', 'l******u@gmail.com'),
                      ['1*******9@qq.com'],)
            return HttpResponseRedirect('/contact/thanks/')
    return render(request, 'contact_form.html', {'errors': error_types})
'''
   
'''
def contact(request):
    error_types = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            error_types.append('Enter a subject.')
        if not request.POST.get('message', ''):
            error_types.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            error_types.append('Enter a valid e-mail address.')
        if not error_types:
            send_mail(request.POST['subject'], request.POST['message'],
                      request.POST.get('email', 'l******u@163.com'),
                      ['1********9@qq.com'],)
            return HttpResponseRedirect('/contact/thanks/')
    return render(request, 'contact_form.html', {
                           'errors': error_types,
                           'subject': request.POST.get('subject', ''),
                           'message': request.POST.get('message', ''),
                           'email': request.POST.get('email', ''),}
                 )
'''


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['subject'], cd['message'],
                      cd.get('email', 'l*****u@163.com'),
                      ['1*******9@qq.com'],)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject':'I love your site!'})
    return render(request, 'contact_form.html', {'form': form})


