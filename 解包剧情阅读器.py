import re

# 要读取的文件路径
path = './'
# 要读取的文件名
filename = "a"
# 文件后缀
houzhui = ".txt"

with open(path+filename+houzhui, 'r',encoding='utf-8') as f:
    juqing = f.readlines()

re_mingzi = re.compile('name="(.*)"]')
re_duihua = re.compile(']\s*(.*)')
re_huifu = re.compile('"(.*)",')
re_xuanxiang = re.compile('"(.*)"')

jiexijuqing=[]

for i in juqing:
    # 第一种类型 对话
    if i[:5] == "[Name" or i[:5] =="[name":
        mingzi=re_mingzi.findall(i)
        duihua=re_duihua.findall(i)
        
        # print(mingzi[0]+": "+duihua[0])
        jiexijuqing.append(mingzi[0]+": "+duihua[0])
    
    # 第二种类型 无人物文字
    if i[:5] =="[Dial" or i[:5] =="[dial" :
        # print("")
        jiexijuqing.append("")
    
    # 第三种类型 选择支
    if i[:5] =="[Deci" or i[:5] =="[deci" :
        huifulist = re_huifu.findall(i)[0].split(";")
        # print("\n下面是可选择的回复：")
        jiexijuqing.append("\n下面是可选择的回复：")
        j = 1
        for huifu in huifulist:
            # print("    选项{}：".format(j)+huifu)
            jiexijuqing.append("    选项{}：".format(j)+huifu)
            j+=1
    if i[:5] =="[Pred" or i[:5] =="[pred" :
        xuanxianglist = re_xuanxiang.findall(i)
        
        # print("\n下面是回复选项{}的剧情：".format(xuanxianglist))
        jiexijuqing.append("\n下面是回复选项{}的剧情：".format(xuanxianglist))
    
    # 遇到文字直接输出
    if i[:1] !="[":
        # print(i)
        jiexijuqing.append(i)

# 要保存的文件路径
spath = './'
# 要保存的文件名
sfilename = filename+"_jiexi"+".txt"

with open(spath+sfilename, 'w') as f:
    for i in jiexijuqing:
        f.write("\n"+i)
