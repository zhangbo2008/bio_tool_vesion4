"# bio_annotate_tools" 
4.1版本.
目前功能:
保存bio txt文件按钮: 按下后编辑器里面的文本自动保存为output.txt  , 标注保存为output.bio
读取bio txt文件按钮: 按下后编辑器里面的文本设置为output.txt, 标注设置为output.bio
颜色类别数量最大十个.可以在1.py:19 设置. 目前主要是因为屏幕按钮太多会不容易排列,所以最大设置10个类别.
                                      代码目前默认6个类别.不同任务时候需要自己修改.
支持三种标注方式. 第一排单独标注:选择一块文本后点按钮会涂色
                第二排全体标注:会全文搜索跟选中的相同文本一样的都读图一样色
                第三排是正则标注:框里面写入正则然后点右边的按钮会正则匹配全部符合的文本进行涂色.

加入了各种标注的颜色提醒.
正则输入框里面写了默认的例子.





3.0版本:
#================一个bug, 比如 aaa 然后我要把aa标注为红色.那么就会图2次.所以这里面我们强制让他只图最前面的aa,后的aa忽略#==============3.0版本修复了这个bug#================一个bug, 比如 aaa 然后我要把aa标注为红色.那么就会图2次.所以这里面我们强制让他只图最前面的aa,后的aa忽略#==============3.0版本修复了这个bug



2.0版本:
2022-01-29,17点11

更新了,全文匹配全部标注.

2022-01-29,10点58

网上的bio软件太垃圾了.
所以自己手撸一个.
基于tkinter开发. 只要你装了python3就可以直接运行1.py
使用方法.
1.贴入自己的文本.
2.鼠标选择一段文字然后点击下面1-5标注按钮
3.点击生成文件,就会在1.py同级目录生成ouput.bio文件.
#注意这个标注是任意字符都标注.空格也会一般标注为O.
#以为我的理解是这样会支持中英文以及名字里面带空格的情况,是最好的标注方式.
#至于标注按钮不够多,颜色不够明显,可以根据自己要求修改1.py里面的文件.




#==========bio标注: NER任务. 命名实体识别,信息抽取.


经典工具是 精灵标注助手



















"# bio_tool_version3" 
"# bio_tool_vesion4" 
