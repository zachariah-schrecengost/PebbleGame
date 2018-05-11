import matplotlib.pyplot as plot
ax = plot.axes()
plot.plot(0,4,'ro')
ax.annotate(1,(0,4))
ax.arrow(0,4,1,0,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
ax.arrow(0,4,0,-1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
plot.plot(1,4,'ro')
ax.annotate(2,(1,4))
ax.arrow(1,4,0,-1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
ax.arrow(1,4,1,0,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
plot.plot(2,4,'ro')
ax.annotate(3,(2,4))
ax.arrow(2,4,-1,-1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
ax.arrow(2,4,0,-1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
plot.plot(3,4,'ro')
ax.annotate(4,(3,4))
ax.arrow(3,4,-1,0,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
ax.arrow(3,4,-1,-1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
plot.plot(0,3,'ro')
ax.annotate(6,(0,3))
ax.arrow(0,3,1,0,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
ax.arrow(0,3,1,1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
plot.plot(1,3,'ro')
ax.annotate(7,(1,3))
ax.arrow(1,3,-1,-1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
ax.arrow(1,3,0,-1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
plot.plot(2,3,'ro')
ax.annotate(8,(2,3))
ax.arrow(2,3,0,-1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
ax.arrow(2,3,-1,0,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
plot.plot(3,3,'ro')
ax.annotate(9,(3,3))
ax.arrow(3,3,-1,-1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
ax.arrow(3,3,-1,0,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
plot.plot(0,2,'ro')
ax.annotate(11,(0,2))
ax.arrow(0,2,1,0,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
ax.arrow(0,2,0,1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
plot.plot(1,2,'ko')
ax.annotate(12,(1,2))
plot.plot(2,2,'ro')
ax.annotate(13,(2,2))
ax.arrow(2,2,-1,0,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
ax.arrow(2,2,0,-1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
plot.plot(3,2,'ro')
ax.annotate(14,(3,2))
ax.arrow(3,2,-1,0,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
ax.arrow(3,2,0,1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
plot.plot(0,1,'ro')
ax.annotate(16,(0,1))
ax.arrow(0,1,0,1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
ax.arrow(0,1,1,1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
plot.plot(1,1,'bo')
ax.annotate(17,(1,1))
ax.arrow(1,1,1,1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
plot.plot(2,1,'ro')
ax.annotate(18,(2,1))
ax.arrow(2,1,1,1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
ax.arrow(2,1,-1,0,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
plot.plot(3,1,'ro')
ax.annotate(19,(3,1))
ax.arrow(3,1,-1,0,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
ax.arrow(3,1,0,1,fc="k", ec="k",
head_width=0.05, head_length=0.1, length_includes_head=True)
plot.show()
