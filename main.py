import json
import requests
from datetime import datetime

version = 0.1

# 读取JSON文件
with open('characters.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

bot_key = data['bot']['key']
bot_id = data['bot']['id']
characters = data['characters']

# 获取今天的日期
today = datetime.now().strftime('%m-%d')

# 检查是否有角色生日
for character in characters:
    if character['birthday'] == today:
        message = f"今天是{today}，{character['name']}生日快乐！"
        payload = {
            'key': bot_key,
            'id': bot_id,
            'message': message
        }
        # 发送消息到群
        response = requests.post('https://api.example.com/send_message', json=payload)
        if response.status_code == 200:
            print(f"消息发送成功: {message}")
        else:
            print(f"消息发送失败: {response.status_code}")

