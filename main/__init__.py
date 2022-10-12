from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'main'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # next button delay
    DELAY = 3000

    TREATMENTS = ['facts', 'alt-facts', 'both', 'control']

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

    treatment = models.StringField(doc='one of three options randomly chosen in creating_session function')

    fc1 = models.IntegerField(
        choices=choices,
        label="<b>How persuasive do you find the statement above?</b>"
    )

    fc2 = models.IntegerField(
        choices=choices,
        label="<b>How persuasive do you find the statement above?</b>"
    )

    fc3 = models.IntegerField(
        choices=choices,
        label="<b>How persuasive do you find the statement above?</b>"
    )

    fc4 = models.IntegerField(
        choices=choices,
        label="<b>How persuasive do you find the statement above?</b>"
    )

    afc1 = models.IntegerField(
        choices=choices,
        label="<b>How persuasive do you find this statement?</b>"
    )

    afc2 = models.IntegerField(
        choices=choices,
        label="<b>How persuasive do you find this statement?</b>"
    )

    afc3 = models.IntegerField(
        choices=choices,
        label="<b>How persuasive do you find this statement?</b>"
    )

    afc4 = models.IntegerField(
        choices=choices,
        label="<b>How persuasive do you find this statement?</b>"
    )

    both1_altfact = models.IntegerField(
        choices=choices,
        label="<b>How persuasive do you find this statement?</b>"
    )

    both1 = models.IntegerField(
        choices=choices,
        label="<b>Having read both both the statement and the fact check, how persuasive do you now find the politician’s statement?</b>"
    )

    both2_altfact = models.IntegerField(
        choices=choices,
        label="<b>How persuasive do you find this statement?</b>"
    )

    both2 = models.IntegerField(
        choices=choices,
        label="<b>Having read both both the statement and the fact check, how persuasive do you now find the politician’s statement?</b>"
    )

    both3_altfact = models.IntegerField(
        choices=choices,
        label="<b>How persuasive do you find this statement?</b>"
    )

    both3 = models.IntegerField(
        choices=choices,
        label="<b>Having read both both the statement and the fact check, how persuasive do you now find the politician’s statement?</b>"
    )

    both4_altfact = models.IntegerField(
        choices=choices,
        label="<b>How persuasive do you find this statement?</b>"
    )

    both4 = models.IntegerField(
        choices=choices,
        label="<b>Having read both both the statement and the fact check, how persuasive do you now find the politician’s statement?</b>"
    )

# FUNCTIONS
def creating_session(subsession):
    for player in subsession.get_players():
        player.treatment = random.choice(C.TREATMENTS)
        if player.treatment == 'control':
            player.participant.control = True
        else:
            player.participant.control = False

# PAGES
class InstructionsAF(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'alt-facts'


class InstructionsF(Page):
    
    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'facts'


class InstructionsB(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'both'

# =========================================================

class Fact1(Page):
    form_model='player'
    form_fields=['fc1']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'facts'

class Fact2(Page):
    form_model='player'
    form_fields=['fc2']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'facts'

class Fact3(Page):
    form_model='player'
    form_fields=['fc3']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'facts'

class Fact4(Page):
    form_model='player'
    form_fields=['fc4']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'facts'

# =====================================================

class AFact1(Page):
    form_model='player'
    form_fields=['afc1']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'alt-facts'


class AFact2(Page):
    form_model='player'
    form_fields=['afc2']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'alt-facts'

class AFact3(Page):
    form_model='player'
    form_fields=['afc3']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'alt-facts'

class AFact4(Page):
    form_model='player'
    form_fields=['afc4']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'alt-facts'

# ======================================================

class Both1AF(Page):
    form_model='player'
    form_fields=['both1_altfact']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'both'

class Both1(Page):
    form_model='player'
    form_fields=['both1']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'both'

class Both2AF(Page):
    form_model='player'
    form_fields=['both2_altfact']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'both'


class Both2(Page):
    form_model='player'
    form_fields=['both2']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'both'


class Both3AF(Page):
    form_model='player'
    form_fields=['both3_altfact']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'both'


class Both3(Page):
    form_model='player'
    form_fields=['both3']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'both'


class Both4AF(Page):
    form_model='player'
    form_fields=['both4_altfact']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'both'


class Both4(Page):
    form_model='player'
    form_fields=['both4']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 'both'


page_sequence = [ InstructionsAF, InstructionsF, InstructionsB, Fact1, Fact2, Fact3, Fact4, AFact1, AFact2, AFact3, AFact4, Both1AF, Both1, Both2AF, Both2, Both3AF, Both3, Both4AF, Both4, ]