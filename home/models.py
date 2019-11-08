from django.db import models
from django.forms import ModelForm


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    course_number = IntegerRangeField()
    group_number = IntegerRangeField()
    teacher = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = IntegerRangeField(min_value=0, max_value=4)
    second_day = IntegerRangeField(min_value=0, max_value=4)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.FileField(null=True, upload_to="media/profile/")
