from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # optional
    sports = models.CharField(max_length=100, blank=True)

    phone = models.CharField(max_length=100)
    # TO-DO: total hours
    # total_hours = models. (max is 6)
    email = models.EmailField()


    years = [
        ('FN', 'Freshman'),
        ('SE', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    ]

    year = models.CharField(
        max_length=2,
        choices=years,
        null=True,
    )

    preferred = [
        ('WE', 'Weekend Shifts'),
        ('EM', 'Early Morning Shifts'),
        ('LN', 'Late Night Shifts'),
    ]

    preferences = ArrayField(
        models.CharField(choices=preferred, max_length=2),
        default=list,
        blank=True,
    )
    # connect multiple schedules
    # Class Schedule
    # Not Available times and reason
    # Preferred times (in the order of most to least)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    # foreign id from Form
    am_pm = [
        ('AM', 'AM'),
        ('PM', 'PM'),
    ]
    weekdays = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]

    weekday = models.CharField(
        max_length=3,
        choices=weekdays,
    )
    start = models.TimeField() # stores time in 24 hr
    # handle am, om in template display
    end = models.TimeField()
    start_am_pm = models.CharField(
        max_length=2,
        choices=am_pm,
    )
    end_am_pm = models.CharField(
        max_length=2,
        choices=am_pm,
    )
    reason = models.TextField()
