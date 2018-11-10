#! -*- coding: utf-8 -*-

import jieba
from scipy.misc import imread
from wordcloud import ImageColorGenerator, WordCloud as WC

text = open('files/python_zh.txt').read()
cn_text = ' '.join(jieba.cut(text))

font_path = '/usr/share/fonts/adobe-source-han-sans-cn/SourceHanSansCN-Normal.otf'
back_coloring = imread('images/python_logo.png')

wc = WC(font_path=font_path, background_color='white',
        mask=back_coloring, random_state=42, margin=2)
wc.generate(cn_text)

image_colors = ImageColorGenerator(back_coloring)
wc.recolor(color_func=image_colors)

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

wc.to_file('images/wordcloud_cn.png')

