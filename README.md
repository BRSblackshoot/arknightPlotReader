# 明日方舟解包剧情阅读器

## 目录

*   [说明](#说明)

*   [目标](#目标)

*   [转换文本](#转换文本)

    *   [文本类型](#文本类型)
    *   [代码思路](#代码思路)
    *   [代码](#代码)

# 说明

之前在NGA看到别人写了一个明日方舟纯文本阅读网站，数据从PRTS获取

现在偶然间知道了解包大佬通常在外网直播解包，并且在Github上创建了一个仓库叫ArknightsGameDate，通过工作流随时更新方舟各服(中日英韩)的最新数据

github链接：[https://github.com/Kengxxiao/ArknightsGameData](https://github.com/Kengxxiao/ArknightsGameData "https://github.com/Kengxxiao/ArknightsGameData")

简单介绍一下，找到zh\_CN文件夹，这里是国服数据，子文件夹里的level和story分别是关卡数据和过场剧情 &#x20;

story里的obt/main是主线剧情，activities是各支线活动剧情 &#x20;

比如说story/obt/main/level\_main\_10-01\_beg.txt 就是10-1的剧情 &#x20;

干员在character\_table里面，不过建议善用关键词搜索，里面干员是用的代号

其他的文件也差不多一看就懂

这个仓库里的数据算是最快获取数据的地方了，更快就要自己学会解包

# 目标

prst有点奇怪，有的时候会等服务器开了才把剧情放出来，有的时候（比如现在主线10章开启期间）服务器还没开放，就把剧情放到prst了

所以为了我个人方便，就打算写一个纯文本阅读器，将每次大更新时，解包大佬发布的剧情转为纯文本然后发出来，瞄准以下情况：

1.  PRTS没有立刻发布更新的剧情

2.  早上10点到下午16点这个时间段想看新剧情但是不太想看解包大佬给的那几千行带源码的剧情包

# 转换文本

## 文本类型

先不考虑如何拿到txt文件，就当做本地已经有了，并且不考虑web开发，就考虑单机情况下，将剧情包转为便于阅读的文本

目前看到的文本内容有三种

```text
第一种 人物对话框
[name="蔓德拉"]别做梦了——我从来不会让领袖失望！

```

```纯文本
第二种 无人物 在对话框显示文字
[Dialog]
[Blocker(fadetime=2,block=true)]
[Image]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
塔露拉？
辛苦你了，这种天气你还去站岗。
我知道是你自己要求的。
[Character(name="avg_npc_078")]
[name="塔露拉"]  你知道。在我们走出冬天前我的火是不会熄的。
[Character]
[Dialog]

```

```纯文本
第三种 带选择支
[Decision(options="发生什么了！;怎么会......;凯尔希，想想办法！", values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_003_kalts_1")]
[name="凯尔希"]  ......过来，Dr.{@nickname}。
[name="凯尔希"]  接下来我要做的这件事，你不可以告诉任何人。
[name="凯尔希"]  龙门的陈长官！
[Character(name="char_010_chen_1")]
[name="陈"]  不再是了。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]  那就请你帮我看住那边那条龙。之后我们会立刻对她进行收监。你有任何问题吗？
[Character(name="char_010_chen_1")]
[name="陈"]  先照顾阿米娅吧。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Image(fadetime=0)]
[Character(name="char_003_kalts_1")]
[name="凯尔希"]  好。博士，把手伸出来。
[Decision(options="好！;（伸出手）;我就算退后你也会拽住我对不对？",values="1;2;3")]
[Predicate(references="1;2;3")]
```

## 代码思路

基于正则表达式提取需要的字符串

首先将人物对话框的改为`人物名：对话`

然后遇到直接展示的，遇到`[Dialog]`就空一行，后面的文字直接输出

最后遇到选择支的，先把选择支给出，然后分别展示各个选择支回复
