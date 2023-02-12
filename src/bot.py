from graia.ariadne.app import Ariadne
from graia.ariadne.entry import config
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.ariadne.message import Source
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.parser.base import DetectPrefix, MentionMe
from graia.ariadne.model import Friend
from typing_extensions import Annotated
from loguru import logger

app = Ariadne(
    config(
        verify_key="123456789",  # 填入 VerifyKey
        account=123456789,  # 你的机器人的 qq 号
    ),
)

@app.broadcast.receiver("FriendMessage")
async def friend_message_listener(app: Ariadne, friend: Friend):
    # logger.info(f"{source}")
    # logger.info(f"{chain}")

    await app.send_message(friend, MessageChain([Plain("Hello, World!")]))
    # 实际上 MessageChain(...) 有没有 "[]" 都没关系

app.launch_blocking()
