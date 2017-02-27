import matplotlib.pyplot as plt
import rigol_ds1104b

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})

osc = rigol_ds1104b.RigolDS1104B("/dev/usbtmc0")

x, y = osc.get_data()

fig, ax = plt.subplots()

ax.plot(x, y, 'r-')
ax.set_xlabel("time [s]", color="red")
ax.set_ylabel("voltage [V]", color="red")
ax.set_axis_bgcolor('green')
plt.grid(True)
plt.show()