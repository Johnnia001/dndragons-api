from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Character(models.Model):
    # define fields
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    exp = models.CharField(max_length=100)
    charClass = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    alignment = models.CharField(max_length=100)
    background = models.CharField(max_length=300)
    strength = models.CharField(max_length=300)
    dexterity = models.CharField(max_length=100)
    constitution = models.CharField(max_length=100)
    intelligence = models.CharField(max_length=100)
    wisdom = models.CharField(max_length=100)
    charisma = models.CharField(max_length=100)
    prof = models.CharField(max_length=100)
    savingThrows = models.CharField(max_length=100)
    skills = models.CharField(max_length=300)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        # This must return a string
        return f"character'{self.name}', is level {self.level} "

   # def as_dict(self):
   #     """Returns dictionary version of Character models"""
   #     return {
   #         'id': self.id,
   #         'name': self.name,
   #         'level': self.level,
   #         'exp': self.exp,
   #         'charClass':self.charClass,
   #        'race': self.race,
   #         'alignment': self.alignment,
   #         'background': self.background
   #     }
