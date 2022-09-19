import requests
from termcolor import colored
import time


def main():
    liste = open('mail.txt').read().splitlines()
    for email in liste:
        time.sleep(0.5)
        mailcheck(email)


def mailcheck(email):
    api_key = '' # for api key https://isitarealemail.com
    response = requests.get("https://isitarealemail.com/api/email/validate?email=" + email, headers={'Authorization': "Bearer " + api_key })

    status = response.json()['status']

    if status == "valid":
        print(colored("Email is valid : ", "green"), email)





main()
