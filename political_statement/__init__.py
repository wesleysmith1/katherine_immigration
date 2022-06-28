from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'main'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


choices = [
        [1, 'Strongly persuasive in favor of immigration'],
        [2, 'Somewhat persuasive in favor of immigration'],
        [3, 'Neither persuasive nor non-persuasive in favor of immigration'],
        [4, 'Not too persuasive in favor of immigration'],
        [5, 'Not at all persuasive in favor of immigration']
    ]


class Player(BasePlayer):

    ps1 = models.IntegerField(
        choices=choices,
        label="Having read both both the statement and the fact check, how persuasive do you now find the politician’s statement?"
    )

    ps2 = models.IntegerField(
        choices=choices,
        label="Having read both both the statement and the fact check, how persuasive do you now find the politician’s statement?"
    )

    ps3 = models.IntegerField(
        choices=choices,
        label="Having read both both the statement and the fact check, how persuasive do you now find the politician’s statement?"
    )

    ps4 = models.IntegerField(
        choices=choices,
        label="Having read both both the statement and the fact check, how persuasive do you now find the politician’s statement?"
    )


# FUNCTIONS
# PAGES
class PoliticalStatement1(Page):
    form_model='player'
    form_fields=['ps1']


class PoliticalStatement2(Page):
    form_model='player'
    form_fields=['ps2']


class PoliticalStatement3(Page):
    form_model='player'
    form_fields=['ps3']


class PoliticalStatement4(Page):
    form_model='player'
    form_fields=['ps4']


page_sequence = [PoliticalStatement1, PoliticalStatement2, PoliticalStatement3, PoliticalStatement4,]