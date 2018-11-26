#! -*- coding: utf-8 -*-

import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fname = '/usr/share/fonts/adobe-source-han-sans-cn/SourceHanSansCN-Light.otf'
myfont = FontProperties(fname=fname, size=20)

sns.set(style='whitegrid')
f, ax = plt.subplots(figsize=(6, 12))

# 读取csv数据，因为内容含中文，所以要指定编码
loan_rate = pd.read_csv(u'央行历年贷款基准利率.csv', encoding='gb18030')

# 只需要取时间和五年以上的贷款利率
df = loan_rate.iloc[:, [0, -1]]
df.columns = ['date', 'rate']
df.date = pd.to_datetime(df.date, format='%Y.%m.%d').astype('unicode')
df = df[::-1]

sns.set_color_codes('muted')
bar = sns.barplot(x='rate', y='date', data=df, 
                  label='利率(%)', color='b')

# 设置图例，调整文字大小(rcParams["legend.fontsize"] = 14)
ax.legend(ncol=2, loc='best', frameon=True, prop={'size': 14, 'fname': fname})

ax.set(xlabel='', ylabel='')
ax.set_title('近20年房贷利率一览', fontproperties=myfont)
plt.show()

# bbox_inches需要设置为tight，否则保存下来的图不完整
f.savefig('近20年房贷利率柱状图.jpg', dpi=100, bbox_inches='tight')

