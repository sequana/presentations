# Creates the images used in the slides (flow for the section from sequentials
# to dependent graph

from cno import CNOGraph
from pylab import savefig, figure

figure(figsize=(6,9))

c = CNOGraph()
node1 = "command line"
node2 = "Shell script"
node3 = "Makefile"
node4 = "Snakefile"

c.add_reaction("%s=%s" % (node1, node2))
c.add_reaction("%s=%s" % (node2, node3))
c.add_reaction("%s=%s" % (node3, node4))
c.plot()
savefig("flow_methods.png")


for i, node in enumerate([node1, node2, node3, node4]):
    c._stimuli = [node]
    c.plot()
    savefig("flow_methods_%s.png" % (i+1))


