# 第十二次作业

## · 摘要
本次作业完成了第十一次作业，完成了作业4.16题的实现：

>***4.16 实现地球、木星和太阳的真实三体运动模拟**

## · 背景介绍
同第十一次作业。

查询数据可知，太阳的质量约为木星质量的1000倍，地球质量的33万倍

只是三体运动中，计算其中之一的坐标时，要同时考虑另外两个星体对其的引力作用。

同时，因为三个星体都在运动，所以将质心放在原点上更实用，这里就用到了质心公式

![](http://i.imgur.com/OuAO6nJ.jpg)

并且，使太阳也有初速度，从而总动量为0，就可以将系统的质心固定不动。

## · 正文

#### 4.16 实现地球、木星和太阳的真实三体运动模拟

**①以太阳为原点，太阳初始速度为0**

运行程序[the sun origin of 0 initial velocity.py](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/chapter%204/for%20the%20twelfth%20homework/the%20sun%20origin%20of%200%20initial%20velocity.py)

木星质量为其真实质量时

![](http://i.imgur.com/XNaqu99.jpg)

木星质量为其真实质量的10倍时

![](http://i.imgur.com/ipFec0f.jpg)

木星质量为其真实质量的100倍时

![](http://i.imgur.com/dPBe8lx.jpg)

木星质量为其真实质量的1000倍(=太阳质量)时

![](http://i.imgur.com/C4LeUcI.jpg)

**①以太阳为原点，太阳有初始速度，使得总动量为0**

运行程序[the sun origin of 0 total momentum.py](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/chapter%204/for%20the%20twelfth%20homework/the%20sun%20origin%20of%200%20total%20momentum.py)


木星质量为其真实质量时

![](http://i.imgur.com/Qhfjyqz.jpg)

木星质量为其真实质量的10倍时

![](http://i.imgur.com/JAzL15o.jpg)

木星质量为其真实质量的100倍时

![](http://i.imgur.com/FpezVCl.jpg)

木星质量为其真实质量的1000倍(=太阳质量)时

![](http://i.imgur.com/tDR7t05.jpg)

**③以质心为原点，太阳有初始速度，使得总动量为0**

运行程序[the center of mass origin of 0 initial velocity.py](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/chapter%204/for%20the%20twelfth%20homework/the%20center%20of%20mass%20origin%20of%200%20initial%20velocity.py)


木星质量为其真实质量时

![](http://i.imgur.com/EvwUgwy.jpg)

木星质量为其真实质量的10倍时

![](http://i.imgur.com/52MKJwZ.jpg)

木星质量为其真实质量的100倍时

![](http://i.imgur.com/9b3eWMj.jpg)

木星质量为其真实质量的1000倍(=太阳质量)时

![](http://i.imgur.com/ZxqwOnX.jpg)


## · 结论

**可以看出：**

**1.增加太阳初始速度使总动量为0时，轨道扰动最小**

**2.质心原点与太阳原点图像上没有很大差异**

**3.随着木星质量的变大，轨道扰动加大，地球轨道偏差变化较大。当木星质量与太阳相等时，变成太阳与木星的两体运动，地球由于质量太小接近于两体系统的卫星。**

## · 致谢

感谢华扬同学，借鉴了代码与报告。

感谢南京大学邹聪同学对代码错误提供了修改方法
