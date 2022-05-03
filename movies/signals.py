import datetime

def congratulatory(sender, instance, created, **kwargs):
    if created and instance.updated_at == datetime.date.today():
        print(f"У {instance.full_name} сегодня день рождения! 🥳")

from django.db.models.signals import post_save

post_save.connect(receiver=congratulatory, sender='movies.Person', weak=True, dispatch_uid='congratulatory_signal')
