from matplotlib import pyplot as plt

print(plt.style.available)
# plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')
plt.xkcd()
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
# plt.plot(dev_x,dev_y,'k--',label='all devss')
# plt.plot(dev_x,dev_y,color='k',linestyle='--',marker='.',label='all devss')
# py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
# plt.plot(dev_x,py_dev_y,'b',label='py devs')
plt.plot(dev_x,py_dev_y,color='b',linestyle='-.',marker='o',linewidth=3,label='py devs')
plt.plot(dev_x,py_dev_y,label='py devs')
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
# plt.plot(dev_x,js_dev_y,color='#239944',linewidth=3,label='js_devs')
plt.plot(dev_x,js_dev_y,label='js_devs')
plt.plot(dev_x,dev_y,color='k',linestyle='--',marker='.',label='all devss')

plt.title('Median avg salary (USD) by ages')
plt.xlabel('Ages')
plt.ylabel('Salaries (USD)')
# plt.legend(['all devs','py devs'])
plt.legend()
plt.tight_layout()
# plt.grid(True)
plt.savefig('plot.png')
plt.show()