from django.db import models
from .get_country import get_country_code
# Create your models here.
class Peak(models.Model):
    """Model definition for Peak."""
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    altitude = models.IntegerField()
   

    # TODO: Define fields here

    class Meta:
        """Meta definition for Peak."""

        verbose_name = 'Peak'
        verbose_name_plural = 'Peaks'

    def __str__(self):
        """Unicode representation of Peak."""
        return '{' + 'lat: {}, lng: {}, name: "{}"'.format(self.latitude, self.longitude, self.name)

    @property
    def full_url(self):
        """Unicode representation of Peak."""
        return '{' + 'lat: {}, lng: {}, name: "{}"'.format(self.latitude, self.longitude, self.name) +  '}' 

    # def save(self):
    #     """Save method for Peak."""
    #     pass

    def get_absolute_url(self):
        """Return absolute url for Peak."""
        return ('')

    # TODO: Define custom methods here




class WhiteListCountry(models.Model):
    country_code = models.CharField(max_length=2)

    def __str__(self):
        return self.country_code

    @staticmethod
    def is_country_allowed(country_code):
        return WhiteListCountry.objects.filter(country_code=country_code).exists()


class RejectedConnexion(models.Model):
    """Model definition for RejectedConnexion."""
    ip = models.CharField(max_length=15, blank=True,null=True)
    country_code = models.CharField(max_length=2, blank=True,null=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for RejectedConnexion."""

        verbose_name = 'Rejected Connexion'
        verbose_name_plural = 'Rejected Connexions'

    def __str__(self):
        """Unicode representation of RejectedConnexion."""
        return '{} {}'.format(self.country_code, self.ip)

    def get_absolute_url(self):
        """Return absolute url for RejectedConnexion."""
        return ('')

    # TODO: Define custom methods here
