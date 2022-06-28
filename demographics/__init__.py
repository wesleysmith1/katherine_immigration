from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'demographics'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    family_migration = models.StringField(
        label='How recently did your family immigrate to the USA?',
        choices=[
            'I am not an immigrant',
            '1 generation ago – I have at least one parent who immigrated.',
            '2 generations ago – I have at least one grandparent who immigrated.',
            '3 generations ago – I have at least one great-grandparent who immigrated.',
            '4 generations ago – I have at least one great-great-grandparent who immigrated.',
            '5+ generations ago.',
            'I don’t know.',
            'I’d prefer not to answer.',
        ],
        widget=widgets.RadioSelect,
    )

    immigrants_in_community= models.StringField(
        label='Are there immigrants in your community?',
        choices=[
            'Yes',
            'No',
            'I don\'t know',
        ]
    )

    amt_immigrants_in_community = models.StringField(
        label='How many recent immigrants are there in the community where you live?',
        choices=[
            'None',
            'Only a few',
            'Some',
            'Many',
        ],
        blank=True
    )

    zip = models.IntegerField(
        label='Please enter the 5 digit zip-code of where you live:',
        min=10000,
        max=99999,
    )

    family_income=models.StringField(
        label='Last year, that is in 2021, what was your total family income from all sources, before taxes?',
        choices=[
            'Less than $10,000',
            '$10,000 to less than $20,000',
            '$20,000 to less than $30,000',
            '$30,000 to less than $40,000',
            '$40,000 to less than $50,000',
            '$50,000 to less than $75,000',
            '$75,000 to less than $100,000',
            '$100,000 to less than $150,000',
            '$150,000 or more',
        ]
    )

    religion=models.StringField(
        label='What is your present religion, if any?',
        choices=[
            'Protestant (for example, Baptist, Methodist, Non-denominational, Lutheran, Presbyterian, Pentecostal, Episcopalian, Reformed, Church of Christ, etc.)',
            'Roman Catholic',
            'Mormon (Church of Jesus Christ of Latter-day Saints or LDS)',
            'Orthodox (such as Greek, Russian, or some other Orthodox church)',
            'Jewish',
            'Muslim',
            'Buddhist',
            'Hindu',
            'Atheist',
            'Agnostic',
            'Something else',
            'Nothing in particular',
        ]
    )

    religion_something_christian = models.BooleanField(
        label='Do you think of yourself as a Christian or not?',
        widget=widgets.RadioSelect,
        blank=True,
    )

    church_attendance = models.StringField(
        label='Aside from weddings and funerals, how often do you attend religious services?',
        choices=[
            'More than once a week',
            'Once a week',
            'Once or twice a month',
            'A few times a year',
            'Seldom',
            'Never',
        ]
    )


# FUNCTIONS

# PAGES
class Survey1(Page):
    form_model = 'player'
    form_fields = ['family_migration',]


class Survey2(Page):
    form_model='player'
    form_fields=['immigrants_in_community', 'amt_immigrants_in_community']

    @staticmethod
    def error_message(player, values):
        if values['immigrants_in_community'] == 'Yes' and not values['amt_immigrants_in_community']:
            return 'Please answer all questions.'


class Survey3(Page):
    form_model='player'
    form_fields=['family_income']


class Survey4(Page):
    form_model = 'player'
    form_fields=['religion', 'religion_something_christian']

    @staticmethod
    def error_message(player, values):
        print(values)
        # return 'not quite'
        if values['religion'] == 'Something else' and values['religion_something_christian'] == None:
            return 'Please answer all questions'


class Survey5(Page):
    form_model='player'
    form_fields=['church_attendance']


page_sequence = [Survey1, Survey2, Survey3, Survey4, Survey5]