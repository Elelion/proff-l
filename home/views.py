import os

import django

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import DetailView, TemplateView

from .models import *
from .static_data import *


# -----------------------------------------------------------------------------


class HomeIndex(TemplateView):
    print(django.get_version())

    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['SEO_title'] = 'Безрамное панорамное остекление - Проф-Лайн'
        context['sliders'] = SLIDERS
        context['glazing_frameless'] = GlazingFrameless.objects.all().order_by('id')
        context['advantages'] = ADVANTAGES
        context['glazing_frameless_types'] = GlazingType.objects.all().order_by('id')
        context['questions'] = QUESTIONS

        return context


class HomeGlazingFramelessDetail(DetailView):
    model = GlazingFrameless
    context_object_name = 'glazing_frameless'
    template_name = 'home/glazing_frameless_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['SEO_title'] = f'{self.object.title} | Решения для безрамного остекления',

        return context


class HomeGlazingFramelessTypeDetail(DetailView):
    model = GlazingType
    context_object_name = 'glazing_type'
    template_name = 'home/glazing_frameless_type_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['SEO_title'] = f'{self.object.title} | Типы безрамного остекления',

        return context


# -----------------------------------------------------------------------------


def feedback_modal(request):
    if request.method == 'POST':
        data_type = request.POST.get('data-type')
        name = ''
        phone = ''

        # TODO: оставляем для SPAM бота, в коде НЕ используется
        # bot_check = ''  # проверка, заполнял ли форму бот или человек
        # recaptcha_response = request.POST.get('g-recaptcha-response')

        # **

        if data_type == 'modal':
            name = request.POST['feed-back-modal-name']
            phone = request.POST['feed-back-modal-phone']

        # **

        # проверяем кликнули на нашу капчу или нет
        # if not recaptcha_response:
        #    return HttpResponse(f'Вы не прошли проверку капчи...')

        # **

        # TODO: оставляем для SPAM бота, в коде НЕ используется
        # проверка, если имя и телефон заполнены
        # и bot_chech НЕ заполнено, то все ок
        # bot_check - скрытое поле, боты заполнят его автоматически
        # if name != "" and phone != "" and bot_check == "":

        if name != "" and phone != "":
            feedback_send_mail(name, phone)

            return redirect('home:success_mail')
        else:
            errors_data = {
                'title_html_h1': '<span>4</span><span>2</span><span>3</span>',
                'title': 'Ошибка 423',
                'message_html': 'Обнаружен СПАМ бот! '
                                'Проверка не пройдена! '
                                'Свяжитесь с нами по указанным на сайте телефону',
            }

            return render(
                request,
                'home/error_page.html',
                {'errors_data': errors_data},
                status=423)


# **


def feedback_send_mail(name, phone):
    # theme
    # body
    # form
    # [to, to, to...]
    send_mail('Заявка с сайта proff-l.ru',

              'Новая заявка с сайта:\n\n'
              f'Имя клиента: {name}\n'
              f'Телефон клиента: {phone}\n',

              'proff.l.ru@gmail.com',
              [os.getenv('EMAIL_MAIN_RECIPIENT')],
              fail_silently=False)


def success_mail(request):
    notification = NOTIFICATION.get('mail_send_ok', {})

    context = {
        'img': notification.get('img'),
        'title': notification.get('title'),
        'text': notification.get('text'),
    }

    return render(request, 'home/notification_user.html', context)


# -----------------------------------------------------------------------------


def page_not_found(request, exception):
    errors_data = {
        'title': '404',
        'title_description': '404 ошибка!',
        'message': 'Ой, ой! Вы попали на не существующую страницу!',
    }

    return render(
        request,
        'home/error_page.html',
        {'errors_data': errors_data},
        status=404)
