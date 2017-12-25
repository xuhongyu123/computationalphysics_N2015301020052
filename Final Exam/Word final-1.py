import numpy as np
import matplotlib.pylab as plt

x = np.linspace(0, 30, 1000)
V_1=0.5-1/x+0.5/x**2
V_2=0.5-1/x+2/x**2
V_3=0.5-1/x+4.5/x**2
V_4=0.5-1/x+8/x**2
V_5=0.5-1/x+12.5/x**2

plt.plot(x,V_1,'-',label='L=1',linewidth=2)
plt.plot(x,V_2,'-',label='L=2',linewidth=2)
plt.plot(x,V_3,'-',label='L=3',linewidth=2)
plt.plot(x,V_4,'-',label='L=4',linewidth=2)
plt.plot(x,V_5,'-',label='L=5',linewidth=2)
plt.ylim(0,0.8)
plt.title(u'Newtonian Gravity massive particles', fontsize=16,fontproperties='STSong')
plt.xlabel('r')
plt.ylabel('V(r)')
plt.legend(loc='upper right')
plt.show()


import numpy as np
import matplotlib.pylab as plt

x = np.linspace(0, 30, 1000)
V_1=0.5/x**2
V_2=2/x**2
V_3=4.5/x**2
V_4=8/x**2
V_5=12.5/x**2
plt.plot(x,V_1,'-',label='L=1',linewidth=2)
plt.plot(x,V_2,'-',label='L=2',linewidth=2)
plt.plot(x,V_3,'-',label='L=3',linewidth=2)
plt.plot(x,V_4,'-',label='L=4',linewidth=2)
plt.plot(x,V_5,'-',label='L=5',linewidth=2)
plt.ylim(0,0.8)
plt.title(u'Newtonian Gravity massless particles', fontsize=16,fontproperties='STSong')
plt.xlabel('r')
plt.ylabel('V(r)')
plt.legend(loc='upper right')
plt.show()


import numpy as np
import matplotlib.pylab as plt
x = np.linspace(0, 30, 1000)
V_1=0.5-1/x+0.5/x**2-1/x**3
V_2=0.5-1/x+2/x**2-4/x**3
V_3=0.5-1/x+4.5/x**2-9/x**3
V_4=0.5-1/x+8/x**2-16/x**3
V_5=0.5-1/x+12.5/x**2-25/x**3

plt.plot(x,V_1,'-',label='L=1',linewidth=2)
plt.plot(x,V_2,'-',label='L=2',linewidth=2)
plt.plot(x,V_3,'-',label='L=3',linewidth=2)
plt.plot(x,V_4,'-',label='L=4',linewidth=2)
plt.plot(x,V_5,'-',label='L=5',linewidth=2)
plt.ylim(0,0.8)
plt.title(u'General Relativity massive particles', fontsize=16,fontproperties='STSong')
plt.xlabel('r')
plt.ylabel('V(r)')
plt.legend(loc='upper right')
plt.savefig('V-r 1')
plt.show()


import numpy as np
import matplotlib.pylab as plt

x = np.linspace(0, 30, 1000)
V_1=0.5/x**2-1/x**3
V_2=2/x**2-4/x**3
V_3=4.5/x**2-9/x**3
V_4=8/x**2-16/x**3
V_5=12.5/x**2-25/x**3

plt.plot(x,V_1,'-',label='L=1',linewidth=2)
plt.plot(x,V_2,'-',label='L=2',linewidth=2)
plt.plot(x,V_3,'-',label='L=3',linewidth=2)
plt.plot(x,V_4,'-',label='L=4',linewidth=2)
plt.plot(x,V_5,'-',label='L=5',linewidth=2)
plt.ylim(0,0.8)
plt.title(u'General Relativity massless particles', fontsize=16,fontproperties='STSong')
plt.xlabel('r')
plt.ylabel('V(r)')
plt.legend(loc='upper right')
plt.show()
