#! -*- coding: utf-8 -*-

from scipy.misc import imread
from wordcloud import ImageColorGenerator, WordCloud as WC

text = open('files/python_en.txt').read()
back_coloring = imread('python_logo.png')

wc = WC(background_color='white', mask=back_coloring, random_state=42, margin=2)
wc.generate(text)

image_colors = ImageColorGenerator(back_coloring)
wc.recolor(color_func=image_colors)

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

wc.to_file('image_colored_wordcloud.png')

