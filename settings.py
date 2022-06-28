from os import environ


SESSION_CONFIGS = [
    dict(
        name='full_experiment', app_sequence=['main', 'voting_preferences', 'big_five', 'sd3', 'political_survey', 'demographics'],
        num_demo_participants=1,
    ),
    dict(
        name='political_survey', app_sequence=['political_survey', 'payment_info'], num_demo_participants=1
    ),
    dict(
        name='big_five', app_sequence=['big_five', 'payment_info'], num_demo_participants=1
    ),
    dict(
        name='sd3', app_sequence=['sd3', 'payment_info'], num_demo_participants=1
    ),
    dict(
        name='main', app_sequence=['main'], num_demo_participants=1,
    ),
    dict(
        name='voting_preferences', app_sequence=['voting_preferences',], num_demo_participants=1,
    ),
    dict(
        name='demographics', app_sequence=['demographics'], num_demo_participants=1,
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '5925258192968'

INSTALLED_APPS = ['otree']
