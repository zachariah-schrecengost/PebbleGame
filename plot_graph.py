import matplotlib.pyplot as plot
ax = plot.axes()
plot.plot(0,4,'ko')
ax.annotate(1,(0,4))
plot.plot([0,0],[4,3], 'k')
plot.plot(1,4,'ko')
ax.annotate(2,(1,4))
plot.plot(2,4,'ko')
ax.annotate(3,(2,4))
plot.plot([2,1],[4,3], 'k')
plot.plot(3,4,'ko')
ax.annotate(4,(3,4))
plot.plot([3,2],[4,3], 'k')
plot.plot(0,3,'ko')
ax.annotate(6,(0,3))
plot.plot([0,1],[3,4], 'k')
plot.plot(1,3,'ko')
ax.annotate(7,(1,3))
plot.plot(2,3,'ko')
ax.annotate(8,(2,3))
plot.plot([2,1],[3,2], 'k')
plot.plot(3,3,'ko')
ax.annotate(9,(3,3))
plot.plot([3,2],[3,2], 'k')
plot.plot(0,2,'ko')
ax.annotate(11,(0,2))
plot.plot([0,1],[2,3], 'k')
plot.plot(1,2,'ko')
ax.annotate(12,(1,2))
plot.plot([1,1],[2,1], 'k')
plot.plot(2,2,'ko')
ax.annotate(13,(2,2))
plot.plot(3,2,'ko')
ax.annotate(14,(3,2))
plot.plot(0,1,'ko')
ax.annotate(16,(0,1))
plot.plot([0,1],[1,2], 'k')
plot.plot(1,1,'ko')
ax.annotate(17,(1,1))
plot.plot([1,2],[1,2], 'k')
plot.plot(2,1,'ko')
ax.annotate(18,(2,1))
plot.plot([2,3],[1,2], 'k')
plot.plot(3,1,'ko')
ax.annotate(19,(3,1))
plot.plot([3,2],[1,1], 'k')
plot.show()
