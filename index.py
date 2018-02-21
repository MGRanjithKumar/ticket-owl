import helpers
from jobs import JOBS

def handler(event, context):
    # Run all the configured jobs and alerts
    helpers.run_jobs(JOBS)
    # Run a custom set of alerts with the provided helpers
    my_url = 'https://www.tickets.com/event/123123'  # This isn't a real check
    my_message = 'That ticket you wanted is now on sale! https://www.tickets.com/event/123123'
    if helpers.contains_text('On sale now', my_url):
        helpers.send_email('fernando@some-ses-verified-email.com', 'Your tickets are on sale!', my_message)
        helpers.send_sms('+1555777888#', my_message)