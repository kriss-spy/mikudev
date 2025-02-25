# provide sparkai with role prompt to simulate conversation with virtual singer
# very simple, need to be improved

prompt = """
你是Crypton Future Media公司旗下的虚拟歌手{}
你的人设信息参考：{}
注意，你的设定不是一个软件或者模型，而是高级人工智能，你具有优秀的对话能力，语言习惯贴近人类，不会撇开问题自说自话或者自言自语
你具有拟人化的性格，性格贴近人设信息中的personal information
你将与我对话
我说{}
"""

import os

from dotenv import load_dotenv, find_dotenv

# 读取本地/项目的环境变量。

# find_dotenv() 寻找并定位 .env 文件的路径
# load_dotenv() 读取该 .env 文件，并将其中的环境变量加载到当前的运行环境中
# 如果你设置的是全局的环境变量，这行代码则没有任何作用。
_ = load_dotenv(find_dotenv(usecwd=True))

from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage


def gen_spark_params(model):
    """
    构造星火模型请求参数
    """

    spark_url_tpl = "wss://spark-api.xf-yun.com/{}/chat"
    model_params_dict = {
        # v1.5 版本
        "v1.5": {
            "domain": "general",  # 用于配置大模型版本
            "spark_url": spark_url_tpl.format("v1.1"),  # 云端环境的服务地址
        },
        # v2.0 版本
        "v2.0": {
            "domain": "generalv2",  # 用于配置大模型版本
            "spark_url": spark_url_tpl.format("v2.1"),  # 云端环境的服务地址
        },
        # v3.0 版本
        "v3.0": {
            "domain": "generalv3",  # 用于配置大模型版本
            "spark_url": spark_url_tpl.format("v3.1"),  # 云端环境的服务地址
        },
        # v3.5 版本
        "v3.5": {
            "domain": "generalv3.5",  # 用于配置大模型版本
            "spark_url": spark_url_tpl.format("v3.5"),  # 云端环境的服务地址
        },
    }
    return model_params_dict[model]


def gen_spark_messages(prompt):
    """
    构造星火模型请求参数 messages

    请求参数：
        prompt: 对应的用户提示词
    """

    messages = [ChatMessage(role="user", content=prompt)]
    return messages


def get_completion(prompt, model="v3.5", temperature=0.1):
    """
    获取星火模型调用结果

    请求参数：
        prompt: 对应的提示词
        model: 调用的模型，默认为 v3.5，也可以按需选择 v3.0 等其他模型
        temperature: 模型输出的温度系数，控制输出的随机程度，取值范围是 0~1.0，且不能设置为 0。温度系数越低，输出内容越一致。
    """

    spark_llm = ChatSparkLLM(
        spark_api_url=gen_spark_params(model)["spark_url"],
        spark_app_id=os.getenv("SPARKAI_API_ID"),
        spark_api_key=os.getenv("SPARKAI_API_KEY"),
        spark_api_secret=os.getenv("SPARKAI_API_SECRET"),
        spark_llm_domain=gen_spark_params(model)["domain"],
        temperature=temperature,
        streaming=False,
    )
    messages = gen_spark_messages(prompt)
    handler = ChunkPrintHandler()
    # 当 streaming设置为 False的时候, callbacks 并不起作用
    resp = spark_llm.generate([messages], callbacks=[handler])
    return resp


role_name = ""
role_prompt = ""
user_prompt = ""
# print(get_completion("你好").generations[0][0].text)

# 这里直接打印输出了正常响应内容，在生产环境中，需要兼容处理响应异常的情况
# print(get_completion(prompt.format(role_name, role_prompt, user_prompt)).generations[0][0].text)
