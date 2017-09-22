## 第三次作业

### 一、摘要
在屏幕上让自己的名字动起来

### 二、背景介绍
大概就是在上一次的作业上搞点操作玩点新花样吧，可是我觉得我上次作业的第二种方法貌似没有什么进步空间了T_T。所以貌似这次又是一次新的开始

### 三、正文
- level_1

暴力拼图打法好！在直接暴力拼写自己名字(反正关键在动上面就打的首字母缩写省事）的基础上，加上老师上课说的根据老师的提示，使用指令import os，i = os.system('cls')即可清空屏幕上已经显示的"图形"，再输出另外的"帧",即可让图形动起来。再者，使用指令import time，time.sleep(sometime)即可让计
算机输出每帧的间隔可控，避免动画太快。还是比较基础的。

（p.s.一个奇怪的问题是我用spyder运行正常，用jupyter notebook运行无法清屏，不是很懂。。。。）

代码在此([戳我戳我](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/homework3/Word3-1.py))

效果展示([戳我戳我](https://pan.baidu.com/s/1boDXIlL))

- level_2

以上方法让我感觉很蠢T_T。因为每次都要打一次输出内容，所以采用了一下的方法二，大体思路是先构造各种字符对应的16进制数表，然后定义函数，并构造空数组b
利用之前的16进制数表在b中填入空或者#输出字符，再用循环控制输出的位置形成移动，就差不多是介个样子了。

代码在此（[戳我戳我](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/homework3/Word3-2.py)）

效果展示([戳我戳我](https://pan.baidu.com/s/1dFaoy8D))

- 假装是level_3

发现大佬们都在用pygame的小球模型，不明觉厉的我也去学习了一下，但是发现学习不懂T_T，这就很难受了。最后秉着留着代码（凑字数）的原则，还是找大佬拿了一段小球在屏幕上弹射的代码充数

代码在此（[戳我戳我](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/homework3/Word3-3.py)）

### 结论
本次作业嘛，主要就是一个import os，i = os.system('cls')代码的应用，基本还在射程之内。level2就属于超纲部分了，这里先提前感谢高中同学的讲解！（待会
致谢还会再说），帮助我理解了level2代码的一些含义和用的语法。至于level3，学习学习大佬的操作就好

### 致谢
提供的pygame代码的[大佬](http://www.cnblogs.com/hongten/p/hongten_pygame_bouncing_ball.html)和提供修改意见的蔡茂睿同学

感谢知道我写level 1 的曾梓龙学长和一同学习的乔敏琛同学

感谢曹一学长的代码指导和南京大学邹聪同学的讲解

以上

