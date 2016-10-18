from django.db import models

# Create your models here.
class JournalEntry(models.Model):
    date = models.DateField(auto_now_add=True)
    today_grateful = models.CharField(max_length = 500)
    affirmations = models.CharField(max_length = 500)
    amazing_things = models.CharField(max_length = 500)
    today_better = models.CharField(max_length = 500)
    wish_change = models.CharField(max_length = 500)
    brain_dump = models.CharField(max_length = 5000)

    def __str__(self):
        if len(self.brain_dump) < 100:
            return self.brain_dump
        else:
            return self.brain_dump[0:100] + '  ...'
