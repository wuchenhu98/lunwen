import matplotlib.font_manager as fm

# 列出系统中的所有字体
for font in fm.fontManager.ttflist:
    print(font.name)
