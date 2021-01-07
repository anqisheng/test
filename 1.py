import imageio
import jieba
import csv
import collections
from wordcloud import WordCloud
import re
import jieba.analyse

CSV_FILE_PATH="./tb_c2cMsg_424240054.csv"
STOP_WORDS_FILE_PATH="./chinese.txt"
def read_csv_to_dict(index) -> dict:
    #utf-8
    with open(CSV_FILE_PATH, 'r', encoding='GB18030') as csvfile:
        reader = csv.reader(csvfile)
        column=[]
        result=''
        for columns in reader:
            # column.append(jieba.lcut(columns[index]))
            if re.findall(r'<(.*)>(.*)',columns[index]) or re.findall(r'http(.*)',columns[index]):
                result=result
            else:
                column+=jieba.lcut(columns[index])
        # column = [columns[index] for columns in reader]
        # print(column)
        # dic = collections.Counter(column)#统计列表元素出现次数
        return column
        # print(result)
        # return result
def analysis_sina_content():
    # 读取微博内容列
    words = read_csv_to_dict(1)
    word_list=' '
    word_dict={}
    excludes =[]
    # excludes=["img","url","cn","encoding","UTF","id","通话","一个","然后","流泪","不是","没有","可以","干嘛","这个","我们","明天","回去","现在","什么","知道","就是","那个","今天","刚刚"]
    # fp=open(STOP_WORDS_FILE_PATH,'r',encoding="gb18030")
    # reader=fp.read();
    # for word in reader:
    #     excludes.append(word)
    # fp.close()
    for word in words:
        # 数据清洗，去掉无效词
        if word not in excludes and len(word)>1 and len(word)<6:
            word_list = word_list + ' ' + word
            if (word_dict.get(word)):
                word_dict[word] = word_dict[word] + 1
            else:
                word_dict[word] = 1
            # print(word)
    sort_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    print(sort_words[0:101])  # 输出前0-100的词
    #print(dic)
    # print(word_list)
    color_mask = imageio.imread("1.png")
    wordcloud = WordCloud(
        background_color='white',font_path='/Library/Fonts/Arial Unicode.ttf', width=1000,height=600,collocations=False,mask=color_mask# 图幅宽度 中文字体名（点击属性查看，选英文名的汉字字体）不加报错 默认路径C:\Windows\Fonts\STZHONGS.TTF 华文中宋
    ).generate(word_list)#generate_from_frequencies(sort_words)

    image_1 = wordcloud.to_image()
    wordcloud.to_file("zrc.png")
    image_1.show()
analysis_sina_content()