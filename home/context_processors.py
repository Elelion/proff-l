import os

from home.models import *


def common_data_context(request):
    return {
        'user_email_context': os.getenv('EMAIL_MAIN_RECIPIENT'),
        'whatsapp_number_context': os.getenv('WHATSAPP_NUMBER_URL'),
        'contact_phone_context': os.getenv('CONTACT_PHONE'),
        'yandex_geo_link_context': os.getenv('YANDEX_GEO_URL'),
        'menu_glazing_frameless_context': GlazingFrameless.objects.all().order_by('id'),
        'menu_glazing_frameless_types_context': GlazingType.objects.all().order_by('id')
    }
