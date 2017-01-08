from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class NamePage(Page):
    form_model = models.Player
    form_fields = ['name']

    def is_displayed(self):
        return self.round_number == 1

class AgePage(Page):
    form_model = models.Player
    form_fields = ['age']

    def is_displayed(self):
        return self.round_number == 1

class SalaryPage(Page):
    form_model = models.Player
    form_fields = ['salary']

    def is_displayed(self):
        return self.round_number == 1

class EmotionPage(Page):

    def get_round_number(self):
        return self.round_number

    def get_current_emotion(self):
        return Constants.emotions[self.get_round_number() - 1]

    def get_current_emotion_adjective(self):
        return Constants.emotion_adjectives[self.get_round_number() - 1]

    form_model = models.Player
    form_fields = ['emotion', 'val'] # Indexed starting at 1

    def vars_for_template(self):
        return {'current_emotion': self.get_current_emotion(),
                'current_emotion_adjective': self.get_current_emotion_adjective()}

page_sequence = [
    NamePage,
    AgePage,
    SalaryPage,
    EmotionPage,
]
