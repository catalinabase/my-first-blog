from django.db import models
from django.utils import timezone

WOWCLASSES = (  
    ('DK', 'Death Knight'),
    ('DH', 'Demon Hunter'),
    ('MON', 'Monk'),
    ('SHA', 'Shaman'),
    ('PAL', 'Paladin'),
    ('PRI', 'Priest'),
    ('HUN', 'Hunter')
)

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    wowclass = models.CharField(max_length=3, choices=WOWCLASSES, default='')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

