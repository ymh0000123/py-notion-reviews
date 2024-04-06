import re
import json

def tojson(data):
    pattern = r'\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|'

# 匹配数据
    matches = re.findall(pattern, data)

# 将匹配结果转换为JSON格式
    result = []
    for match in matches:
        status, email, create_time, content, nickname, url1, url2, ip = match
        result.append({
            "显示": status,
            "邮箱": email,
            "创建时间": create_time,
            "内容": content,
            "昵称": nickname,
            "URL": url1 if url1 != '/' else url2,
            "IP": ip
        })

# 打印结果
    return json.dumps(result, ensure_ascii=False, indent=2)