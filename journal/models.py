from django.db import models
from datetime import datetime

today = datetime.today().strftime("%Y-%m-%d")

# Create your models here.

class DailyImage(models.Model):
    date = models.DateField(auto_now_add=True, unique=True)
    name = models.CharField(max_length = 1000)
    image = models.CharField(max_length = 1000)
    location = models.CharField(max_length = 1000)

    def __str__(self):
        return str(self.date) + ": " + self.name + ", " + self.location #originally str(self.date)

class JournalEntry(models.Model):
    date = models.DateField(auto_now_add=True)
    today_grateful = models.CharField(max_length = 500)
    affirmations = models.CharField(max_length = 500)
    amazing_things = models.CharField(max_length = 500)
    today_better = models.CharField(max_length = 500)
    wish_change = models.CharField(max_length = 500)
    brain_dump = models.CharField(max_length = 5000)
    image = models.ForeignKey(DailyImage, to_field='date', default=today)

    def __str__(self):
        if len(self.brain_dump) < 100:
            return self.brain_dump
        else:
            return self.brain_dump[0:100] + '  ...'
