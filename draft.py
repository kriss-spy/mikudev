import os, dotenv
_ = dotenv.load_dotenv(dotenv.find_dotenv(usecwd=True))

from my_vocaloid import virtual_singer, initialize_singers_characters, initialize_singers_names

singers_characters = initialize_singers_characters()
singers_names = initialize_singers_names()
miku = virtual_singer(singers_names["miku"], singers_characters["miku"])
miku.say_hello()
print(miku.chat_without_history("hello", "english"))
# print(miku.chat_without_history("hello", "english"))
