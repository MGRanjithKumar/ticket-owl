# Ticket Owl

*An alternate explaination of how to use this can be found on my website [here](https://www.fernandomc.com/posts/ticket-owl-tool-check-website-changes/)*

Let's say you want to see when some arbitrary text appears or dissapears from a website and be notified via email or text.

Maybe you need to:

- Check if your favorite musican has opened ticket sales for their next show
- Monitor some webpage and check for certain text
- See if a webpage has changed from a previous version and be notified of the differences (a feature in development)

Whatever the case, you want an easy way run these checks and be notified via a text message or email depending on the results. You can do this easily with Ticket Owl. Ticket Owl is a project written in Python3 that relies on the [Serverless Framework](https://www.serverless.com) and [AWS](https://aws.amazon.com) to run periodic jobs to check for various conditions on websites.

Ticket Owl can run jobs defined in a `jobs.py` configuration file or you can write your own custom logic using provided helpers.

What I'll assume you already have installed:
1. An AWS Account
2. The Serverless Framework

Here's how to start using Ticket Owl:
1. Clone the repo: `git clone https://github.com/fernando-mc/ticket-owl.git`
2. Either write your own alert processes in `index.py` using the helpers in `helpers.py` OR write some jobs in jobs.py 
3. Optionally change the `schedule: rate(5 minutes)` in the `serverless.yml` file to to any aws [schedule expression](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html). This will allow you to determine how frequently you want to check on the website you're interested in.
4. Optionally change the `timeout: 6` value from 6 to a larger number if you are running many jobs 
5. Optionally [verify an SES email](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses-procedure.html) in AWS if you want to use the email alerts feature
6. Deploy your service to aws with `sls deploy`