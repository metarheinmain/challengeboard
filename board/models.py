from django.db import models


class Challenge(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    datetime_end = models.DateTimeField(verbose_name='End date', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    mode = models.CharField(max_length=100, choices=(
        ('max', 'Highest value wins'),
        ('min', 'Lowest value wins'),
        ('first', 'First entry wins'),
    ))
    value_unit = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_highscore(self):
        if self.mode == 'max':
            order = '-value'
            val = lambda p: p.value
        elif self.mode == 'min':
            order = 'value'
            val = lambda p: p.value
        elif self.mode == 'first':
            self.mode = '-datetime'
            val = lambda p: p.datetime
        ps = list(self.participants.order_by(order))
        curval = None
        curpos = 0
        for p in ps:
            if curval is None or val(p) != curval:
                curpos += 1
                curval = val(p)
            p.pos = curpos
        return ps


class Participant(models.Model):
    challenge = models.ForeignKey(Challenge, related_name="participants")
    name = models.CharField(max_length=300)
    value = models.FloatField(null=True, blank=True)
    datetime = models.DateTimeField()

    def __str__(self):
        return self.name
