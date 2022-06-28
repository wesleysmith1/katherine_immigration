from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'big_five'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Big five
    OCEAN1 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Extraverted, enthusiastic"
    )

    OCEAN2 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Critical, inclined to argue with others"
    )

    OCEAN3 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Dependable, self-disciplined"
    )

    OCEAN4 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Anxious, easily upset"
    )

    OCEAN5 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="A deep thinker, creative"
    )

    OCEAN6 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Reserved, quiet"
    )

    OCEAN7 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Sympathetic, warm"
    )

    OCEAN8 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Disorganized, careless"
    )

    OCEAN9 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),
        label="Calm, emotionally stable"
    )

    OCEAN10 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7], 
        widget=widgets.RadioSelectHorizontal(),                                  
        label="Conventional, preferring work that is routine"
    )


# FUNCTIONS
# PAGES
class Survey(Page):
    form_model = 'player'
    form_fields = [f"OCEAN{i}" for i in range(1, 11)]


page_sequence = [Survey]
