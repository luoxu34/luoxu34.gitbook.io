# 抓取选股宝涨幅前5的股票池

## 由来

偶尔浏览[选股宝的主题库](https://xuangubao.cn/zhutiku)，但是使用起来不是很方便：
* 必须登陆才能看到主题包含股票
* 股票池不能直接复制股票代码，如果导入自选需要手动输入

基于这两个原因，有了这篇笔记。

## 源码

```python
# -*- coding:utf-8 -*-

import time
import requests
from bs4 import BeautifulSoup

# 登陆配置
user = dict(Mobile='xxx', Password='xxx')

# url汇总
login_url = 'https://api.xuangubao.cn/api/account/mobile_login'
zhutiku_url = 'https://xuangubao.cn/zhutiku'
theme_template = 'https://wows-api.wallstreetcn.com/v3/aioria/sset/bankuaiji?id={id}'
stocks_query = 'https://wows-api.wallstreetcn.com/real?fields=prod_name,last_px,px_change_rate&en_prod_code={}'

'''
流程：
登陆 -> 从主题库中获取涨幅榜前5 -> 提取主题下收录的股票 -> 获取股票对应的名称、最新价和跌涨幅
'''

def login():
    """登陆成功返回session，否则None"""
    s = requests.session()
    r = s.post(login_url, json=user)

    rsp = r.json()
    token = rsp.get('Token')

    if not token:
        # 5次登陆失败会锁定账号
        print('Login fail: code={errcode} msg={errmsg}'.format(**rsp))
        return

    # 选股宝的数据是请求华尔街见闻的，如果不传token不会得到数据
    s.headers.update({'X-Appgo-Token': token})
    return s


def grab_theme_id(session):
    html = session.get(zhutiku_url).text
    soup = BeautifulSoup(html, 'html.parser')

    # 涨跌共18个主题，取涨幅榜的前5个主题研究
    themes = soup.find_all(class_='zhutiku-sort-bkj')
    theme_ids = [link.get('data-url') for link in themes[:5]]
    return theme_ids


def query_theme_stock(session, theme_id):
    """查询主题下的股票，返回股票代码列表"""
    rsp = session.get(theme_template.format(id=theme_id)).json()
    
    if rsp.get('code') == 20000:
        data = rsp.get('data', {})
        name, stocks =  data.get('name'), data.get('stocks', [])
        stocks = [item.get('symbol') for item in stocks]
        return name, stocks


def query_stock_detail(session, stock_lst):
    # 这里只查询股票名称、最新价和涨跌幅
    rsp = session.get(stocks_query.format(','.join(stock_lst)))
    
    datas = rsp.json().get('data', {}).get('snapshot', {})
    if 'fields' in datas:
        del datas['fields']

    result = list()
    for k, v in datas.items():
        code = k.split('.')[0]
        name = v[0].replace(' ', '')
        last_px = str(v[1])
        px_change_rate = '%.2f %%' % v[2]
        result.append((code, name, last_px, px_change_rate))
    
    if result:
        # 按涨幅降序排列
        return sorted(result, key=lambda item: float(item[3].split()[0]), reverse=True)
    return result


def main():
    today = time.strftime('%Y.%m.%d', time.localtime(time.time()))
    print(today)
    print('\n')

    # 登陆，保存token
    session = login()
    if not session:
        exit(-1)
        
    # 提取涨幅前5的主题id
    theme_ids = grab_theme_id(session)
    if not theme_ids:
        print('No datas, exit...')
        exit(0)
    
    for _id in theme_ids:
        # 提取主题收录的股票
        result = query_theme_stock(session, _id)
        if not result:
            print('pass {}...'.format(_id))
        name, stock_lst = result
        
        # 查询股票的现价和涨幅
        stock_detail = query_stock_detail(session, stock_lst)
        print(name)
        for item in stock_detail:
            print('\t\t'.join(item))
        print('\n')


if __name__ == '__main__':
    main()

```

## 运行效果
```python
In [1]: %run grab_stock_theme.py
2018.12.05


苹果期货
300175		朗源股份		4.42		9.95 %
603336		宏辉果蔬		18.56		4.27 %
000902		新洋丰          9.47		-2.97 %
600962		国投中鲁		8.42		-1.17 %
600192		长城电工		4.76		-0.21 %


知识产权
300356		光一科技		8.38		9.97 %
002235		安妮股份		6.99		8.20 %
300579		数字认证		26.48		6.13 %
300182		捷成股份		5.26		4.99 %

.....
```

## 运行时间
```python
In [2]: %time main()

CPU times: user 116 ms, sys: 6.92 ms, total: 123 ms
Wall time: 2.22 s
```

## 还没解决

1. 还是需要登陆才能抓取到热门主题
2. 如果能显示股票的基本财务信息更佳
3. 如果能显示是否龙头企业、今日龙头等信息更佳

