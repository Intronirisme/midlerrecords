from django.shortcuts import render
from .models import Page, Site, Studio
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.
def index(request):
    apparence = Site.objects.first()
    context = {
        'background': apparence.background,
        'description': apparence.description,
        'front': apparence.front,
        'back': apparence.back,
        'right': apparence.right,
        'left': apparence.left,
        'top': apparence.top,
        'bottom': apparence.bottom,
        'fonttitle': apparence.fonttitle,
        'fontbody': apparence.fontbody,
        'fontbodylight': apparence.fontbodylight,
        'fontbodybold': apparence.fontbodybold,
        'content': Page.objects.get_real_instances()
    }
    return render(request, 'index.html', context)

def contact(request):
    apparence = Site.objects.first()
    context = {
        'background': apparence.background,
        'description': apparence.description,
        'fonttitle': apparence.fonttitle,
        'fontbody': apparence.fontbody,
        'fontbodylight': apparence.fontbodylight,
        'fontbodybold': apparence.fontbodybold
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = '''De : {0}
Addresse : {1}
Message :

{2}
            '''.format(form.cleaned_data['name'], form.cleaned_data['email_address'], form.cleaned_data['message'])
            try:
                send_mail(
                    subject = "Midler Records",
                    message = message,
                    from_email = None,
                    recipient_list = [apparence.mailing_address],
                    fail_silently = False
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'thanks.html', context)
    else:
        form = ContactForm()
        context['form'] = form
        return render(request, 'contact.html', context)