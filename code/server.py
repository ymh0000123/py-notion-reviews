from flask import Flask, render_template, request, redirect, url_for, jsonify
from ndatabase import notion_database, read_notion_database
from md import to_markdown_no_table
from flask_cors import CORS
import os
from akismet import Akismet
from dotenv import load_dotenv

load_dotenv()

AKISMET_API_KEY = os.getenv("AKISMET_API_KEY")
WEBSITE_URL = os.getenv("WEBSITE_URL")

akismet = Akismet(key=AKISMET_API_KEY, blog_url=WEBSITE_URL)

app = Flask(__name__)

# 检查是否存在白名单文件，如果不存在则创建一个空文件
def create_whitelist_if_not_exists(filename='whitelist.txt'):
    try:
        with open(filename, 'x') as f:
            pass  # 创建空文件
    except FileExistsError:
        pass  # 文件已存在

# 读取白名单文件并获取规则列表
def read_whitelist(filename='whitelist.txt'):
    with open(filename, 'r') as f:
        whitelist = f.readlines()
    return [rule.strip() for rule in whitelist]

# 创建白名单文件
create_whitelist_if_not_exists()

# 设置白名单允许跨域访问
CORS(app, origins=read_whitelist())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_comment', methods=['POST'])
def add_comment():
    nickname = request.form['nickname']
    comment_text = request.form['comment']
    email = request.form['email']
    webpage_url = request.form['webpage_url']
    ip = request.remote_addr

    # 判断是否为垃圾评论
    is_spam = akismet.comment_check(
        user_ip=request.remote_addr,
        user_agent=request.user_agent.string,
        comment_content=comment_text,
        comment_author=email,
        comment_author_email=email,
        comment_author_url=WEBSITE_URL,
        referrer=request.referrer,
    )

    if is_spam:
        # 如果评论被认定为垃圾，您可以在这里执行相应的操作，比如拒绝该评论或者进行其他处理。
        return "检测到是垃圾评论"
    else:
        notion_database(nickname, comment_text, email, '显示', webpage_url, ip)

    # 如果评论没有被认定为垃圾，将评论添加到数据库中
    # 此处省略将评论添加到数据库的代码，您可以根据具体需求来实现它

    return redirect(url_for('index'))

@app.route('/comments-api')
def comments_api():
    all_comments = to_markdown_no_table(read_notion_database())  # 获取所有评论

    # 将评论数据转换为 JSON 格式并返回

    #return jsonify(all_comments)
    return all_comments
    #return tojson(all_comments)


@app.route('/comments')
def show_comments():
    # 不再需要在这里转换为 Markdown
    return render_template('comments.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
