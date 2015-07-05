#!/usr/bin/python
from __future__ import print_function

__author__ = "akarmarkar"

import itertools
from functools import partial
from copy import deepcopy
from itertools import repeat
from optparse import OptionParser

"""
Given k containers of capacities c1,c2,c3...ck and a target level t, write a
program that measures out exactly t liters of water from a pool using the k
containers.
"""

class Container(object):
   def __init__(self, id, capacity, initial_level=0):
      self.id = id
      self.capacity = capacity
      self.level = initial_level

   @property
   def residual_cap(self):
      return self.capacity - self.level

   def is_empty(self):
      return self.level == 0

   def is_full(self):
      return self.residual_cap == 0

   def __repr__(self):
      return "{0}->({1}/{2})".format(self.id, self.level, self.capacity)

   def __eq__(self, other):
      return self.id == other.id and self.capacity == other.capacity and \
             self.level == other.level

   def op_empty(self):
     """Empty container {0}(drain {1} liters)"""
     str = self.op_empty.__doc__.format(self.id, self.level)
     self.level = 0
     return str

   def op_fill(self):
     """Top up container {0}(fill {1} liters)"""
     str = self.op_fill.__doc__.format(self.id,self.residual_cap)
     self.level = self.capacity
     return str

   def op_transfer_until_full(self, target_container):
      """Transfer {0} liters from container {1} to container {2}"""

      # If target container has less or equal residual space than the fluid level
      # present in the source container, then transfer the entire residual level
      # target_container will be full to the brim
      if target_container.residual_cap <= self.level:
         transferred_liters = target_container.residual_cap
         self.level -= target_container.residual_cap
         target_container.level = target_container.capacity
      else:
         # Some residual capacity will be present.
         transferred_liters = self.level
         target_container.level += self.level
         self.level = 0

      return self.op_transfer_until_full.__doc__.format(
         transferred_liters, self.id, target_container.id)

class State(object):
   def __init__(self, containers, target_level, transitions=None):
      self.containers = deepcopy(containers)
      if transitions is None:
         self.transitions = [str(self)]
      else:
         self.transitions = deepcopy(transitions)
      self.target_level = target_level

   @staticmethod 
   def clone(state):
       return deepcopy(state)

   def __eq__(self, other):
      return self.containers == other.containers

   def __repr__(self):
      return "{0}".format(self.containers)

   def gen_op_empty(self):
      """Empty container {0}(drain {1} liters)"""
      for container in self.containers:
         if container.level > 0:
            new_state = State(self.containers, self.target_level,
                              self.transitions)
            container = new_state.containers[
               new_state.containers.index(container)]
            new_state.transitions.append(str(new_state) + ": " +
                                         container.op_empty())
            yield new_state

   def gen_op_fill(self):
      """Top up container {0}(fill {1} liters)"""
      for container in self.containers:
         if container.level < container.capacity:
            new_state = State.clone(self)
            container = new_state.containers[
               new_state.containers.index(container)]
            new_state.transitions.append(str(new_state) + ": " +
                                         container.op_fill())
            # new_state.transitions.append(str(new_state))
            yield new_state

   def gen_op_transfer_until_full(self):
      # Pick permutations of src and tgt containers
      for src, tgt in itertools.permutations(
            self.containers, 2):
         # transfer operation is valid only if src container is not completely
         # empty and tgt container is not full to the brim.
         if not src.is_empty() and not tgt.is_full():
            new_state = State.clone(self)

            src = new_state.containers[new_state.containers.index(src)]
            tgt = new_state.containers[new_state.containers.index(tgt)]

            new_state.transitions.append(str(new_state) + ": " +
                                         src.op_transfer_until_full(tgt))
            yield new_state

   def generate_ops_states(self):
      for state in self.gen_op_empty():
         yield state
      for state in self.gen_op_fill():
         yield state
      for state in self.gen_op_transfer_until_full():
         yield state

   def is_solved(self):
      """
      Helper method to check if current state is the terminal state. ie:
      Puzzle is solved.
      :param s:
      :param target_level:
      :return: True/False.
      """
      for c in self.containers:
         if c.level == self.target_level:
            self.transitions.append("Your target level {0} is in "
                                    "container {1}".format(
               self.target_level, c.id))
            return True
      return False

# states is a dict of seen states.
states = {}

class Puzzle(object):
   def __init__(self, containers, target_level, quit_on_first_soln=False):
      self.containers = containers
      self.target_level = target_level
      self.quit_on_first_soln = quit_on_first_soln
      self.solutions = []

   def solve(self):
      states_to_process = [State(self.containers, self.target_level)]
      current_index = 0

      while current_index < len(states_to_process):

         current_state = states_to_process[current_index]

         if current_state.is_solved():
            self.solutions.append(",\n".join(current_state.transitions))
            current_index += 1
            if self.quit_on_first_soln:
               break
            continue

         if __debug__:
            print("Processing: ", current_state)

         for new_state in current_state.generate_ops_states():

            if new_state not in states_to_process:
               states_to_process.append(new_state)
               if __debug__:
                  print("Generated: ", new_state)

         current_index += 1

      return self

   def __repr__(self):
      if not self.solutions:
         return "No solution !"
      else:
         str = ''
         for index, soln in enumerate(self.solutions):
            str += "solution {0} = {1}\n\n".format(index, soln)

         return str


if __name__ == '__main__':
   parser = OptionParser()
   parser.add_option("-t", "--target", dest="target", type="int",
                     help="target level", metavar="target", action="store")
   parser.add_option("-c", "--container", dest="containers", type="int",
                     help="target level", metavar="containers",
                     action="append")
   parser.add_option("-o", "--one-solution", dest="quit_on_first_soln",
                     help="Quit after generating first solution",
                     metavar="quit_on_first_soln",
                     action="store_true")

   (options, args) = parser.parse_args()
   if options.target is None:
      parser.error('target not given')
   if not options.containers:
      parser.error('container(s) not given')
   if len(options.containers) == 1:
      parser.error('Only 1 container given. Min - 2, Max - 5.')

   containers = []
   for index, capacity in enumerate(options.containers, 0):
      label = chr(ord('A') + index)
      containers.append(Container(label, capacity))
   print(Puzzle(containers, options.target,
                 options.quit_on_first_soln).solve())
