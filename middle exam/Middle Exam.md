# 期中作业
## · 摘要
用pygame写一个游戏。我记得好像是要求写发射炮弹的游戏？时隔已久，记不清了。

哥几个都是随便学习的一个游戏的写法就写了

于是我也就这样了，不过选了两个感觉和老师的要求以及物理模型有关的游类型：弹球和坦克对轰

## · 背景介绍
Pygame 是一组用来开发游戏软件的 Python 程序模块，基于 SDL 库的基础上开发。允许你在 Python 程序中创建功能丰富的游戏和多媒体程序，Pygame 是一个高可移植性的模块可以支持多个操作系统。用它来开发小游戏非常适合。

以上引用自百度

安装过程如图

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/middle%20exam/%E6%9C%9F%E4%B8%AD1.png)

其实对于我这种小白来说，pygame就是从零开始的异世界冒险

努力学习了一整个星期，还是停留在借鉴他人源代码基础上

但是好歹掰出了点东西

## · 正文
### ***1.弹球弹弹弹***
很基础的游戏了，就是一堆球在框里谈来谈去，手动修改数量和速度改变弹球运动状态

源代码戳这里[word m-1](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/middle%20exam/Word%20middle-1.py)

运行需要的文件在这里[data-1](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/tree/master/middle%20exam/data%201)

运行的效果大概是这样

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/middle%20exam/%E6%9C%9F%E4%B8%AD2.gif)

然后我很骚的学会了怎么加bgm，但是好像只能加wav文件，而改成这个文件之后好听的歌就变了，所以随便搞了一个调子
### ***2.坦克对轰***
其实是一个很没有技术含量的游戏

我觉得我主要干的事情就是贴图

坦克都是平射加农炮（主要是懒得设计抛物线轨迹什么的）

A和D键左右移动（虽然移动没啥用),J射击，漏掉五辆坦克就lose，至于win嘛...貌似没有，可以一直刷敌军（刺激吧）

源代码戳这里[word m-2](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/middle%20exam/Word%20middle-2.py)

需要的文件在这里[data2](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/tree/master/middle%20exam/data%202)

简单的展示一下界面，过程中本人在疯狂按J。

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/middle%20exam/%E6%9C%9F%E4%B8%AD3.gif)

希望老师玩的开心（好像毫无可玩性），也住院老师早日康复！！！

## · 结论
没啥结论...写的很痛苦算么

## · 致谢
感谢室友教我安装pygame

感谢南京大学邹聪同学给我参考了他用flash做的游戏（没啥参考性）

参考网站

[用Python和Pygame写游戏-从入门到精通](https://eyehere.net/2011/python-pygame-novice-professional-1/)

[【python游戏编程之旅】](http://www.cnblogs.com/msxh/p/4966899.html)

[python开发_tkinter_小球完全弹性碰撞游戏](http://www.cnblogs.com/hongten/archive/2013/09/28/hongten_python_pong.html)

[pygame系列_小球完全弹性碰撞游戏](https://www.cnblogs.com/hongten/p/3369278.html)

[pygame坦克大战小游戏](http://bbs.fishc.com/forum.php?mod=viewthread&tid=81941&extra=page%3D1&page=1)


