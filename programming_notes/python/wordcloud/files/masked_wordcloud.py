#! -*- coding: utf-8 -*-

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud as WC

text = open('files/python_en.txt').read()
alice_mask = np.array(Image.open('logo.png'))

wc = WC(background_color='white', mask=alice_mask, 
        contour_width=2, contour_color='steelblue')
wc.generate(text)

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
wc.to_file('masked_wordcloud.png')

