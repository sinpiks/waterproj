from django.shortcuts import render

from django.template.loader import get_template
from django.core.mail import get_connection, EmailMultiAlternatives

from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse

from  .form import *
from .models import Products, Vacancies, DEV_TYPE_OF_BOOTLE


class VacancieDescription(FormMixin, DetailView):
    model = Vacancies
    template_name = 'vacancie_description.html'
    context_object_name = 'vacancie'
    form_class = ContactForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = self.get_object()
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['phone_number'],
                         form.cleaned_data['message'])
            context = {'success': 1}
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

                               
    def get_success_url(self):
       return reverse('vacancie_description', kwargs={'pk': self.object.id})

def index(request):
    return render(request, 'index.html')

def aboutUs(request):
    return render(request, 'aboutUs.html', context = post_form(request))

def factorio(request):
    return render(request, 'factorio.html', context = post_form(request))

def description(request):
    products = Products.objects.all()
    return render(request, 'description.html', {'products' : products, 'type_of_product' : DEV_TYPE_OF_BOOTLE})

def vacancies(request):
    vacancies = Vacancies.objects.all()
    context = post_form(request)
    context['vacancies'] = vacancies
    return render(request, 'vacancies.html', context = context)

def contacts(request):
    return render(request, 'contacts.html', context = post_form(request))


#функция для отправки данных формы на почту. Дополнительные настройки в settings.py. Форма в form.py
def send_message(name, email, phone_number, message):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'email': email, 'phone_number': phone_number, 'message': message}
    subject = 'Сообщение от пользователя'
    from_email =  'iljamd2001@mail.ru'                   
    text_content = text.render(context)
    html_content = html.render(context)


    msg = EmailMultiAlternatives(subject, text_content, from_email, ['iljamd2001@mail.ru'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

# Create your views here.


def post_form(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['phone_number'],
                         form.cleaned_data['message'])
            context = {'success': 1}

    else:
        form = ContactForm()

    context['form'] = form
    return context


