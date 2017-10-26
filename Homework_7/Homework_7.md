# 第七次作业#

## · 摘要 ##
本次作业完成了第七次作业，重现了课本的研究过程，并使用欧拉法完成了3.12题的实现：

>***研究庞加莱截面在不同外力相位取值时的情况，与Figure 3.9进行比较。**
>

## · 背景介绍 ##

本次作业将讨论同时考虑线性、强迫力以及摩擦这三种因素的单摆的运动轨迹，也就是所谓的物理摆。

物理摆有许多性质与简单单摆一致，但是也有很多自身独有的奇特性质。其中最重要的可能就是所谓的混沌现象。

由教材
式（3.18），（3.19）

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_7/7-6.jpg)

其中,设置

g=9.8

l=9.8

q为摩擦系数

F_d为强迫力

Ω_d为强迫角频率

由于作业本身就要求与3.9比较，我索性从3.6开始重现课本的思路（真的不是凑字数）

##· 正文 ##

#### 1.不同驱动力下物理摆的运动

运行程序

[word7-1](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_7/Word7-1.py)

[word7-2](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_7/Word7-2.py)


![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_7/7-1.png)


![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_7/7-2.png)

图中蓝色线表示Force=0的状态，可见没有外界驱动力下的单摆在阻力的影响下很快就停止了。

图中红线表示Force=0.5时的运动，可见单摆在开始阶段将初始条件决定的运动通过阻力消耗后，在之后的运动中做与外力同频率的简谐振动。

这两种单摆的运动与上一篇文章中描述的一样。

绿色的线表示Force=1.2时的运动状态，可以看到，单摆的运动是没有周期性的，这就是混沌的特征。图中竖直的线是由于当角度超过180度时，程序将其角度自动减小360度，反之亦然。

然后这里就出了点bug

我也不知道为什么第一幅图30s后就跟课本的Figure 3.6不一样了。但是感觉好像我的还规律一些（虽然本来就是没规律的）

可能是程序的问题？但是问了学长学姐也没有好的答案，同级貌似没有像我这样无耻的从3.6开始做的

#### 2.混沌摆对初值的敏感性

混沌摆的最大特征是当初值仅仅改变了一点点时，结果就会有极大的变化。为了示意这种情况，选择两个摆，它们的初始角度仅仅相差0.001rad。之后观察它们分别在F=1.2（混沌）和F=0.5（非混沌）的情况下角度之差的变化规律。

运行程序[word7-3](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_7/Word7-3.py)

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_7/7-3.png)

蓝线为Force=0.5的情况。由图可知，对于两个初始位置差异很小的非混沌摆，其角度差会迅速减小，最终趋于0.这表明非混沌摆对初值不敏感。

绿线为Force=1.2的情况。由图可知，在混沌状态下，初始角度相差极小的两个物理摆的角度差随着时间推移会变大，最终趋于稳定。

#### 3.混沌摆的角度与角速度的关系

运行程序[word7-4](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_7/Word7-4.py)


![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_7/7-4.jpg)

图像与课本Figure 3.8完美符合。撒花。感动。

红线为Force=0.5，即非混沌情况下单摆的角度与角速度的关系。由图可见，除开最初的一段线，这关系基本上是一个椭圆，这表明对应每一个角度由两个角速度，反之亦然。最终的轨迹与初始值无关，这与上面的结论相合，也是符合简谐振动的规律的。

绿线为Force=1.2，即混沌情况下的单摆的角度与角速度的关系。这里的图像明显比非混沌情况要复杂，但可以明显看出图像上的点并不是随机的，其中有一定的规律性。混沌系统一般都会显示这类的规律性。 


#### 4.exercise 3.12 研究庞加莱截面在不同外力相位取值时的情况，与Figure 3.9进行比较。

终于进入正题了

运行程序[word7-5](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_7/Word7-5.py)

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_7/7-5.png)

Figure 3.9为t=驱动力周期倍数的时刻的情况

excise 3.12对t为不同外力相位的情况进行了讨论

可以看到，随着相位从0到pi/4再到pi/2，图像明显逐渐移动

## · 结论 ##

数值分析表明，混沌图像有一定规律性。参数的变化对混沌状态有较大影响，且混沌摆角度对初值依赖性也很大。庞加莱截面在不同外力相位取值时的情况下，逐渐移动。

## · 致谢 ##

感谢华扬学姐，借鉴了代码。
感谢南京大学邹聪同学，提供了修改意见
