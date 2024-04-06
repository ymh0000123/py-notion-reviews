def to_markdown(data):
    markdown_table = ["|状态|邮箱|创建时间|内容|昵称|URL|IP|",
                      "|---|---|---|---|---|---|---|"]

    for page in data['results']:
        status = page['properties']['状态']['select']['name'] if page['properties']['状态']['select'] else '-'
        email = page['properties']['邮箱']['email'] if page['properties']['邮箱']['email'] else '-'
        created_time = page['properties']['创建时间']['created_time']
        content = page['properties']['内容']['rich_text'][0]['plain_text'] if page['properties']['内容']['rich_text'] else '-'
        nickname = page['properties']['昵称']['title'][0]['plain_text'] if page['properties']['昵称']['title'] else '-'
        page_url = page['properties']['页面']['url'] if page['properties']['页面']['url'] else '-'
        IP = page['properties']['IP']['rich_text'][0]['plain_text'] if page['properties']['IP']['rich_text'] else '-'
        url = page['url']

        # 将每行的数据添加到Markdown表格中
        markdown_table.append(f"|{status}|{email}|{created_time}|{content}|{nickname}|{url}|{page_url}|{IP}|")

    # 将整个Markdown表格作为一个字符串返回
    return '\n'.join(markdown_table)

def to_markdown_no_table(data):
    markdown_table = []

    for page in data['results']:
        status = page['properties']['状态']['select']['name'] if page['properties']['状态']['select'] else '-'
        email = page['properties']['邮箱']['email'] if page['properties']['邮箱']['email'] else '-'
        created_time = page['properties']['创建时间']['created_time']
        content = page['properties']['内容']['rich_text'][0]['plain_text'] if page['properties']['内容']['rich_text'] else '-'
        nickname = page['properties']['昵称']['title'][0]['plain_text'] if page['properties']['昵称']['title'] else '-'
        page_url = page['properties']['页面']['url'] if page['properties']['页面']['url'] else '-'
        IP = page['properties']['IP']['rich_text'][0]['plain_text'] if page['properties']['IP']['rich_text'] else '-'
        url = page['url']

        # 将每行的数据添加到Markdown表格中
        markdown_table.append(f"|{status}|{email}|{created_time}|{content}|{nickname}|{url}|{page_url}|{IP}|")

    # 将整个Markdown表格作为一个字符串返回
    return '\n'.join(markdown_table)