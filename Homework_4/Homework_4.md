## 第四次作业
### 一、摘要
本次作业内容为教材课后习题1.5：两种原子核各有几率衰变成另一种核，因此它们的衰变规律将由两个互相耦合的一阶线性微分方程描述。我采用课本上介绍的
欧拉方法来解决此问题，并用图像表示出了两种核数目随时间的变化规律。 

通过本次作业的练习，我终于基本掌握了用python绘图的方法，另外，也第一次通过自己写程序来解决微分。

### 二、背景介绍
题目1.5课本习题1.5 Consider again  a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into ones of type B, while nuclei of type B decay into ones of type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The correponding rate equation are   
　　　　　　　　　　　　　　　d N_A /dt = N_B/tau - N_A/tau  
　　　　　　　　　　　　　　　d N_B /dt = N_A/tau - N_B/tau  
where for simplicity we have assumed that the two types of decay are characterized by the same time constant, tau. Solve this system of equations for the numbers of nuclei, N_A and N_B, as functions of time. Consider different initial conditions, such as N_A=100, N_B=0, etc., and take tau =1s. Show that you numerical results are consistent with the idea that the system reaches a steady state in which N_A and N_B are constant. In such a steady state, the time dericatives dN_A/dt and dN_B/dt should vanish.
 
 主要为参考上课讲的例题利用matplotlib进行绘图和用程序解微分方程
 
 ### 三、正文
 - 例题回顾
 
 之所以有这一段是因为这一段完全反应了我对本次作业的学习过程
 
 首先尝试去重现课本例题，衰变曲线。课本范例运用的原理通俗讲就是设定dt，然后前一步得到的点变成后一步的初始点这样，一步步推进，去找点画线。
 
 看了老师上传的uranium decay的范例后，由于上课开了小差（罪过罪过），只能把看得懂的代码提炼出来
 ![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_4/4-1.png)
 
其中

n_uranium是粒子初始总数，设定的是一个list，然后往里面添加（.append）的形式。

t是经过的时间，同样是个list，初始值为0。

tau为时间常数，仔细对比衰变公式，其值其实对应的是半衰期的-1/ln2倍，一般定义为“平均寿命”的含义。

dt是步长，每走一步间隔多长时间。

n是走了几步。

然后添加输入值。

最后网上查找Co元素的半衰期为5.27年，设初始有1000个粒子，代入数据得到的图像是这样的。
 ![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_4/4-2.png)
 
 好像和老师弄出来的图也差不多
 
 但是抱着探索的精神，我又一次去麻烦了精通python的基友，以一顿饭的代价像他虚心学习了一波。了解到老师给的代码中我删掉的四个函数目的是鼓励用一个个函数来代替重复的程序，用一个个函数的话，对于程序来说，调用更方便，看起来程序更干净，懂吧

 initialize为初始化函数，用于定义数据组、给出初始条件，利用这个函数配上global数据可以实现多次输入
 
 calculate为计算函数，相当于写一个fx，这样后面的给定自变量就能直接运算出结果不用再写
 
 store和read顾名思义分别是储存和读取函数，保证每次运行的结果都有记录并且之后能够调用
 
 由于例题中我们只进行了一次简单的运算，所以以上四个函数可有可无。
 
 - 习题
 
终于来到正题了。在了解了例题的代码法则之后，在例题的基础上进行相应的函数修改即可实现本题。由于这个题看起来很复杂所以我不敢像上面那样删掉四个函数，所以在没有完全弄懂这四个函数的情况下我本来想恬不知耻的依葫芦画瓢把四个函数抄了过来。

为解决课本上的习题，需用到的的函数库有
　　　　　　import pickle；
　　　　　　from pylab import *；
　　　　　　import numpy as py；
其中第一个是用来导入、导出数据的；第二个则是绘图的函数库；第三个用来制造数组极为方便。
  
然后是关于微分方程的解法，这里采用书上介绍的欧拉法

欧拉法的原理是将微分方程化为差分方程，并利用前一时刻的结果来计算后一时刻的结果，反复迭代即得到变量对时间的依赖关系。欧拉法要能求得比较精确的解，步长的选取是十分关键的。一般来说，选取原则是：步长必须小于系统中任意的特征参数(例如，本题中就是要小于衰变的特征时间)。

本次计算中，衰变特征时间tau=10，取步长分别为四种情况：5.0, 2.0， 1.0， 2.0，0.5, 由此分别计算出数值解并作图(如下左图)。另外，为更直观地表示出各情况数值计算的精度，分别计算了各情况数值解与解析结果的偏差(如右下图)。可以发现，在步长为时间常数的1/2时,数值解偏离正确值很大，在核数为1000左右的情况下，计算偏差能达到200；而当步长减小时，计算误差则也减小；当步长仅为时间常数的1/20时，数值偏差衰减到不足20，此时可以认为计算精度比较满意。

源代码在此[戳我戳我](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_4/Word4.py)

指令框

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_4/4-3.png)

数值结果[txt数据](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_4/text_4)

效果图

![](https://github.com/zhaozhanyi0804/computationalphysics_N2015301020052/blob/master/Homework_4/4-4.png)

### 四、结论
matplotlib使用起来非常方便，但是由于一直想着想把图像画到同一张图上。所以强行增加了工作难度，最后请教了学长才勉强完成代码。对四个函数的使用和对如何编辑方程与计算有了新的体会，也算小有成就吧

### 五、致谢
感谢陈遥洋学长的代码指导

感谢南京大学的邹聪同学对我在使用函数上的帮助和语法上的排bug

感谢caihao老师的作业例子[点击进入](https://github.com/caihao/computational_physics_whu/tree/master/chapter1)

感谢matplotlib的教程[点击进入](http://liam0205.me/2014/09/11/matplotlib-tutorial-zh-cn/) 

感谢python的数据读取和写入教程[点击进入](http://www.ibm.com/developerworks/cn/opensource/os-python8/)




 


 
