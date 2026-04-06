from django.db import models

# Create your models here.
class Form(models.Model):
    years = [
        ('FN', 'Freshman'),
        ('SE', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    ]
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    year = models.CharField(
        max_length=2,
        choices=years,
    )
    preferred_schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    school_schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    unavailable_schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)



class Schedule(models.Model):
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
    start = models.TimeField()
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
