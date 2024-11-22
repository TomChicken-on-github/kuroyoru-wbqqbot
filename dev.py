# -*- coding: utf-8 -*-
import asyncio
import os
import json
from datetime import datetime

import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import GroupMessage, Message, C2CMessage

version = 0.1

appinfo = read(os.path.join(os.path.dirname(__file__), "appinfo.yaml"))

_log = logging.get_logger()

# 读取 JSON 文件
with open('characters.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 获取今天的日期
today = datetime.now().strftime('%m-%d')

class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    async def on_group_at_message_create(self, message: GroupMessage):
        messageResult = await message._api.post_group_message(
            group_openid=message.group_openid,
              msg_type=0, 
              msg_id=message.id,
              content=f"收到了消息：{message.content}")
        _log.info(messageResult)

    async def on_c2c_message_create(self, message: C2CMessage):
        await message._api.post_c2c_message(
            openid=message.author.user_openid, 
            msg_type=0, msg_id=message.id, 
            content=f"收到了消息：{message.content}")
    
    async def on_at_message_create(self, message: Message):
        _log.info(message.author.avatar)
        if "sleep" in message.content:
            await asyncio.sleep(10)
        _log.info(message.author.username)
        await message.reply(content=f"收到了消息： {message.content}")


if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    # intents = botpy.Intents.none()
    # intents.public_messages=True

    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_messages=True,public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=appinfo["appid"], secret=appinfo["secret"])