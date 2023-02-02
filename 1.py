#资料:
# http://www.wb86.com/post/330.html

# https://tkdocs.com/tutorial/text.html

#2022-01-28,22点58
# 现在技术难点已经完全攻破.
#现在解释如下. 道理就是把文字片段的背景色进行修改.(点击界面下面的标注1---5),消除标签点击第一个标注为空按钮
#======这里面我们就标注为B-tag1,I-tag1,E-tag1......B-tag5,....B-tag5即可
#得到BIO文件之后,用户只需要根据自己定好的替换自己需要的标签即可.比如B-PRODUCT...
#解释一下为什么用背景色来区分各个标签.因为我们有时候要标注空格比如尼古拉斯 凯奇.
# 这个名字之间带个空格,那么我们空格也要标注为I-PERSON才行.用前景色无法把空格染色!所以我们用背景色技巧!

#====================第三版. 打开原来的bio文件进行读取之前bio结果.

#==================自定义配置都写最上面:#如何动态修改tkinter按钮.
#=========现在的方案是 按照bio里面的直接按照配色表生成.现在支持10个.#==========现在还是自动配色吧. 搞一个配色表存着太麻烦感觉.
# =======================配置!!!!!!!!!!!!!!!!!!!
color_and_biaoqian=[
    ['white','标注为空'],
    ['red','person'],
    ['yellow','address'],
    ['Blue','org'],
    ['Cyan','telephone'],
    ['orange','time'],
    ['PeachPuff', 'nation'],
    # ['Gray', 'time3'],
    # ['Brown', 'time4'],
    # ['Tan', 'time5'],
    # ['Beige', 'time6']
]
#=============支持2种模式, 可以先写bioes或者bio
tool_type='bioes'
# tool_type='bio'







# 环境是win10 python3.6

from tkinter import *
#=============第一层是text
import tkinter
root = Tk(className='                                                                                                                            信息抽取标注工具(一键生成bioes格式)')
# frame = Frame (root, relief=RAISED, borderwidth=20)

text = Text(root, width=125,height=20,font=('宋体',15),wrap = 'none')
text.insert('1.0', '贴入你要处理的sdfsadf张某,李某,sdfsdfasfasd王某他们杀人了fas]\n sdfsadf张某,李某,sdfsdfasfasd王某他们杀人了文字 中文 English 都行\n贴入你要处理的文字')# 1.0 第一行0列.

colorlist=[i[0] for i in color_and_biaoqian]
labellist=[i[1] for i in color_and_biaoqian]

#====滚动条竖直:
scroll = tkinter.Scrollbar()
# 放到窗口的右侧, 填充Y竖直方向
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)



#滚动条横向
s2 = Scrollbar(root, orient = HORIZONTAL)
s2.pack(side = BOTTOM, fill = X)

s2.config(command = text.xview)
text.config(xscrollcommand=s2.set)
print( text.get('1.0', 'end'))
text.pack()
# frame.pack()



#第二层是frame 来放按钮的.
frame = Frame (root, relief=RAISED, borderwidth=2)
frame.pack (side=TOP, fill=BOTH, ipadx=5, ipady=5, expand=1)

def helloCallBack(color):
   print(1111111111111)
   try:
       print(SEL_FIRST,SEL_LAST)
       print(text.index("sel.first"),text.index("sel.last"))
       text.tag_config(color,  background=color)  # 再为标签进行设置==类似html里面的div 里面class属性.
       #===============注意要先删除其他的标签.
       for i in colorlist:
           text.tag_remove( i,text.index("sel.first"), text.index("sel.last"))  # =======变色
       if color !='white':#======white实际上是不进行背景色标注!这样效果最好!!!!!!a trick
            text.tag_add(color, text.index("sel.first"),text.index("sel.last")) #=======变色
       # print(text.tag_ranges(color))


       # print(11111111111)
   except:
       pass


def helloCallBack_read_bio(i,j,color):
   print(1111111111111)
   a=i
   b=j
   try:
       # print(SEL_FIRST,SEL_LAST)
       # print(text.index("sel.first"),text.index("sel.last"))
       text.tag_config(color,  background=color)  # 再为标签进行设置==类似html里面的div 里面class属性.
       #===============注意要先删除其他的标签.
       for i in colorlist:
           text.tag_remove( i,a, b)  # =======变色
       if color !='white':#======white实际上是不进行背景色标注!这样效果最好!!!!!!a trick
            text.tag_add(color, a,b) #=======变色
       # print(text.tag_ranges(color))


       # print(11111111111)
   except:
       pass

import kmp_for_array

def helloCallBack_quanbiaozhu(color):

   print(1111111111111)
   if 1:
       print(SEL_FIRST,SEL_LAST)
       print(text.index("sel.first"),text.index("sel.last"))
       text.tag_config(color,  background=color)  # 再为标签进行设置
       wenben=text.get(text.index("sel.first"),text.index("sel.last"))
       print("获取到的文本是",wenben)
       if 1:
          #=============调用python的搜索
          all_text=text.get('1.0',END)
          print(all_text)
          tmp= all_text.split('\n')
          out2=[]
          for i in range(len(tmp)):#=========这里面需要字符串的kmp算法
              kkk=kmp_for_array.kmp(tmp[i],wenben,return_all=True)
              if kkk!=-1:
                #================一个bug, 比如 aaa 然后我要把aa标注为红色.那么就会图2次.所以这里面我们强制让他只图最前面的aa,后的aa忽略#==============3.0版本修复了这个bug
                last_tail=0
                for j in kkk:
                    if j>=last_tail:
                        out2.append([f'{i+1}.{j}',f'{i+1}.{j+len(wenben)}' ])
                        last_tail=j+len(wenben)


              print(out2,999999999999999999)

       for weizhi in out2:
       #===============注意要先删除其他的标签.
           for i in colorlist:
               text.tag_remove( i,weizhi[0], weizhi[1])  # =======变色
           if color !='white':#======white实际上是不进行背景色标注!这样效果最好!!!!!!a trick
                text.tag_add(color,weizhi[0], weizhi[1]) #=======变色

           # print(text.tag_ranges(color))
import  re
#
# def zhengzehelloCallBack_quanbiaozhu2(color):
#
#    print(1111111111111)
#    if 1:
#        print(SEL_FIRST,SEL_LAST)
#        print(text.index("sel.first"),text.index("sel.last"))
#        text.tag_config(color,  background=color)  # 再为标签进行设置!!!!!!!!!!!!!!!!!这句话千瓦不要忘了!!!!!!!!!!!!!!
#        wenben='g'
#        print("获取到的文本是",wenben)
#        if 1:
#           #=============调用python的搜索
#           all_text=text.get('1.0',END)
#           print(all_text)
#           tmp= all_text.split('\n')
#           out2=[]
#           for i in range(len(tmp)):#=========这里面需要字符串的kmp算法
#               kkk=kmp_for_array.kmp(tmp[i],wenben,return_all=True)
#               if kkk!=-1:
#                 #================一个bug, 比如 aaa 然后我要把aa标注为红色.那么就会图2次.所以这里面我们强制让他只图最前面的aa,后的aa忽略#==============3.0版本修复了这个bug
#                 last_tail=0
#                 for j in kkk:
#                     if j>=last_tail:
#                         out2.append([f'{i+1}.{j}',f'{i+1}.{j+len(wenben)}' ])
#                         last_tail=j+len(wenben)
#
#
#               print(out2,999999999999999999)
#
#        for weizhi in out2:
#        #===============注意要先删除其他的标签.
#            for i in colorlist:
#                text.tag_remove( i,weizhi[0], weizhi[1])  # =======变色
#            if color !='white':#======white实际上是不进行背景色标注!这样效果最好!!!!!!a trick
#                 text.tag_add(color,weizhi[0], weizhi[1]) #=======变色

def zhengzehelloCallBack_quanbiaozhu(color):

           a=e.get()

           print(a,3333333333333333333333333333333333333333)
           print(1111111111111)
           aaa=text.get('1.0',"end")
           print(text.get('1.0',"end"),324234234234324234234234234324234233)
           tmp=re.findall(a,aaa)
           tmp=set(tmp)
           if 1:
               for i1 in tmp:
                   #找到每一个索引:
                       # print(SEL_FIRST, SEL_LAST)
                       # print(text.index("sel.first"), text.index("sel.last"))
                       text.tag_config(color, background=color)  # 再为标签进行设置
                       wenben =i1
                       print("获取到的文本是", i1)
                       if 1:
                           # =============调用python的搜索
                           all_text = text.get('1.0', END)
                           print(all_text)
                           tmp = all_text.split('\n')
                           out2 = []
                           for i in range(len(tmp)):  # =========这里面需要字符串的kmp算法
                               kkk = kmp_for_array.kmp(tmp[i], wenben, return_all=True)
                               if kkk != -1 and kkk!=0:
                                   # ================一个bug, 比如 aaa 然后我要把aa标注为红色.那么就会图2次.所以这里面我们强制让他只图最前面的aa,后的aa忽略#==============3.0版本修复了这个bug
                                   last_tail = 0
                                   for j in kkk:
                                       if j >= last_tail:
                                           out2.append([f'{i + 1}.{j}', f'{i + 1}.{j + len(wenben)}'])
                                           last_tail = j + len(wenben)

                               print(out2, 999999999999999999)

                       for weizhi in out2:
                           # ===============注意要先删除其他的标签.
                           for i in colorlist:
                               text.tag_remove(i, weizhi[0], weizhi[1])  # =======变色
                           if color != 'white':  # ======white实际上是不进行背景色标注!这样效果最好!!!!!!a trick
                               print(color, weizhi[0], weizhi[1],'fjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
                               text.tag_add(color, weizhi[0], weizhi[1])  # =======变色

       # print(11111111111)

#https://blog.csdn.net/wjciayf/article/details/79261005  颜色表
# c0='black'
# c1='red'
# c2='yellow'
# c3='Blue'
# c4='Cyan'
# c5='Lime'
#=================command 这个函数不能用for实现.改用动态生成.可以避免共享变量.
#放按钮使用.
aa=[0,1,2,3,4,5,6,7,8,9,10]
save_all_button=[]
def setup_button():

    print('进行重置按钮')
    print(colorlist,99999999999999999999999999999999999999999)
    b=tkinter.Button(frame, text ="标注为空", command = lambda :helloCallBack(colorlist[0]))
    b.grid(row=0,column=1,padx=10)
    button_grid_info = b.grid_info()
    # b.grid_forget()
    if 0: #########2023-02-01,18点46这个地方可以删除国企按钮,其实没啥必要删除.因为你扩充时候可能还需要.扩充时候可以自己改代码19行. 添加自己需要的类别.
        for i in save_all_button:#================这一步用来每次删除过期的按钮.
            button_grid_info = i.grid_info()
            i.grid_forget()
  # row column可以自己修改按钮放的位置!!!!!
    for i in range(len(color_and_biaoqian)):
        if i==0:
            continue
#============callback函数里面不允许写变量..........  #参考https://www.cnpython.com/qa/68533
        if 1:           # lambda表达式.里面要写x=i, 然后再把x传入:右边的函数.这样可以脱离之前的变量控制.
            fffff=('宋体',10,'bold')
            b=tkinter.Button(frame, bg=colorlist[i],font=fffff,text =labellist[i], command = lambda x=i: helloCallBack(colorlist[x]))
            b.grid(row=0,column=(i+1),padx=10)
            save_all_button.append(b)#===============把变量存在全局变量里面,变量就不会跟着函数销毁了.
    #================下面一排是全标注===全文有这个词的直接全标注上.

            b=tkinter.Button(frame, bg=colorlist[i], font=fffff,text =labellist[i]+'全标注', command = lambda x=i:helloCallBack_quanbiaozhu(colorlist[x]))
            b.grid(row=1,column=(i+1),padx=10)
            save_all_button.append(b)

            b = tkinter.Button(frame,  bg=colorlist[i],font=fffff,text=labellist[i] + '正则标注',
                               command=lambda x=i: zhengzehelloCallBack_quanbiaozhu(colorlist[x]))
            b.grid(row=2, column=(i + 1), padx=10)
            save_all_button.append(b)


def save():
        moshi=cmb.get()
        print(moshi,3333333333333333333333333333333333333333333333333333)
        if 'es' in moshi:
            tool_type='bioes'
        else:
            tool_type = 'bio'
        print("获取文本")
        result = text.get("1.0", "end")  # 获取文本输入框的内容


        with open('output.txt','w',encoding='utf-8') as f:
            f.writelines(result)





        for i in colorlist:
            aaa=text.tag_ranges(i)###=得到的aaa标里面每2个表示开头结尾索引.
            print(aaa,i)
        #=======下面都是简单的字符串处理而已
        yuanwen=result.split('\n')
        jieguo=[list('O'*len(i)) for i in yuanwen]
        #=====根据颜色标注即可:
        for dex,i in enumerate(colorlist):
            aaa = text.tag_ranges(i)  ###=得到的aaa标里面每2个表示开头结尾索引.
            for j in range(len(aaa)//2):
                a11= int(aaa[2*j].string.split('.')[0])#首航
                a12= int(aaa[2*j].string.split('.')[1])#首列
                a21= int(aaa[2*j+1].string.split('.')[0])#尾行
                a22= int(aaa[2*j+1].string.split('.')[1])# 尾列
                if tool_type!='bio':
                    if a11!=a21:
                        print("bugle !!!!","索引在",a11,a12,a21,a22)
                    else:
                        if a22-a12==1:#标注S!
                            jieguo[a11-1][a12]="S-"+str(labellist[dex])
                        else:
                            jieguo[a11-1][a12:a22]=["B-"+str(labellist[dex])]+["I-"+str(labellist[dex])]*(a22-a12-2)+["E-"+str(labellist[dex])]
                if tool_type=='bio':
                    if a11 != a21:
                        print("bugle !!!!", "索引在", a11, a12, a21, a22)
                    else:

                            jieguo[a11 - 1][a12:a22] = ["B-" + str(labellist[dex])] + ["I-" + str(labellist[dex])] * (
                                        a22 - a12 - 1)

        print(jieguo,111111111111111111111111111111111111111111111111111111)
        jieguo=[' '.join(i)+'\n' for i in jieguo]
        print(jieguo)
        with open('output.bio','w') as f:
            f.writelines(jieguo)















setup_button()
def chognzhi():

    #============填入文本.
    with open('output.txt' ,encoding='utf-8') as f:
        tmp=f.readlines()
    text.delete('1.0','end')
    text.insert('1.0',''.join(tmp))






    with open('output.bio' ) as f:
        tmp=f.readlines()
    tmp3=tmp
    print(tmp)
    tmp=' '.join(tmp).replace('\n',' ').split(' ')
    tmp=[i[2:] for i in tmp if '-' in i]
    tmp2=[]
    for i in tmp:
        if i not in tmp2:
            tmp2.append(i)

    tmp=tmp2
    print(tmp,333333333333333333333333333)
    #=======进行配色.


    clis=   ['white',    'red'    ,'yellow','Blue','Cyan','orange','PeachPuff','Gray', 'Brown', 'Tan','Beige']



#我们的默认标签, 只有当新的跟这里面的不一样时候才做修改.
    global color_and_biaoqian
    global colorlist
    global labellist

    # color_and_biaoqian = [
    #     ['white', '标注为空'],
    # ['red','person'],
    # ['yellow','address'],
    # ['Blue','org'],
    # ['Cyan','telephone'],
    # ['orange','time'],
    # ['PeachPuff', 'nation'],
    # # ['Gray', 'time3'],
    # # ['Brown', 'time4'],
    # # ['Tan', 'time5'],
    # # ['Beige', 'time6']
    #
    # ]
    for i in range(len(tmp)):
        if tmp[i] not in labellist:
            color_and_biaoqian.append([clis[i+1],tmp[i]]) #替换就的按钮.
    colorlist = [i[0] for i in color_and_biaoqian]
    labellist = [i[1] for i in color_and_biaoqian]
    setup_button()
    #=============下面我们根据bio进行涂色.
    print(tmp3,44444444444444)
    tmp3=[i1.replace('\n','').split(' ') for i1 in tmp3]
    for i in range(len(tmp3)):
        for j in range(len(tmp3[i])):
            print(i,j,343423423423423423423423423423)
            print(i)
            print(j)
            print(tmp3[i][j],333333333333333333333333333333333333333333333333)
            if '-' in tmp3[i][j]:
                aaa=tmp3[i][j][2:]
                for jjj in color_and_biaoqian:
                    if jjj[1]==aaa:
                        color=jjj[0]
                        helloCallBack_read_bio(str(i+1)+'.'+str(j),str(i+1)+'.'+str(j+1),color)













#=============第三版我们来实现读取bio文件的功能.为了方便就不加对话框了.直接读取output.bio
b=tkinter.Button(frame, text ="读取bio文件和txt", command = chognzhi)
b.grid(row=0,column=0,padx=10)







# entryExample = Entry(root)
# entryExample.place(x = -10,
#         y =-10,
#         width=2000,
#         height=100)
import tkinter
from tkinter import ttk  # 导入ttk模块，因为下拉菜单控件在ttk中




# 创建下拉菜单
cmb = ttk.Combobox(frame)
cmb.grid(row=1, column=(1), padx=20)
# 设置下拉菜单中的值
cmb['value'] = ('标注模式bioes', '标注模式bio')

# 设置默认值，即默认下拉框中的内容
cmb.current(0)
# 默认值中的内容为索引，从0开始







aaa=tkinter.Label(frame,text='提示:右边写入正则表达式')
aaa.grid(row=2,column=0,padx=10)


b=tkinter.Button(frame, text ="保存文件为BIO和txt", command = save)
b.grid(row=1,column=0,padx=10)





# b=tkinter.Button(root, text ="标注2", command = helloCallBack(c2))
# b.pack()
# b=tkinter.Button(root, text ="标注3", command = helloCallBack(c3))
# b.pack()
# b=tkinter.Button(root, text ="标注4", command = helloCallBack(c4))
# b.pack()
# b=tkinter.Button(root, text ="标注5", command = helloCallBack(c5))


# text.tag_add('highlightline', '5.0', '6.0')
#
# text.tag_configure('highlightline', background='yellow', font='TkFixedFont', relief='raised')
# text.insert('end','ffffffffff','highlightline')
try:
    print(text.get(SEL_FIRST,SEL_LAST))
except:
    pass



E1 = Entry(frame, bd =5,)
E1.insert('0','.{1}某')

E1.grid(row=2, column=(1), padx=20)

e=E1


# b = tkinter.Button(frame, text='右边输入你要的正则再点我进行标注', command=lambda x=1:reg())
# b.grid(row=2, column=( 0), padx=10)



#按扭调用的函数，
def reg():
    a = e.get()
    print(a,333333333333333333333333333333333333333333333333333333333)



















root.mainloop()
















'''
colors =#FFB6C1 LightPink 浅粉红
#FFC0CB Pink 粉红
#DC143C Crimson 深红/猩红
#FFF0F5 LavenderBlush 淡紫红
#DB7093 PaleVioletRed 弱紫罗兰红
#FF69B4 HotPink 热情的粉红
#FF1493 DeepPink 深粉红
#C71585 MediumVioletRed 中紫罗兰红
#DA70D6 Orchid 暗紫色/兰花紫
#D8BFD8 Thistle 蓟色
#DDA0DD Plum 洋李色/李子紫
#EE82EE Violet 紫罗兰
#FF00FF Magenta 洋红/玫瑰红
#FF00FF Fuchsia 紫红/灯笼海棠
#8B008B DarkMagenta 深洋红
#800080 Purple 紫色
#BA55D3 MediumOrchid 中兰花紫
#9400D3 DarkViolet 暗紫罗兰
#9932CC DarkOrchid 暗兰花紫
#4B0082 Indigo 靛青/紫兰色
#8A2BE2 BlueViolet 蓝紫罗兰
#9370DB MediumPurple 中紫色
#7B68EE MediumSlateBlue 中暗蓝色/中板岩蓝
#6A5ACD SlateBlue 石蓝色/板岩蓝
#483D8B DarkSlateBlue 暗灰蓝色/暗板岩蓝
#E6E6FA Lavender 淡紫色/熏衣草淡紫
#F8F8FF GhostWhite 幽灵白
#0000FF Blue 纯蓝
#0000CD MediumBlue 中蓝色
#191970 MidnightBlue 午夜蓝
#00008B DarkBlue 暗蓝色
#000080 Navy 海军蓝
#4169E1 RoyalBlue 皇家蓝/宝蓝
#6495ED CornflowerBlue 矢车菊蓝
#B0C4DE LightSteelBlue 亮钢蓝
#778899 LightSlateGray 亮蓝灰/亮石板灰
#708090 SlateGray 灰石色/石板灰
#1E90FF DodgerBlue 闪兰色/道奇蓝
#F0F8FF AliceBlue 爱丽丝蓝
#4682B4 SteelBlue 钢蓝/铁青
#87CEFA LightSkyBlue 亮天蓝色
#87CEEB SkyBlue 天蓝色
#00BFFF DeepSkyBlue 深天蓝
#ADD8E6 LightBlue 亮蓝
#B0E0E6 PowderBlue 粉蓝色/火药青
#5F9EA0 CadetBlue 军兰色/军服蓝
#F0FFFF Azure 蔚蓝色
#E0FFFF LightCyan 淡青色
#AFEEEE PaleTurquoise 弱绿宝石
#00FFFF Cyan 青色
#00FFFF Aqua 浅绿色/水色
#00CED1 DarkTurquoise 暗绿宝石
#2F4F4F DarkSlateGray 暗瓦灰色/暗石板灰
#008B8B DarkCyan 暗青色
#008080 Teal 水鸭色
#48D1CC MediumTurquoise 中绿宝石
#20B2AA LightSeaGreen 浅海洋绿
#40E0D0 Turquoise 绿宝石
#7FFFD4 Aquamarine 宝石碧绿
#66CDAA MediumAquamarine 中宝石碧绿
#00FA9A MediumSpringGreen 中春绿色
#F5FFFA MintCream 薄荷奶油
#00FF7F SpringGreen 春绿色
#3CB371 MediumSeaGreen 中海洋绿
#2E8B57 SeaGreen 海洋绿
#F0FFF0 Honeydew 蜜色/蜜瓜色
#90EE90 LightGreen 淡绿色
#98FB98 PaleGreen 弱绿色
#8FBC8F DarkSeaGreen 暗海洋绿
#32CD32 LimeGreen 闪光深绿
#00FF00 Lime 闪光绿
#228B22 ForestGreen 森林绿
#008000 Green 纯绿
#006400 DarkGreen 暗绿色
#7FFF00 Chartreuse 黄绿色/查特酒绿
#7CFC00 LawnGreen 草绿色/草坪绿
#ADFF2F GreenYellow 绿黄色
#556B2F DarkOliveGreen 暗橄榄绿
#9ACD32 YellowGreen 黄绿色
#6B8E23 OliveDrab 橄榄褐色
#F5F5DC Beige 米色/灰棕色
#FAFAD2 LightGoldenrodYellow 亮菊黄
#FFFFF0 Ivory 象牙色
#FFFFE0 LightYellow 浅黄色
#FFFF00 Yellow 纯黄
#808000 Olive 橄榄
#BDB76B DarkKhaki 暗黄褐色/深卡叽布
#FFFACD LemonChiffon 柠檬绸
#EEE8AA PaleGoldenrod 灰菊黄/苍麒麟色
#F0E68C Khaki 黄褐色/卡叽布
#FFD700 Gold 金色
#FFF8DC Cornsilk 玉米丝色
#DAA520 Goldenrod 金菊黄
#B8860B DarkGoldenrod 暗金菊黄
#FFFAF0 FloralWhite 花的白色
#FDF5E6 OldLace 老花色/旧蕾丝
#F5DEB3 Wheat 浅黄色/小麦色
#FFE4B5 Moccasin 鹿皮色/鹿皮靴
#FFA500 Orange 橙色
#FFEFD5 PapayaWhip 番木色/番木瓜
#FFEBCD BlanchedAlmond 白杏色
#FFDEAD NavajoWhite 纳瓦白/土著白
#FAEBD7 AntiqueWhite 古董白
#D2B48C Tan 茶色
#DEB887 BurlyWood 硬木色
#FFE4C4 Bisque 陶坯黄
#FF8C00 DarkOrange 深橙色
#FAF0E6 Linen 亚麻布
#CD853F Peru 秘鲁色
#FFDAB9 PeachPuff 桃肉色
#F4A460 SandyBrown 沙棕色
#D2691E Chocolate 巧克力色
#8B4513 SaddleBrown 重褐色/马鞍棕色
#FFF5EE Seashell 海贝壳
#A0522D Sienna 黄土赭色
#FFA07A LightSalmon 浅鲑鱼肉色
#FF7F50 Coral 珊瑚
#FF4500 OrangeRed 橙红色
#E9967A DarkSalmon 深鲜肉/鲑鱼色
#FF6347 Tomato 番茄红
#FFE4E1 MistyRose 浅玫瑰色/薄雾玫瑰
#FA8072 Salmon 鲜肉/鲑鱼色
#FFFAFA Snow 雪白色
#F08080 LightCoral 淡珊瑚色
#BC8F8F RosyBrown 玫瑰棕色
#CD5C5C IndianRed 印度红
#FF0000 Red 纯红
#A52A2A Brown 棕色
#B22222 FireBrick 火砖色/耐火砖
#8B0000 DarkRed 深红色
#800000 Maroon 栗色
#FFFFFF White 纯白
#F5F5F5 WhiteSmoke 白烟
#DCDCDC Gainsboro 淡灰色
#D3D3D3 LightGrey 浅灰色
#C0C0C0 Silver 银灰色
#A9A9A9 DarkGray 深灰色
#808080 Gray 灰色
#696969 DimGray 暗淡灰
#000000 Black 纯黑
'''













