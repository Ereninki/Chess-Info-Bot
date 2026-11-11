# Chess-Info Bot

This is a slack bot that gives information about **chess.com players**, **random puzzles** and **random players** who has titles!!!

# Tech Stack

- **Python programming language**
- **uv** library manager
- **slack_bolt** library for making a slack bot alive
- **request** library for getting information from the web

---

# Usage

This slack bot has 3 slash commands, **/chess-player < chess.com username >**, **/chess-title < GM, WGM, IM, WIM, FM, WFM, NM, WNM, CM, WCM (use one of these for command to work!)>** and **/chess-random-puzzle** in this [slack channel!!](https://hackclub.enterprise.slack.com/archives/C0CFALTELDV)

---

The **/chess-player < chess.com username >** command gives you information about a chess.com player with the username you typed

**example:** /chess-player MagnusCarlsen
![image](https://cdn.hackclub.com/01a1cc59-99ab-793d-836d-ba500f30c0ab/image%20(2).png)

---

The **/chess-title** command shows you 10 random player from the chess title you selected (btw the chess titles are GM, WGM, IM, WIM, FM, WFM, NM, WNM, CM, WCM if you didnt know..)

**example**: /chess-title GM
![image](https://cdn.hackclub.com/01a1cc61-0fbe-7293-883f-bd47653b0cb3/image%20(3).png)

---

The **/chess-random-puzzle** command is just giving you information about a random puzzle in chess.com

**example:** /chess-random-puzzle
![image](https://cdn.hackclub.com/01a1ccb2-8227-7017-9c4d-5bb7eb6d7f48/image%20(4).png)

---

# How to host one on your computer?

Well, you just need to install [uv](https://github.com/astral-sh/uv), clone this repo with `git clone https://github.com/Ereninki/Chess-Info-Bot`, replace the **values** in the **.env.example** and **remove** the **.example** from the file name and finally running `uv run ./main.py` in the root folder of the repo will make the bot alive!!