from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'sd3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


survey_choices = [
    [1, 'Strongly disagree'],
    [2, 'Disagree'],
    [3, 'Neither agree nor disagree'],
    [4, 'Agree'],
    [5, 'Strongly agree'],
]
class Player(BasePlayer):

    sd3_1 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="It's not wise to tell your secrets."
    )

    sd3_2 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I like to use clever manipulation to get my way."
    )

    sd3_3 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="Whatever it takes, you must get the important people on yourside."
    )

    sd3_4 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="Avoid direct conflict with others because they may be useful inthe future."
    )

    sd3_5 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="It’s wise to keep track of information that you can use againstpeople later."
    )

    sd3_6 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="You should wait for the right time to get back at people."
    )

    sd3_7 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="There are things you should hide from other people because they don’t need to know."
    )

    sd3_8 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="Make sure your plans benefit you, not others."
    )

    sd3_9 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="Most people can be manipulated."
    )

    sd3_10 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="People see me as a natural leader."
    )

    sd3_11 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I hate being the center of attention."
    )

    sd3_12 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="Many group activities tend to be dull without me."
    )

    sd3_13 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I know that I am special because everyone keeps telling me so."
    )

    sd3_14 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I like to get acquainted with important people."
    )

    sd3_15 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I feel embarrassed if someone compliments me."
    )

    sd3_16 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I have been compared to famous people."
    )

    sd3_17 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I am an average person."
    )

    sd3_18 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I insist on getting the respect I deserve."
    )

    sd3_19 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I like to get revenge on authorities."
    )

    sd3_20 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I avoid dangerous situations."
    )

    sd3_21 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="Payback needs to be quick and nasty."
    )

    sd3_22 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="People often say I’m out of control."
    )

    sd3_23 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="It’s true that I can be mean to others."
    )

    sd3_24 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="People who mess with me always regret it."
    )

    sd3_25 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I have never gotten into trouble with the law."
    )

    sd3_26 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I enjoy having sex with people I hardly know."
    )

    sd3_27 = models.IntegerField(
        choices=survey_choices, 
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="I’ll say anything to get what I want."
    )




# FUNCTIONS
# PAGES
class Survey(Page):
    form_model = 'player'
    form_fields = [f'sd3_{i}' for i in range(1, 28)]


page_sequence = [Survey,]
