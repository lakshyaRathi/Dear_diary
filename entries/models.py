from django.db import models

class Entries(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Entries #{}'.format(self.id)

    
    class Meta:
        verbose_name_plural='entries'
