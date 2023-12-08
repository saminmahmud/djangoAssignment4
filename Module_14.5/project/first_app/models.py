from django.db import models
from django.core import validators

class StudentModel(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    email_field = models.EmailField()
    binary_field = models.BinaryField(max_length=20)
    lala = models.BigAutoField(primary_key=True)
    char_field = models.CharField(max_length=255)
    # comma_separated_field = models.CharField(
    #     validators=[validators.comma_separated_validator],
    #     max_length=255
    # )
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    file_field = models.FileField(upload_to='files/')
    float_field = models.FloatField()
    generic_ip_address_field = models.GenericIPAddressField()
    image_field = models.ImageField(upload_to='images/')
    integer_field = models.IntegerField()
    json_field = models.JSONField()
    null_boolean_field = models.BooleanField(null=True)
    positive_big_integer_field = models.PositiveBigIntegerField()
    positive_integer_field = models.PositiveIntegerField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    slug_field = models.SlugField()
    small_integer_field = models.SmallIntegerField()
    text_field = models.TextField()
    time_field = models.TimeField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()
    
# def __str__(self):
#     return f'{self.name} and {self.roll}'
