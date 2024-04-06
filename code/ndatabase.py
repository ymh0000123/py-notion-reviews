import os
from dotenv import load_dotenv
from notion_client import Client
from datetime import datetime

# 加载环境变量
load_dotenv()

# 从环境变量中获取 API 密钥和数据库 ID
NOTION_KEY = os.getenv('NOTION_KEY')
NOTION_PAGE_ID = os.getenv('NOTION_PAGE_ID')

# 初始化 Notion 客户端
notion = Client(auth=NOTION_KEY)

def notion_database(name, content, email,statuses,url,IP):
    try:
        # 获取今天的日期
        today_date = datetime.now().strftime('%Y-%m-%d')

        # 创建新页面（记录）到你的 Notion 数据库
        response = notion.pages.create(**{
            'parent': {'database_id': NOTION_PAGE_ID},
            'properties': {
                '昵称': {
                    'title': [
                        {'text': {'content': name}}
                    ]
                },
                '日期': {
                    'date': {
                        'start': today_date,
                    }
                },
                '内容': {
                    'rich_text': [{'text': {'content': content}}],
                },
                '邮箱': {
                    'email': email,
                },
                '状态': {
                    'select': {
                        'name': statuses
                    }
                },
                '页面': {
                    'url': url
                },
                'IP': {
                    'rich_text': [{'text': {'content': IP}}],
                }
            }
        })
    except Exception as e:
        print('Error adding item to Notion:', e)

#notion_Database_xr('awa', '这是一个示例内容', 'example@example.com', '显示', 'https://www.example.com', '127.0.0.1')

def read_notion_database(page_id=NOTION_PAGE_ID, api_key=NOTION_KEY):
    try:
        client = Client(auth=api_key)
        database = client.databases.query(**{"database_id": page_id})
        return database
    except Exception as e:
        return {"error": str(e)}
    
