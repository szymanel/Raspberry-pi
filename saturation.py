#-*-coding:utf-8-*-

import matplotlib.pyplot as plt
import numpy as np
import hrcalc

# load log data
red = []
with open("./red.log", "r") as f:
    for r in f:
        red.append(int(r))

ir = []
with open("./ir.log", "r") as f:
    for r in f:
        ir.append(int(r))

# x-axis values



saturation = []
for i in range(37):
    #print(hrcalc.calc_hr_and_spo2(ir[25*i:25*i+100], red[25*i:25*i+100]))
    sp_count = hrcalc.calc_hr_and_satur(ir[5*i:5*i+900], red[5*i:5*i+900])
    sp = hrcalc.calc_hr_and_satur(ir[5*i:5*i+900], red[5*i:5*i+900])
    if sp > 85 and sp < 100:
        saturation.append (sp)
        print (sp)
     
    
x = np.arange(len(saturation))

fig = plt.figure()
ax = fig.add_subplot(111)

# RED LED
ax.plot(x, saturation, c="red", label="SATURATION")



# modify limits
ax.set_ylim(80, 100)
# ax.set_xlim(400,600)

# show legend
ax.legend(loc="best")

plt.show()
