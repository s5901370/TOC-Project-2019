from pygraphviz import *
G=AGraph(strict=False,directed=True)
G.add_node('user')
G.add_node('Q1')
G.add_node('Q2')
G.add_node('Q3')
G.add_node('Q4')
G.add_node('Q5')

G.add_edge('user','Q1')
G.add_edge('Q1','Q2')
G.add_edge('Q2','Q3')
G.add_edge('Q3','Q4')
G.add_edge('Q4','Q5')
G.add_edge('Q5','user')
e = G.get_edge('user','Q1')
e.attr['label'] = 'advance'
e = G.get_edge('Q1','Q2')
e.attr['label'] = 'advance'
e = G.get_edge('Q2','Q3')
e.attr['label'] = 'advance'
e = G.get_edge('Q3','Q4')
e.attr['label'] = 'advance'
e = G.get_edge('Q4','Q5')
e.attr['label'] = 'advance'
e = G.get_edge('Q5','user')
e.attr['label'] = 'advance'
G.layout(prog='dot')
G.draw('file.png')