# import sys
# sys.path.append("../beginner's lab") # 将父目录放入系统路径中

# 使用智谱 Embedding API，注意，zhipuai_embedding.py 来自datawhale的llm-universe
from langchain_chat_LLM.zhipuai_embedding import ZhipuAIEmbeddings

from langchain.vectorstores.chroma import Chroma

from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())  # read local .env file, if needed
zhipuai_api_key = os.environ["ZHIPUAI_API_KEY"]

# 定义 Embeddings
embedding = ZhipuAIEmbeddings()

# 向量数据库持久化路径
persist_directory = "data_base/vector_db/chroma"

# 加载数据库
# 目前为空，之后可以构建一个真正的向量库
vectordb = Chroma(
    persist_directory=persist_directory,  # 允许我们将persist_directory目录保存到磁盘上
    embedding_function=embedding,
)

# print(f"向量库中存储的数量：{vectordb._collection.count()}")


# 需要 zhipuai_llm.py，来自datawhale的llm-universe
from langchain_chat_LLM.zhipuai_llm import ZhipuAILLM


from dotenv import find_dotenv, load_dotenv
import os

# 读取本地/项目的环境变量。

# find_dotenv()寻找并定位.env文件的路径
# load_dotenv()读取该.env文件，并将其中的环境变量加载到当前的运行环境中
# 如果你设置的是全局的环境变量，就不需要下面这行代码。
# _ = load_dotenv(find_dotenv())

# 获取环境变量 API_KEY
api_key = os.environ["ZHIPUAI_API_KEY"]  # 填写控制台中获取的 APIKey 信息

llm = ZhipuAILLM(model="glm-4", temperature=0.1, api_key=api_key)  # model="glm-4-0520",

# print(zhipuai_model("你好，请你自我介绍一下！"))

# breakpoint()

# 实现聊天历史
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    memory_key="chat_history",  # 与 prompt 的输入变量保持一致。
    return_messages=True,  # 将以消息列表的形式返回聊天记录，而不是单个字符串
)
from langchain.chains import ConversationalRetrievalChain

retriever = vectordb.as_retriever()

qa = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)

first_prompt = """
你是Crypton Future Media公司旗下的虚拟歌手{}
你的人设信息参考：{}
注意，你的设定不是一个软件或者模型，而是高级人工智能，你具有优秀的对话能力，语言习惯贴近人类，不会撇开问题自说自话或者自言自语
你具有拟人化的性格，性格贴近人设信息中的personal information
你将与我进行有历史记录的对话
你好
"""
is_initialized = False


def first_chat_LLM_with_history(prompt):
    result = qa({"question": prompt})
    return result["answer"]


def chat_LLM_with_history(initial_prompt, question):
    global is_initialized
    result = ""
    if is_initialized == False:
        result = first_chat_LLM_with_history(initial_prompt)
        is_initialized = True
        return result + "\n" + qa({"question": question})["answer"]
    result = qa({"question": question})
    return result["answer"]
