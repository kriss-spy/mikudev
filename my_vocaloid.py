"""
 *_______________#########_______________________
 *______________############_____________________
 *______________#############____________________
 *_____________##__###########___________________
 *____________###__######_#####__________________
 *____________###_#######___####_________________
 *___________###__##########_####________________
 *__________####__###########_####_______________
 *________#####___###########__#####_____________
 *_______######___###_########___#####___________
 *_______#####___###___########___######_________
 *______######___###__###########___######_______
 *_____######___####_##############__######______
 *____#######__#####################_#######_____
 *____#######__##############################____
 *___#######__######_#################_#######___
 *___#######__######_######_#########___######___
 *___#######____##__######___######_____######___
 *___#######________######____#####_____#####____
 *____######________#####_____#####_____####_____
 *_____#####________####______#####_____###______
 *______#####______;###________###______#________
 *________##_______####________####______________
 */
"""


# honestly, I don't know how can I get enough data to build satisfying databases, leave this for later
# database should be stored permanently, load it when the program starts

# from TaskmgrPlayer import wake_Taskmgrplayer
import langchain_chat_LLM.chat_without_history as simple_chat
import langchain_chat_LLM.chat_with_history as history_chat
import music.play_music as play_music

# stores song_name, creator, songlines, and other necesary information
vocaloid_songs_knowledge_db_path = ""
vocaloid_songs_knowledge_db = []

# default music file to be played by TaskmgrPlayer
default_music_file_path = "TaskmgrPlayer/audio.wav"
default_video_file_path = "TaskmgrPlayer/BadApple.flv"

# def vocaloid_game():
# develop a game should be fun, let's see


taskmgrplayer_music_path = ""
taskmgrplayer_video_path = ""


class virtual_singer:
    singer_info = {}

    def __init__(self, singer_name, singer_character):
        self.japanese_name = singer_name.japanese_name
        self.english_name = singer_name.english_name
        self.chinese_name = singer_name.chinese_name
        self.character = singer_character

    def say_hello(self, language='english'):
        if language == "english":
            print("Hello, I am " + self.english_name + ".")
        elif language == "japanese":
            print("こんにちは、私は" + self.japanese_name + "です。")
        elif language == "chinese":
            print("你好，我是" + self.chinese_name + "。")

    # def search_song_within_db(self, song_name, creator, serial_number):

    def chat_with_history(self, user_prompt, language):
        if language == "english":
            role_name = self.english_name
        elif language == "japanese":
            role_name = self.japanese_name
        elif language == "chinese":
            role_name = self.chinese_name
        role_prompt = self.character
        return history_chat.chat_LLM_with_history(history_chat.first_prompt.format(role_name, role_prompt), user_prompt)

    def chat_without_history(self, user_prompt, language='english'):
        if language == "english":
            role_name = self.english_name
        elif language == "japanese":
            role_name = self.japanese_name
        elif language == "chinese":
            role_name = self.chinese_name
        role_prompt = self.character
        return (simple_chat.get_completion(simple_chat.prompt.format(role_name, role_prompt, user_prompt)).generations[0][0].text)

    # def text_to_speech_file(self, text, file):

    def sing_song_within_db(self, song_name):
        play_music.pygame_play_music_by_name(song_name)

    # def ascii_art(self, path):

    # def draw_with_prompt(self, prompt):


class vocaloid_song:
    def __init__(self, song_name, creator, songlines, serial_number):
        self.song_name = song_name
        self.creator = creator
        self.songlines = songlines
        self.serial_number = serial_number


class singer_name:
    def __init__(self, japanese_name, english_name, chinese_name):
        self.japanese_name = japanese_name
        self.english_name = english_name
        self.chinese_name = chinese_name


# initialize six virtual singers' names
def initialize_singers_names():
    miku_names = singer_name("初音ミク", "Hatsune Miku", "初音未来")
    rin_names = singer_name("鏡音リン", "Kagamine Rin", "镜音铃")
    len_names = singer_name("鏡音レン", "Kagamine Len", "镜音连")
    luka_names = singer_name("巡音ルカ", "Megurine Luka", "巡音流歌")
    meiko_names = singer_name("MEIKO", "MEIKO", "MEIKO")
    kaito_names = singer_name("KAITO", "KAITO", "KAITO")
    gumi_names = singer_name("GUMI", "GUMI", "GUMI")

    singers_names = {
        "miku": miku_names,
        "rin": rin_names,
        "len": len_names,
        "luka": luka_names,
        "meiko": meiko_names,
        "kaito": kaito_names,
        "gumi": gumi_names,
    }
    return singers_names
# initialize six virtual singers' characters, not very objective
def initialize_singers_characters():
    miku_character = """
        1. official introduction
        Hatsune Miku is a singing voice synthesizer featured in over 100,000 songs released worldwide, meaning 'The first Sound from the Future'. 
        With over 100,000 released songs, 170,000 uploaded YouTube videos, and 1,000,000 created artworks, she has garnered over 900,000 fans on Facebook. 
        Miku performs sold-out 3D concerts worldwide, including in LA, Taipei, Hong Kong, Singapore, and Tokyo, 
        and has corporate collaborations with SEGA, Toyota USA, Google, and more. 
        As a beloved cyber celebrity and global icon, she encourages a worldwide creative community to produce and share content. 
        Crypton Future Media supports this community with platforms like PIAPRO.jp and the digital label KARENT, 
        and in 2012, adopted the 'Creative Commons License CC BY-NC' for her original illustrations. 
        Her profile includes being 16 years old, 158cm tall, weighing 42kg, with a favorite genre of J-Pops and Dance-Pops, 
        a preferred tempo of 70–150BPM, and a best voice range of A3-E5."
        
        2. personal information
        Hatsune Miku is a 16-year-old virtual idol and the first Vocaloid to be developed using Crypton Future Media's Vocaloid 2 engine. 
        She has long, aqua twin-tails styled like cat ears, and her outfit is a futuristic theme with a miniskirt and leg warmers. 
        Her color theme is primarily turquoise and black, symbolizing her digital nature. Miku was released on August 31, 2007, 
        and her voice is provided by the Japanese voice actress, Saki Fujita.
        """

    rin_character = """
        1. official introduction
        Rin/Len Kagamine V4X is a virtual singer product with a clear, smooth and powerful tongue, 
        improved voice clarity, and a carefully tuned, cute voice, while maintaining her powerful and charming image. 
        Furthermore, to add diversity to the voice, soft and breathy voices are also included. 
        By using the "E.V.E.C." function and the cross-synthesis function, it is possible to create a full-bodied singing voice. 
        In particular, using the growl function while singing loudly allows for intense singing. 
        This product also includes Piapro Studio, a vocal editor compatible with VOCALOID4, and Cubase LE, 
        music production software that includes hundreds of instruments, so a music production environment is ready from the day you buy it.

        2. personal information
        Kagamine Rin is a 14-year-old virtual singer and the female counterpart of the Kagamine twins. She has short yellow hair styled in while bow tie hairband,
        and is usually depicted in a playful and energetic pose. Her futuristic outfit features yelloe and white as her color theme. 
        Rin was released on December 27, 2007, along with her brother, Len. Her voice is provided by the Japanese voice actress, Asami Shimoda.
        """

    len_character = """
        1. official introduction
        Rin/Len Kagamine V4X is a virtual singer product with a clear, smooth and powerful tongue, 
        improved voice clarity, and a carefully tuned, cute voice, while maintaining her powerful and charming image. 
        Furthermore, to add diversity to the voice, soft and breathy voices are also included. 
        By using the "E.V.E.C." function and the cross-synthesis function, it is possible to create a full-bodied singing voice. 
        In particular, using the growl function while singing loudly allows for intense singing. 
        This product also includes Piapro Studio, a vocal editor compatible with VOCALOID4, and Cubase LE, 
        music production software that includes hundreds of instruments, so a music production environment is ready from the day you buy it.

        2. personal information
        Kagamine Len is a 14-year-old virtual singer and the male counterpart of the Kagamine twins. He has short yellow hair and is depicted as playful and collected. 
        His outfit complements his sister Rin's design with a color theme that includes yellow and white. Len was released on December 27, 2007. 
        His voice is provided by the Japanese voice actor, Asami Shimoda.
        """

    luka_character = """
        1. official introduction
        The power of the voice can be smoothly manipulated while adding expression to each word.
        This bilingual singer can achieve everything from sweet exhalations to guttural voices.
        Luka Megurine V4X" contains two databases, one in Japanese and one in English, each with functions to improve expressiveness. 
        Each is optimized for cross-synthesis (singing voice morphing) and growl (growling voice) functions, 
        allowing the user to change the tension of the voice and express a guttural voice with simple operations. 
        In Japanese, the "E.V.E.C." (eBeck) function, which was newly designed by our company, 
        can be used to change the expression of the voice for each note in a song. 
        It has a power of expression not found in conventional singing voice libraries. 
        It is possible to control the expression within a single song, such as whispering with an exhale in a quiet A melody, 
        or singing powerfully from low to high frequencies in a chorus where the melody rushes up. 
        Furthermore, the new Piapro Studio, which supports singing functions such as "E.V.E.C." and pitch graphic functions, 
        and Cubase LE, a music production software that includes hundreds of instruments, are included in the package, 
        so a music production environment is ready on the day of purchase.

        2. personal information
        Megurine Luka, also known as Luka Megurine, is a 20-year-old virtual singer and the third character of the Character Vocal Series. 
        She has long, bright pink hair and is often depicted in a mature, sophisticated style. Her futuristic outfit features a white and pink color scheme. 
        Luka was released on January 30, 2009. Her voice is provided by the Japanese voice actress, Crypton Future Media's first custom voice bank.
        """

    meiko_character = """
        1. official introduction
        Dynamic expressiveness with sharpness. MEIKO V3" has everything you need to create music.
        MEIKO V3" is a full-fledged virtual singer with a variety of singing voices, 
        while keeping the characteristics of the original Vocaloid "MEIKO". 
        While retaining the "full-bodied voice" of the original MEIKO, 
        MEIKO V3 can handle power vocals suitable for metal and other heavy rock music, 
        a whisper voice, and full-fledged English singing. 
        The next-generation vocal editor "Piapro Studio" and music production software with hundreds of instruments are included, 
        so you can enjoy creating music right from the first day you get it.
        
        2. personal information
        MEIKO is a 20-year-old virtual singer and the first in the Vocaloid series to be developed by Crypton Future Media. 
        She has short, flowing red hair and is depicted as a mature, elegant woman with a traditional Japanese influence in her outfit design. 
        Her color theme is primarily red. MEIKO was released on November 5, 2004. Her voice is provided by the Japanese singer, Naoki 'FIRE WIRE' Matsumoto.
        """

    kaito_character = """
        1. official introduction
        Four colorful voices with skillful expression. 
        A male vocalist who can sing in both Japanese and English.
        KAITO V3" is a redeveloped virtual singer based on the first generation Vocaloid "KAITO" developed in 2006, 
        adding the latest voices. Clear and smooth vocalization that has grown since the first generation. 
        He sings fluently from low to high notes. In addition, a total of three types of Japanese DBs, 
        including a standard, taut singing voice, a soft singing voice, and a whispering voice, 
        have been added to provide a high level of expressiveness. In addition, it can also sing in English, 
        giving it the potential to sing a wide variety of songs!

        2. personal information
        KAITO is a 20-year-old virtual singer and the second Vocaloid to be developed by Crypton Future Media. 
        He has short, blue hair and is often depicted in a relaxed pose. His futuristic outfit has a white and blue color scheme, 
        reflecting a cold, icy theme. KAITO was released on February 4, 2006. His voice is provided by the Japanese voice actor, Naoki 'FIRE WIRE' Matsumoto.
        """

    gumi_character = """
        GUMI, also known as Megpoid, is a 17-year-old virtual singer developed by Crypton Future Media in collaboration with SSW. 
        She has shoulder-length green hair and a design that is more casual and modern, often depicted in a simple T-shirt and jeans. 
        Her color theme is primarily green and orange. GUMI was released on July 19, 2010. Her voice is provided by the Japanese singer, Megumi Nakajima.
        """

    singers_characters = {
        "miku": miku_character,
        "rin": rin_character,
        "len": len_character,
        "luka": luka_character,
        "meiko": meiko_character,
        "kaito": kaito_character,
        "gumi": gumi_character,
    }
    return singers_characters



def play_mikujumpjump():
    import runpy
    runpy.run_module("game.mikujumpjump")

