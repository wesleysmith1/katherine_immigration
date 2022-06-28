from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


num_choices = [0,1,2,3,4,5,6,7,8,9,10]
class Player(BasePlayer):
    age = models.IntegerField(label='What is your age?')

    gender = models.StringField(
        label='What is your gender?', 
        choices=['Female', 'Male', 'Other', 'Prefer not to answer',],
    )

    race = models.StringField(
        label='What is your race?',
        choices=['Asian', 'Black/African American', 'White or Caucasian', 'Native American', 'Multiracial', 'Other', 'Prefer not to answer']
    )

    marital_status = models.StringField(
        label='What is your marital status?',
        choices=['Married', 'Single', 'Divorced', 'Widowed', 'Other', 'Prefer not to answer']
    )

    birth_order = models.StringField(
        label='What is your birth order?',
        choices=['The only child', 'Oldest child in the family', 'Youngest child in the family', 'Middle child', 'Prefer not to say', ]
    )

    religion = models.StringField(
        label='What is your religious affiliation?',
        choices=['Atheism', 'Buddhism', 'Christianity', 'Hinduism', 'Islam', 'Judaism', 'Nonreligious or Agnostic other', 'Prefer no to answer']
    )

    risk_willingness = models.IntegerField(
        label="How do you see yourself: are you a person who is generally willing to take risks, or do you try to avoid taking risks? Please use a scale from 0 to 10, where a 0 means you are “completely unwilling to take risks” and a 10 means you are “very willing to take risks”. You can also use the values in-between to indicate where you fall on the scale.",
        choices=num_choices,
        widget=widgets.RadioSelectHorizontal,
    )

    others_intentions  = models.IntegerField(
        label="How well does the following statement describe you as a person? As long as I'm not convinced otherwise, I assume that people have only the best intentions. Please use a scale from 0 - 10, where 0 means 'does not describe me at all' and a 10 means you are 'describes me perfectly'.",
        choices=num_choices,
        widget=widgets.RadioSelectHorizontal,
    )

    willingness_to_share = models.IntegerField(
        label="How do you assess your willingness to share with others without expecting anything in return when it comes to charity? Please use a scale from 0 to 10, where 0 means you are 'completely unwilling to share' and a 10 means you are 'very willing to share'. You can also use the values in- between to indicate where you fall on the scale.",
        choices=num_choices,
        widget=widgets.RadioSelectHorizontal,
    )

    willingness_to_punish = models.IntegerField(
        label="How do you see yourself: Are you a person who is generally willing to punish unfair behavior even if this is costly? Please use a scale from 0 to 10, where 0 means you are “not willing at all to incur costs to punish unfair behavior” and a 10 means you are “very willing to incur costs to punish unfair behavior”. You can also use the values in-between to indicate where you fall on the scale.",
        choices=num_choices,
        widget=widgets.RadioSelectHorizontal,
    )

    feedback = models.StringField(blank=True)


# FUNCTIONS
# PAGES
class Survey(Page):
    form_model = 'player'
    form_fields = [
        'gender', 
        'race', 
        'marital_status', 
        'birth_order', 
        'religion', 
        'risk_willingness', 
        'others_intentions', 
        'willingness_to_share', 
        'willingness_to_punish',
        'feedback',
    ]


page_sequence = [Survey]