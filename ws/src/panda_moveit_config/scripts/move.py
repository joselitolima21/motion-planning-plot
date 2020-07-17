#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

# Imports para o subscriber
import rospy
from sensor_msgs.msg import JointState

def all_close(goal, actual, tolerance):
  
  all_equal = True
  if type(goal) is list:
    for index in range(len(goal)):
      if abs(actual[index] - goal[index]) > tolerance:
        return False

  elif type(goal) is geometry_msgs.msg.PoseStamped:
    return all_close(goal.pose, actual.pose, tolerance)

  elif type(goal) is geometry_msgs.msg.Pose:
    return all_close(pose_to_list(goal), pose_to_list(actual), tolerance)

  return True

class MoveGroupPythonIntefaceTutorial(object):
  def __init__(self):
    super(MoveGroupPythonIntefaceTutorial, self).__init__()

    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_group_python_interface_tutorial',
                    anonymous=True)

    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()

    group_name = "panda_arm"
    group = moveit_commander.MoveGroupCommander(group_name)

    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=20)

    self.box_name = ''
    self.robot = robot
    self.scene = scene
    self.group = group
    self.display_trajectory_publisher = display_trajectory_publisher
    # self.planning_frame = planning_frame
    # self.eef_link = eef_link
    # self.group_names = group_names

  def go_to_joint_state(self):
    group = self.group

    joint_goal = group.get_current_joint_values()
    joint_goal[0] = 0
    joint_goal[1] = 0.6393
    joint_goal[2] = -0.2547
    joint_goal[3] = -2.412
    joint_goal[4] = -0.9552
    joint_goal[5] = 3.1932
    joint_goal[6] = 1.8148

    group.go(joint_goal, wait=True)
    
    joint_home = group.get_current_joint_values()
    joint_home[0] = 0
    joint_home[1] = -0.0194
    joint_home[2] = -0.2547
    joint_home[3] = -0.9605
    joint_home[4] = -1.9103
    joint_home[5] = 3.5246
    joint_home[6] = -0.0318

    group.go(joint_home, wait=True)
    
    group.stop()

    current_joints = self.group.get_current_joint_values()
    
    return all_close(joint_goal, current_joints, 0.01)

  def go_to_pose_goal(self):
    group = self.group
  
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.orientation.w = 1.0
    pose_goal.position.x = 0.4
    pose_goal.position.y = 0.1
    pose_goal.position.z = 0.4
    group.set_pose_target(pose_goal)

    plan = group.go(wait=False)

    group.stop()
    group.clear_pose_targets()

    current_pose = self.group.get_current_pose().pose
    return all_close(pose_goal, current_pose, 0.01)

  # Funcoes para o subscriber
  def callback(self,data):
    rospy.loginfo(data.position)
    rospy.loginfo(data.velocity)
    
  def listener(self):
    rospy.Subscriber("/joint_states", JointState, self.callback)
    rospy.spin()


# Funcao principal
def main():
  try:
    print "=============== Iniciando o programa ================"
    tutorial = MoveGroupPythonIntefaceTutorial()

    print "== Comecando a executar o movimento e ler os dados =="
    tutorial.go_to_joint_state()
    # tutorial.listener()
    print "============== Finalizando o programa ==============="
    sys.exit(0)
  except rospy.ROSInterruptException:
    return
  except KeyboardInterrupt:
    return

if __name__ == '__main__':
  main()
