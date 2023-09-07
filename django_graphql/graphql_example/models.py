from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    """
    Address has number, street, city, state
    """
    class States(models.TextChoices):
        """
        States enum field
        """
        ALASKA = 'AK', _('Alaska')
        ALABAMA = 'AL', _('Alabama')
        ARKANSAS = 'AR', _('Arkansas')
        ARIZONA = 'AZ', _('Arizona')
        CALIFORNIA = 'CA', _('California')
        COLORADO = 'CO', _('Colorado')
        CONNECTICUT = 'CT', _('Connecticut')
        DELAWARE = 'DE', _('Delaware')
        FLORIDA = 'FL', _('Florida')
        GEORGIA = 'GA', _('Georgia')
        HAWAII = 'HI', _('Hawaii')
        IOWA = 'IA', _('Iowa')
        IDAHO = 'ID', _('Idaho')
        ILLINOIS = 'IL', _('Illinois')
        INDIANA = 'IN', _('Indiana')
        KANSAS = 'KS', _('Kansas')
        KENTUCKY = 'KY', _('Kentucky')
        LOUISIANA = 'LA', _('Louisiana')
        MASSACHUSETTS = 'MA', _('Massachusetts')
        MARYLAND = 'MD', _('Maryland')
        MAINE = 'ME', _('Maine')
        MICHIGAN = 'MI', _('Michigan')
        MINNESOTA = 'MN', _('Minnesota')
        MISSOURI = 'MO', _('Missouri')
        MISSISSIPPI = 'MS', _('Mississippi')
        MONTANA = 'MT', _('Montana')
        NORTH_CAROLINA = 'NC', _('North Carolina')
        NORTH_DAKOTA = 'ND', _('North Dakota')
        NEBRASKA = 'NE', _('Nebraska')
        NEW_HAMPSHIRE = 'NH', _('New Hampshire')
        NEW_JERSEY = 'NJ', _('New Jersey')
        NEW_MEXICO = 'NM', _('New Mexico')
        NEVADA = 'NV', _('Nevada')
        NEW_YORK = 'NY', _('New York')
        OHIO = 'OH', _('Ohio')
        OKLAHOMA = 'OK', _('Oklahoma')
        OREGON = 'OR', _('Oregon')
        PENNSYLVANIA = 'PA', _('Pennsylvania')
        RHODE_ISLAND = 'RI', _('Rhode Island')
        SOUTH_CAROLINA = 'SC', _('South Carolina')
        SOUTH_DAKOTA = 'SD', _('South Dakota')
        TENNESSEE = 'TN', _('Tennessee')
        TEXAS = 'TX', _('Texas')
        UTAH = 'UT', _('Utah')
        VIRGINIA = 'VA', _('Virginia')
        VERMONT = 'VT', _('Vermont')
        WASHINGTON = 'WA', _('Washington')
        WISCONSIN = 'WI', _('Wisconsin')
        WEST_VIRGINIA = 'WV', _('West Virginia')
        WYOMING = 'WY', _('Wyoming') 

    number = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=States.choices)

    def __str__(self):
        return f"{self.number} {self.street}, {self.city}, {self.state}"


class Person(models.Model):
    """
    Person has email, name, address
    """
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
