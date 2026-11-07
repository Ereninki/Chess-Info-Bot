import os
from dotenv import load_dotenv
load_dotenv()
import requests
from requests.exceptions import HTTPError
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.getenv("BOT_TOKEN"))

headers = {"User-Agent": "Mozilla/5.0"}

@app.command("/chess-player")
def player_info(ack, respond, command):
    ack()

    username = command["text"]
    try:
        chess_api_response = requests.get(f"https://api.chess.com/pub/player/{username}", headers=headers)
        chess_api_response.raise_for_status()
    except HTTPError as e:
        if e.response.status_code == 404:
            print(f"user cant found.. {e}")
            respond("Sorry, but i cant find this chess player, maybe the username is wrong? :hs:")
        else:
            print(f"error: {e}")
            respond("Sorry but there's an error, please retry in a few seconds")
            return

    chess_user_data = chess_api_response.json()
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"{username}'s CHESS.COM DETAILS :chess_pawn:",
                "emoji": True
            }
        },
        {
            "type": "image",
            "image_url": chess_user_data["avatar"],
            "alt_text": f"{username}'s avatar"
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "test"
                }
            ]
        }
    ]
    respond(blocks=blocks)

@app.event("app_mention")
def app_mention(say, body):
    say("Haii :hii: do you need smth? (i have slash commands that you can use!!)")

if __name__ == "__main__":
    print("Your app is starting...")
    handler = SocketModeHandler(app, os.getenv("APP_TOKEN"))
    handler.start()