from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Andrew Wang'

doc = """
Simple survey demonstrating number pad and slider.
"""


class Constants(BaseConstants):
    emotions = ['Happiness', 'Sadness', 'Anger', 'Excitedness']
    emotion_adjectives = ['happy', 'sad', 'angry', 'excited']


    name_in_url = 'simple_survey'
    players_per_group = None
    num_rounds = len(emotions)



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.CharField()
    age = models.FloatField()
    salary = models.FloatField()

    emotion = models.CharField()
    val = models.IntegerField()