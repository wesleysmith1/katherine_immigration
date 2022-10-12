from otree.api import *
import datetime

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'consent'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent_time = models.StringField(null=True)


# PAGES
class ConsentForm(Page):
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.consent_time = str(datetime.datetime.now())


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [ConsentForm, ]
