# 抓取选股宝涨幅前5的股票池（协程版）

## 闲来无事

闲来无事，把[上一篇](grab-stock-theme.md)的代码改成协程版。

## 第三方库

```bash
$ pip install aiohttp
$ pip install cchardet
$ pip install aiodns
```

## 代码

```python
# -*- coding:utf-8 -*-

import time
import aiohttp
import asyncio
from bs4 import BeautifulSoup

# 登陆配置
user = dict(Mobile='xxx', Password='xxx')

'''url汇总
流程：登陆 -> 从主题库中获取涨幅榜前5 -> 提取主题下收录的股票 -> 获取股票对应的名称、最新价和跌涨幅
'''
login_url = 'https://api.xuangubao.cn/api/account/mobile_login'
zhutiku_url = 'https://xuangubao.cn/zhutiku'
theme_template = 'https://wows-api.wallstreetcn.com/v3/aioria/sset/bankuaiji?id={id}'
stocks_query = 'https://wows-api.wallstreetcn.com/real?fields=prod_name,last_px,px_change_rate&en_prod_code={}'


async def grab_theme_id(session):
    async with session.get(zhutiku_url) as resp:
        html = await resp.text()
        soup = BeautifulSoup(html, 'html.parser')

        # 涨跌共18个主题，取涨幅榜的前5个主题研究
        themes = soup.find_all(class_='zhutiku-sort-bkj')
        theme_ids = [link.get('data-url') for link in themes[:5]]
        return theme_ids


async def query_theme_stock(session, theme_id):
    """查询主题下的股票，返回股票代码列表"""
    async with session.get(theme_template.format(id=theme_id)) as resp:
        rsp = await resp.json()
    
        if rsp.get('code') == 20000:
            data = rsp.get('data', {})
            name, stocks =  data.get('name'), data.get('stocks', [])
            stocks = [item.get('symbol') for item in stocks]
            return name, stocks


async def query_stock_detail(session, stock_lst):
    # 这里只查询股票名称、最新价和涨跌幅
    
    async with session.get(stocks_query.format(','.join(stock_lst))) as resp:
        rsp = await resp.json()
        
        datas = rsp.get('data', {}).get('snapshot', {})
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
            # 按涨幅降序
            return sorted(result, key=lambda item: float(item[3].split()[0]), reverse=True)
        return result


async def main():
    today = time.strftime('%Y.%m.%d', time.localtime(time.time()))
    print(today)
    print('\n')
    
    async with aiohttp.ClientSession() as session:
        async with session.post(login_url, json=user) as resp:
            rsp = await resp.json()
            token = rsp.get('Token')

            if not token:
                # 5次登陆失败会锁定账号
                print('Login fail: code={errcode} msg={errmsg}'.format(**rsp))
                exit(-1)

            # 选股宝的数据是请求华尔街见闻的，如果不传token不会得到数据
            session._default_headers.update({'X-Appgo-Token': token})

            theme_ids = await grab_theme_id(session)
            if not theme_ids:
                print('No datas, exit...')
                exit(0)

            for _id in theme_ids:
                result = await query_theme_stock(session, _id)
                if not result:
                    print('pass {}...'.format(_id))

                name, stock_lst = result
                stock_detail = await query_stock_detail(session, stock_lst)
                print(name)
                for item in stock_detail:
                    print('\t\t'.join(item))
                print('\n')

                
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## 效果

发现运行速度差不过，没有明显加快，应该和请求量太少有关。

