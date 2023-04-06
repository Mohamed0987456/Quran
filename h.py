from pyrogram import Client

api_id = 19530787
api_hash = "b9d5bec9d22501ee256ba9cee556cae7"
bot_token = "6122474506:AAFCP68Xm6PoMXz6Nn0zGtUz6_HR5068BVY"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

app.run()
