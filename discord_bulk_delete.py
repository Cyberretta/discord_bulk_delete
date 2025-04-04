import requests
import time

USERNAME = "" # Your username. It is used to find your messages in the conversation in order to delete them. (Not your "Display name" but your real username)
CHANNEL_ID = "" # The channel ID of the channel in which you want to delete your messages.
AUTHORIZATION_TOKEN = "" # Your authorization token

headers = {
    "Authorization": AUTHORIZATION_TOKEN
}

def get_messages_list(before = ""):
    response = ""
    if before == "":
        response = requests.get(f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages?limit=100", headers=headers)
    else:
        response = requests.get(f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages?before={before}&limit=100", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("[-] Error while retrieving messages :")
        print(response.text)
        exit()

def delete_message(id):
    print(f"[i] Deleting {id}")
    response = requests.delete(f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages/{id}", headers=headers)
    if response.status_code != 204:
        print(f"[-] Failed to delete {id}")
        print(response.text)
    return response.status_code

def delete_messages(msg_list):
    for message in msg_list:
        if message["type"] == 0 and message["author"]["username"] == USERNAME:
            time.sleep(1)
            response_code = delete_message(message["id"])
            while(response_code == 429):
                time.sleep(5)
                response_code = delete_message(message["id"])
    return

if __name__ == "__main__":
    before = ""
    while True:
        msg_list = get_messages_list(before)
        if len(msg_list) == 0:
            print("[+] Reached start of conversation. All your messages should have been deleted from the conversation ! Exiting.")
            exit()
        time.sleep(1)
        delete_messages(msg_list)
        before = msg_list[-1]["id"]