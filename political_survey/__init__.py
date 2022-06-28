from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'political_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    voted = models.StringField(
        label='Did you vote in the last election?',
        choices=['Yes', 'No', 'Prefer not to answer']
    )

    political_party = models.StringField(
        label='Generally speaking, do you usually think of yourself as a Republican, a Democrat, an Independent, or something else?',
        choices=['Republican', 'Democrat', 'Independent', 'Something else',],
        widget=widgets.RadioSelectHorizontal,
    )

    democrat = models.StringField(
        label='If you think of yourself as a Democrat, would you call yourself a strong Democrat or a not very strong Democrat?',
        choices=['Strong', 'Not very strong', 'I do not think of myself as a Democrat'],
        widget=widgets.RadioSelectHorizontal,
    )

    republican = models.StringField(
        label='If you think of yourself as a Republican, would you call yourself a strong Republican or a not very strong Republican?',
        choices=['Strong', 'Not very strong', 'I do not think of myself as a Republican'],
        widget=widgets.RadioSelectHorizontal,
    )

    independent = models.StringField(
        label='If you think of yourself as an Independent, do you think yourself as closer to the Republican Party or to the Democratic Party, or neither?',
        choices=['Closer to the Republican Party', 'Closer to the Democratic Party', 'Neither', 'I do not think of myself as an Independent'],
        widget=widgets.RadioSelectHorizontal,
    )

    describe_yourself = models.IntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="Yourself"
    )

    describe_democrats = models.IntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="Democrats"
    )

    describe_republicans = models.IntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="Republicans"
    )


# FUNCTIONS
# PAGES
class Survey(Page):
    form_model = 'player'
    form_fields = [
        'voted', 
        'political_party',
        'democrat',
        'republican',
        'independent',
        'describe_yourself',
        'describe_democrats',
        'describe_republicans',
    ]


page_sequence = [Survey]
