#!/usr/bin/python
from __future__ import print_function

# You're given binary tree as a sequence of (parent,child) tuples in some random order. In this representation, for example the given tree is represented as : 
#
#    (A,B) (A,C) (B,G) (C,H) (E,F) (B,D) (C,E) 
#   The same tree could be written as an s-expression : 
#   (A(B(D)(G))(C(E(F))(H))) 
#
#    Write a program to translate the first representation into the second.
#  Assumptions: 
# 1) Nodes are single char A-Z
# 2) If left node is null, then entry is blank ie : A, is followed by A,B
# 3) left child tuple will always show up before right child tuple.

import sys,os
from collections import defaultdict

class BTreeNode(object):

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def print_tree(self,end=''):
        if not self.data:
            return
        print(self.data,end=end)
        if self.left or self.right:
            print("(",end=end)

            if self.left:
                self.left.print_tree()

            print(")(",end=end)
            
            if self.right:
                self.right.print_tree()

            print(")",end=end)

"""
    def __str__(self):
        str = "(" + self.data 
        if self.left:
            str_left = self.left.__str__()
        else:
            str_left = "()"

        if self.right:
            str_right = self.right.__str__()
        else:
            str_right = "()"

        str += str_left + str_right + ")"

        return str
"""

parents = set()
children = set()
nodes= dict()

def deserialize(f):
    for line in f:
        parent_data,child_data = line.strip().split(",")

        print("parent_data=",parent_data,"child_data=",child_data)
        child_node = None
        if child_data:
            children.add(child_data)
            if child_data in nodes:
                child_node = nodes[child_data]
            else:
                child_node = BTreeNode(child_data)
                nodes[child_data] = child_node

        parents.add(parent_data)
        if parent_data not in nodes:
            # Left child
            nodes[parent_data] = BTreeNode(parent_data,child_node) 
        else:
            if nodes[parent_data].left is None:
                # Left child
                nodes[parent_data].left = child_node
            else:
                nodes[parent_data].right = child_node
    
    #print("parents_data=",parents)
    #print("children=",children)
    root_data = parents - children
    print("root_data=",root_data)
    for _,node in nodes.iteritems():

        left_data = None
        if node.left:
            left_data = node.left.data
        right_data = None
        if node.right:
            right_data = node.right.data

        print("node.data={0},node.left={1},node.right={2}".format(node.data,left_data,right_data))

    return nodes[root_data.pop()]

if __name__ == "__main__":
    with open(sys.argv[1],"r") as f:
       root = deserialize(f)
       print("root-",root.data)
       root.print_tree()



