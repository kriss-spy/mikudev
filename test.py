import my_vocaloid as vcld

# from TaskmgrPlayer import wake_Taskmgrplayer
import sys
import ctypes
import music.play_music as play_music

using_name = "miku"
using_language = "english"

singers_names = vcld.initialize_singers_names()
singers_characters = vcld.initialize_singers_characters()

miku = vcld.virtual_singer(singers_names[using_name], singers_characters[using_name])

# print(miku.chat_without_history("おはよう", "japanese"))

# print(miku.chat_with_history("ryoの「メルト」という曲を知っていますか？?", "japanese"))
# print(miku.chat_with_history("作曲家について教えてください", "japanese"))
# the chat_with_history must use database(currently empty), not very satisfying
# there is language problem, the character setting is only english, so the japanese chat is not very good

# exit()

# wake_Taskmgrplayer.load_resources("original")
# with open("TaskmgrPlayer/version.txt", "r") as f:
#     print(f.read())
# # time.sleep(1)

# wake_Taskmgrplayer.load_resources("original")


# if wake_Taskmgrplayer.is_admin():
#     wake_Taskmgrplayer.wake_and_play()
# else:
#     # 以管理员权限重新运行程序

#     ctypes.windll.shell32.ShellExecuteW(
#         None, "runas", sys.executable, __file__, None, 1
#     )


# vcld.play_mikujumpjump()

play_music.console_music_play()

miku.sing_song_within_db("砂の惑星")
