#!/usr/bin/env python
# coding: UTF-8 

import rospy

LOCATION = {
    'door': ['door', 'dog'],
    'kitchen': ['kitchen', 'page', 'station', 'location'],
    'living room': ['living', 'leaving', 'livingroom', 'living room'],
    'bedroom': ['bedroom', 'bad', 'bed room', 'bad room', 'bed', 'bathroom', 'beijing'],
    'hallway': ['hallway', 'whole way'],
    'dining room': ['dining', 'dying'],
    'garage': ['garage']
}


class Analyzer:
    def __init__(self, cmd):
        self.cmd = cmd
        self.goal = None

    def get_goal(self):
        return self.goal


if __name__ == '__main__':
    try:
        Analyzer('name')
    except rospy.ROSInterruptException:
        pass
