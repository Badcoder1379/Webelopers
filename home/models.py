from django.db import models


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
    course_number = IntegerRangeField(max_value=100000)
    group_number = IntegerRangeField(max_value=10)
    teacher = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = IntegerRangeField(min_value=0 , max_value=4)
    second_day = IntegerRangeField(min_value=0, max_value=4)
