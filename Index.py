#-*- coding: utf-8 -*-

import requests
import json
import xlwt
from tqdm import tqdm
from urllib.parse import urlencode
from requests.exceptions import RequestException

def get_one_page(keyword, page):
    '''获取网页html内容并返回'''
    params = {
        'start': 60*page,
        'pageSize': 60,
        'cityId': 551,
        'workExperience': -1,
        'education': -1,
        'companyType': -1,
        'employmentType': -1,
        'jobWelfareTag': -1,
        'kw': keyword,
        'kt': 3,
        '_v': 0.68835296,
        'x-zp-page-request-id': '2b995be51f934153813673e09ff7c6a4-1541993800360-547038'
    }

    url = 'https://fe-api.zhaopin.com/c/i/sou?'
    try:
        # 获取网页内容，返回html数据
        url += urlencode(params)
        response = requests.get(url)
        # 通过状态码判断是否获取成功
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        return e

def parse_one_page(html):
    '''提取有用信息并返回'''
    # json进行解析
    obj = json.loads(html)
    data = obj['data']
    result = data['results']

    for item in result:
        r = {}
        r[ 'company']= item['company']['name'],
        r[ 'company_type']= item['company']['type']['name'],
        r[ 'company_size']= item['company']['size']['name'],
        r['salary']= item['salary']
        r[ 'working_exp']= item['workingExp']['name'],
        r[ 'edu_level']= item['eduLevel']['name'],
        r['welfare']= item['welfare']
        yield r

def set_style(bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.bold = bold
    style.font = font

    return style

def write_table_headers(headers):
    '''写入表头'''
    file = xlwt.Workbook()
    table = file.add_sheet('安卓',True)
    for i in range(len(headers)):
        table.write(0,i,headers[i],set_style(True))
    return file,table

def write_table_rows(table, j, item):
    '''写入行'''
    table.write(j, 0, item[ 'company'])
    table.write(j, 1, item[ 'company_type'])
    table.write(j, 2, item[ 'company_size'])
    table.write(j, 3, item[ 'salary'])
    table.write(j, 4, item[ 'working_exp'])
    table.write(j, 5, item[ 'edu_level'])
    table.write(j, 6, item[ 'welfare'])

def main(city, keyword, pages):
    '''主函数'''
    filename = 'zl_' + city + '_' + keyword + '.xls'
    headers = ['公司', '性质', '规模', '待遇', '工作经验', '学历', '福利', '', '工作经验（平均）', '平均工资']
    file, table = write_table_headers(headers)
    for i in tqdm(range(pages)):
        '''
        获取该页中所有职位信息，写入csv文件
        '''
        html = get_one_page(keyword, i)
        items = parse_one_page(html)
        j = 1
        for item in items:
            write_table_rows(table, j, item)
            j+=1
    file.save(filename)


if __name__ == '__main__':
     main('重庆', '安卓', 10)