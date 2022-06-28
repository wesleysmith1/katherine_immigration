from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'voting_preferences'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


choices = [
        [1, 'Very important'],
        [2, 'Somewhat important'],
        [3, 'Not too important'],
        [4, 'Not at all important'],
    ]

scale_choices = [
        [1, 'Extremely Unlikely'],
        [2, 'Unlikely'],
        [3, 'Somewhat Unlikely'],
        [4, 'Somewhat Likely'],
        [5, 'Likely'],
        [6, 'Extremely Likely']
    ]

class Player(BasePlayer):
    voting_preferences1 = models.IntegerField(
        choices=choices,
        label="Increasing security along U.S.-Mexico border is a (blank) goal for U.S. immigration policy."
    )

    voting_preferences2 = models.IntegerField(
        choices=choices,
        label="Establishing a way for immigrants here illegally to stay legally is a (blank) goal for U.S. immigration policy."
    )

    voting_preferences3 = models.IntegerField(
        choices=choices,
        label="Taking in refugees escaping from war and violence is a (blank) goal for U.S. immigration policy."
    )    

    voting_preferences4 = models.IntegerField(
        choices=choices,
        label="Thinking about the issue of immigration, how important of a goal should the following be for immigration policy in the U.S.?"
    )

    voting_preferences5 = models.IntegerField(
        choices=scale_choices,
        label="What is the likelihood you would support legislation: Increasing immigration levels by 10%?",
    )
    
    voting_preferences6 = models.IntegerField(
        choices=scale_choices,
        label="What is the likelihood you would support legislation: Simplifying the naturalization process for current illegal immigrants and low skilled immigrants?",
    )

    voting_preferences7 = models.IntegerField(
        choices=scale_choices,
        label="What is the likelihood you would support legislation: Increasing H-1B visas and immigration opportunities for highly skilled immigrants?",
    )


# FUNCTIONS
# PAGES
class VotingPreferences1(Page):
    form_model = 'player'
    form_fields = ['voting_preferences1']


class VotingPreferences2(Page):
    form_model = 'player'
    form_fields = ['voting_preferences2']


class VotingPreferences3(Page):
    form_model = 'player'
    form_fields = ['voting_preferences3']


class VotingPreferences4(Page):
    form_model = 'player'
    form_fields = ['voting_preferences4']


class VotingPreferences5(Page):
    form_model = 'player'
    form_fields = ['voting_preferences5']


class VotingPreferences6(Page):
    form_model = 'player'
    form_fields = ['voting_preferences6']


class VotingPreferences7(Page):
    form_model = 'player'
    form_fields = ['voting_preferences7']


page_sequence = [VotingPreferences1, VotingPreferences2, VotingPreferences3, VotingPreferences4, VotingPreferences5, VotingPreferences6, VotingPreferences7]