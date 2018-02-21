JOBS = [
    # Details of format:
    # {
    #     'url': 'aURL',  # required
    #     'value_to_check': 'a text value to check',  # required
    #     'checker': 'which checker function to use',  # required
    #     'alerts': ['which type(s) of alert', 'to run'], # required
    #     'message': 'a message to send as an alert',  # required
    #     'subject': 'an email subject line',  # optional
    #     'verified_email': 'an SMS-verfied email',  # optional
    #     'phone_number': 'a number with this format: +15555555555'  # optional
    # },
    #
    # Example:
    {
        'url': 'https://www.myticketsite.com/event/123123',
        'value_to_check': 'Feb 10',
        'checker': 'contains_text',
        'alerts': ['email', 'sms'],
        'message': 'The ticket for Feb 10 is now on sale! - https://www.myticketsite.com/event/123123',
        'subject': 'Ticket Owl Alert',
        'verified_email': 'fernando@a-verfied-email.com',
        'phone_number': '+1555666777#'
    }
]
