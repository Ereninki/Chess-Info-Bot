import os
from dotenv import load_dotenv
load_dotenv()
import requests
from random import randint
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
    except Exception as e:
        respond("Sorry, but i cant find this chess player, maybe the username is wrong? :hs:")
        return

    chess_user_data = chess_api_response.json()

    try:
        country_api_response = requests.get(chess_user_data["country"], headers=headers)
        country_api_response.raise_for_status()
    except Exception as e:
        print(f"country error : {e}")
        respond("Sorry but there's an error when finding the user's country, pls try again in a few seconds :pls:")
    
    country_api_json = country_api_response.json()
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
                    "text": f"*Country:* {country_api_json["name"]}\n*User link:* <{chess_user_data["url"]}|{username}>\n*Username:* {chess_user_data["username"]}\n*Streamer:* {chess_user_data["is_streamer"]}\n*League:* {chess_user_data["league"]}\n*Followers:* {chess_user_data["followers"]}\n*User ID:* {chess_user_data["player_id"]}\n*Status:* {chess_user_data["status"]}"
                }
            ]
        }
    ]
    respond(blocks=blocks)

@app.command("/chess-title")
def chess_titles(ack, respond, command):
    ack()

    title = str(command["text"]).upper()
    try:
        chess_titles_response = requests.get(f"https://api.chess.com/pub/titled/{title}", headers=headers)
        chess_titles_response.raise_for_status()
    except Exception as e:
        print(f"titles, probably a 404 error: {e}")
        respond("sorry, i think you entered a wrong title.. pls use only this 'GM, WGM, IM, WIM, FM, WFM, NM, WNM, CM, WCM' thxx :cat-heart:")
        return

    chess_titles_json = chess_titles_response.json()

    ten_players_title = []

    for a in range(10):
        random_player_number = randint(0, len(chess_titles_json["players"]))
        ten_players_title.append(chess_titles_json["players"][random_player_number])

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"RANDOM 10 PLAYERS FROM '{title}' TITLE :chess-brilliant:",
                "emoji": True
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f" \n".join(ten_players_title)
                }
            ]
        }
    ]
    respond(blocks=blocks)

@app.command("/chess-random-puzzle")
def random_puzzle(ack, command, respond):
    ack()

    try:
        random_puzzle_response = requests.get("https://api.chess.com/pub/puzzle/random", headers=headers)
        random_puzzle_response.raise_for_status()
    except Exception as e:
        print(f"puzzle error: {e}")
        respond("sorry, there was an error, pls try again in a few seconds!!")

    random_puzzle_json = random_puzzle_response.json()

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Random Puzzle: {random_puzzle_json["title"]}",
                "emoji": True
            }
        },
        {
            "type": "image",
            "image_url": random_puzzle_json["image"],
            "alt_text": "random puzzle image from chess.com"
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"Name: {random_puzzle_json["title"]}\nURL: {random_puzzle_json["url"]}"
                }
            ]
        }
    ]
    respond(blocks=blocks)

@app.event("app_mention")
def app_mention(say, body):
    say("Haii :hii: do you need smth? (i have slash commands that you can use!!)")


print("Your app is starting...")
handler = SocketModeHandler(app, os.getenv("APP_TOKEN"))
handler.start()