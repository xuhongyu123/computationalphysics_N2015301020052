# 第八次作业

## · 摘要 
本次作业完成了第八次作业，按照课本顺序研究了洛伦兹模型，完成了 3.26题的实现：

>***在不同的区域(in different regimes)构建Figure 3.16和Figure 3.17的相空间图像。**

regimes我理解为不同坐标，相平面。

## · 背景介绍
由教材，大气物理学家Lorenz在研究Rayleigh-Benard问题时，将流体力学基本方程组Navier-Stokes方程组化简为简单形式： 

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/8-1.jpg)

这个方程组被称为Lorenz方程组，或Lorenz模型。其中x,y,z为变量，其余为常数。

遵照惯例，设

sigma=10

b=8/3

##· 正文 ##

#### **1.Figure 3.15——Lorentz模型在不同r下的行为**

运行程序[word8-1](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/Word8-1.py)

改变r的大小，观察z随时间的变化情况。在这个模型中，r代表了流体顶部与底部的温度差，类似于单摆问题中外界驱动力的地位。

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/8-2.png)

可以看到，与课本Figure3.15完全符合

同时，观察x,y随时间的变化情况

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/8-3.jpg)

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/8-4.jpg)

r=5时，图像一开始有一点振荡，随后振幅衰减，x,y,z变成一个与时间无关的常数。

r=10时，图像的特征相似，只是振幅衰减所花的时间要更长一些。

这两种情况对应于流体中的稳定对流运动。它类似于非混沌单摆的运动模式。

r=25时，图像变为混沌状态。

#### **2.Figure 3.16——相空间中的混沌lorenz模型**

运行程序[word8-2](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/Word8-2.py)

首先看x-z平面的

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/8-8.png)

可以看到，与Figure3.16完全符合

然后是x-y平面的

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/8-5.jpg)

然后是y-z平面

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/8-6.jpg)

可见 满足Wikipedia “Lorenz system”词条的示意图

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/8-7.gif)

A sample solution in the Lorenz attractor when ρ = 28, σ = 10, and β = 8/3

非混沌状态（r=5,10）图像会汇聚到一个点，代表系统处于稳定状态。混沌状态（r=25）与混沌摆的情况类似。事实上这个图像非常眼熟——在进行“混沌通信”实验中示波器上显示的就是这样的图像。



#### **3.Figure 3.17——相空间中的混沌lorenz模型**

运行程序[word8-3](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/Word8-3.py)


这里x=0,y=0的条件由x,y绝对值≤0.01代替

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/8-9.png)

可以看到，与Figure3.17完全符合


#### **4.Figure 3.18——混沌转变**

运行程序[word8-4](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/Word8-4.py)

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/8-10.png)

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/8-11.png)

与Figure 3.18相吻合。

r=160，系统是周期性的。

r=163.8，系统开始出现一些非周期的因素，也就是开始变得混沌。

不过这里并不太明白与同样条件的Figure 3.15讨论的区别，为什么随着r增加，先出现非周期性（混沌状态），然后出现周期性，最后又出现非周期性（混沌状态）？

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework-8/8-2.png)



## · 结论

①改变r的大小，观察z随时间的变化情况。在这个模型中，r代表了流体顶部与底部的温度差，类似于单摆问题中外界驱动力的地位。

r=5时，图像一开始有一点振荡，随后振幅衰减，x,y,z变成一个与时间无关的常数。

r=10时，图像的特征相似，只是振幅衰减所花的时间要更长一些。

这两种情况对应于流体中的稳定对流运动。它类似于非混沌单摆的运动模式。

r=25时，图像变为混沌状态。

r=160，系统是周期性的。

r=163.8，系统开始出现一些非周期的因素，也就是开始变得混沌。

似乎随着r增加，先出现非周期性（混沌状态），然后出现周期性，最后又出现非周期性（混沌状态）。

具体原因有待进一步研究

②非混沌状态（r=5,10）的相空间混沌图像会汇聚到一个点，代表系统处于稳定状态。混沌状态（r=25）与混沌摆的情况类似。


## · 致谢

感谢吴雨桥同学，借鉴了代码与报告。

感谢华扬同学的指导
