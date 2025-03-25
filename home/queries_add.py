import django
import os
from django.db import connection


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Project_Dj_proff_l.settings")
django.setup()


# **


sql = """
    SQL QUERY
"""


def insert_data():
    with connection.cursor() as cursor:
        cursor.execute(sql)
    print("Данные успешно добавлены!")


if __name__ == "__main__":
    insert_data()
