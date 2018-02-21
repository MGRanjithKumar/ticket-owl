import urllib.request
import boto3


def get_page_text(url):
    """Helper function to grab page text"""
    return urllib.request.urlopen(url).read().decode('utf-8')


def contains_text(value_to_check, url):
    """Function to check if a page contains the given value"""
    if str(value_to_check) in get_page_text(url):
        return True


def lacks_text(value_to_check, url):
    """Function to check if a page doesn't contain the given value"""
    if str(value_to_check) not in get_page_text(url):
        return True

# def site_changed(url):
#    """Checks against a previous version of the site text stored in AWS S3"""
#    # Create custom bucket if not exists
#       # (store bucket name in SLS config?)
#    # Fetch bucket contents looking for hash of url as key name (somehash.txt)
#    # If no file for url exits (know this by checking for hash)
#       # save website text in s3 and create key with hash --> somehash.txt
#    # If file exists, get it and then download and compare to current site


def send_email(verified_email, subject, message):
    ses = boto3.client('ses')
    ses.send_email(
            Source=verified_email,
            Destination={'ToAddresses': [verified_email]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': message}}
            },
            ReplyToAddresses=[verified_email]
        )


def send_sms(cell_number, message):
    sns = boto3.client('sns')
    sns.publish(
        PhoneNumber=cell_number,  # format must be '+15555555555'
        Message=message
    )


# Checker functions
CHECKERS = {
    'contains_text': contains_text,
    'lacks_text': lacks_text
}

ALERTS = {
    'email': send_email,
    'sms': send_sms,
    'text': send_sms
}


def run_jobs(job_dict):
    for job in job_dict:
        check_result = CHECKERS[job['checker']](job['value_to_check'], job['url'])
        if check_result is True:
            for alert in job['alerts']:
                if alert == 'email':
                    ALERTS[alert](job['verified_email'], job['subject'], job['message'])
                if alert in ['sms', 'text']:
                    ALERTS[alert](job['phone_number'], job['message'])
