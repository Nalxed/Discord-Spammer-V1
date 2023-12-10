import requests
import time
import sys

# Prompt the user for authorization token and channel ID
authorization_token = input("Enter your Discord authorization token: ")
print(f"Token entered: {authorization_token}")


# Ask for confirmation
confirmation = input("Is this the correct token? (y/n): ")
if confirmation.lower() != 'y':
    print("Token confirmation failed. Exiting.")
    sys.exit()

channel_id = input("Enter the channel ID where you want to spam: ")

# Ask the user for the message to send
spam_message = input("Enter the message to spam: ")

payload = {'content': spam_message}

header1 = {
    'authorization': authorization_token
}

# Variable to keep track of the spam count
spam_count = 0

def click():
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=header1)
    # Optionally, print the response for debugging
    # print(r.text)

def spam():
    global spam_count  # Declare spam_count as a global variable
    click()
    spam_count += 1
    print(f"\rMessages sent: {spam_count}", end='', flush=True)  # Print on the same line
    time.sleep(0.031)  # Sleep for 31 milliseconds
    spam()  # Call the function again for continuous spamming

def start_spam():
    response = input("Do you want to start the spamming? (y/n): ")
    if response.lower() == 'y':
        spam()

start_spam()
