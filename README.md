# createbotlabs

DESIGN 

DESIGN OF THE H BOT GANTRY MECHANISM 

Structure Description:
Robot frame is shaped like the capital letter H.
It consists of:
Two vertical posts with linear rails
A horizontal bridge (gantry) that moves vertically (Y-axis) between the vertical post
An actuator carriage that moves horizontally (X-axis) along the bridge

Belt and Pulley Configuration:
There are two motors at the bottom of the left and right vertical posts (fixed).
Each vertical post (bottom) has 2 pulleys (top and bottom).
The bridge also has 2 pulleys (one at each end).
A single continuous belt is threaded through these pulleys:
From motor → up along post → pulley → across bridge end → actuator → opposite bridge end → down post → motor
The ends of the belt are attached to the actuator, forming a loop.
Joints and Motion:
Prismatic joint 1: allows the bridge to move up/down (Y-axis).
Prismatic joint 2: allows the actuator to move left/right (X-axis) along the bridge.
The actuator position is driven by motor rotation and belt tension 



.



RUN INSTRUCTIONS 

ROS NOETIC 
URDF FILE WAS CODED 

ROS NOETIC WAS SOURCED
mkdir -p ~/catkin_ws/src/my_robot_description/launch
gedit ~/catkin_ws/src/my_robot_description/launch/view_robot.launch

Launch file 
<launch>
  <!-- Load the URDF from file and set robot_description parameter -->
  <param name="robot_description" command="cat $(find my_robot_description)/urdf/my_robot.urdf" />

  <!-- GUI to simulate joint movement (optional if you have movable joints) -->
  <node name="joint_state_publisher" pkg="joint_state_publisher_gui" type="joint_state_publisher_gui" />

  <!-- Publishes transforms between links based on joint states -->
  <node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher" />

  <!-- Launch RViz for visualization -->
  <node name="rviz" pkg="rviz" type="rviz" args="-d $(find my_robot_description)/rviz/view_robot.rviz"/>
</launch>

Source the workspace 
cd ~/catkin_ws
catkin_make
source devel/setup.bash


~/catkin_ws/src/my_robot_description/urdf/my_robot.urdf
gedit ~/catkin_ws/src/my_robot_description/urdf/my_robot.urdf

<?xml version="1.0" ?>
<robot name="hbot_gantry">
    <!-- Materials -->
    <material name="silver">
        <color rgba="0.8 0.8 0.8 1" />
    </material>
    <material name="blue">
        <color rgba="0.3 0.4 0.8 1" />
    </material>
    <material name="red">
        <color rgba="0.8 0.2 0.2 1" />
    </material>
    <material name="black">
        <color rgba="0.1 0.1 0.1 1" />
    </material>
    <material name="green">
        <color rgba="0.2 0.6 0.3 1" />
    </material>
    <!-- Base -->
    <link name="base_link">
        <visual>
            <geometry>
                <box size="1.4 0.1 0.2" />
            </geometry>
            <origin xyz="0.6 0 0.1" rpy="0 0 0" />
            <material name="silver" />
        </visual>
        <collision>
            <geometry>
                <box size="1.4 0.1 0.2" />
            </geometry>
            <origin xyz="0.6 0 0.1" />
        </collision>
        <inertial>
            <mass value="10" />
            <origin xyz="0.6 0 0.1" rpy="0 0 0" />
            <inertia ixx="0.5" ixy="0" ixz="0" iyy="0.5" iyz="0" izz="0.5" />
        </inertial>
    </link>
    <!-- Vertical Posts -->
    <link name="left_post">
        <visual>
            <geometry>
                <box size="0.1 1.0 0.1" />
            </geometry>
            <origin xyz="0 0.5 0.15" />
            <material name="blue" />
        </visual>
        <collision>
            <geometry>
                <box size="0.1 1.0 0.1" />
            </geometry>
            <origin xyz="0 0.5 0.15" />
        </collision>
        <inertial>
            <mass value="3" />
            <origin xyz="0 0.5 0.15" rpy="0 0 0" />
            <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.01" iyz="0" izz="0.1" />
        </inertial>
    </link>
    <link name="right_post">
        <visual>
            <geometry>
                <box size="0.1 1.0 0.1" />
            </geometry>
            <origin xyz="0 0.5 0.15" />
            <material name="blue" />
        </visual>
        <collision>
            <geometry>
                <box size="0.1 1.0 0.1" />
            </geometry>
            <origin xyz="0 0.5 0.15" />
        </collision>
        <inertial>
            <mass value="3" />
            <origin xyz="0 0.5 0.15" rpy="0 0 0" />
            <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.01" iyz="0" izz="0.1" />
        </inertial>
    </link>
    <!-- Post Joints -->
    <joint name="base_to_left_post" type="fixed">
        <parent link="base_link" />
        <child link="left_post" />
        <origin xyz="0.1 0 0.15" rpy="0 0 0" />
    </joint>
    <joint name="base_to_right_post" type="fixed">
        <parent link="base_link" />
        <child link="right_post" />
        <origin xyz="1.1 0 0.15" rpy="0 0 0" />
    </joint>
    <!-- Motors with Correct Shaft Orientation -->
    <link name="left_motor">
        <visual>
            <geometry>
                <cylinder radius="0.06" length="0.12" />
            </geometry>
            <!-- Shaft along Y-axis for belt driving -->
            <origin xyz="0 0.06 0" rpy="1.5708 0 0" />
            <material name="green" />
        </visual>
        <collision>
            <geometry>
                <cylinder radius="0.06" length="0.12" />
            </geometry>
            <origin xyz="0 0.06 0" rpy="1.5708 0 0" />
        </collision>
        <inertial>
            <mass value="0.8" />
            <origin xyz="0 0.06 0" rpy="0 0 0" />
            <inertia ixx="0.0015" ixy="0" ixz="0" iyy="0.0015" iyz="0" izz="0.0015" />
        </inertial>
    </link>
    <link name="right_motor">
        <visual>
            <geometry>
                <cylinder radius="0.06" length="0.12" />
            </geometry>
            <origin xyz="0 0.06 0" rpy="1.5708 0 0" />
            <material name="green" />
        </visual>
        <collision>
            <geometry>
                <cylinder radius="0.06" length="0.12" />
            </geometry>
            <origin xyz="0 0.06 0" rpy="1.5708 0 0" />
        </collision>
        <inertial>
            <mass value="0.8" />
            <origin xyz="0 0.06 0" rpy="0 0 0" />
            <inertia ixx="0.0015" ixy="0" ixz="0" iyy="0.0015" iyz="0" izz="0.0015" />
        </inertial>
    </link>
    <joint name="base_to_left_motor" type="fixed">
        <parent link="base_link" />
        <child link="left_motor" />
        <!-- Positioned at base of left post -->
        <origin xyz="0.1 0 0.06" rpy="0 0 0" />
    </joint>
    <joint name="base_to_right_motor" type="fixed">
        <parent link="base_link" />
        <child link="right_motor" />
        <!-- Positioned at base of right post -->
        <origin xyz="1.1 0 0.06" rpy="0 0 0" />
    </joint>
    <!-- Bottom Pulleys (attached to motor shafts) -->
    <link name="left_bottom_pulley">
        <visual>
            <geometry>
                <cylinder radius="0.05" length="0.05" />
            </geometry>
            <!-- Oriented for horizontal belt routing -->
            <origin xyz="0 0 0" rpy="0 1.5708 0" />
            <material name="black" />
        </visual>
        <collision>
            <geometry>
                <cylinder radius="0.05" length="0.05" />
            </geometry>
            <origin xyz="0 0 0" rpy="0 1.5708 0" />
        </collision>
        <inertial>
            <mass value="0.1" />
            <origin xyz="0 0 0" rpy="0 0 0" />
            <inertia ixx="0.03" iyy="0.03" izz="0.03" ixy="0.0" ixz="0.0" iyz="0.0" />
        </inertial>
    </link>
    <link name="right_bottom_pulley">
        <visual>
            <geometry>
                <cylinder radius="0.05" length="0.05" />
            </geometry>
            <origin xyz="0 0 0" rpy="0 1.5708 0" />
            <material name="black" />
        </visual>
        <collision>
            <geometry>
                <cylinder radius="0.05" length="0.05" />
            </geometry>
            <origin xyz="0 0 0" rpy="0 1.5708 0" />
        </collision>
        <inertial>
            <mass value="0.1" />
            <origin xyz="0 0 0" rpy="0 0 0" />
            <inertia ixx="0.03" iyy="0.03" izz="0.03" ixy="0.0" ixz="0.0" iyz="0.0" />
        </inertial>
    </link>
    <!-- Continuous joints for pulley rotation -->
    <joint name="left_motor_to_pulley" type="continuous">
        <parent link="left_motor" />
        <child link="left_bottom_pulley" />
        <origin xyz="0 0.06 0" rpy="0 0 0" />
        <axis xyz="0 1 0" />
        <!-- Rotation around Y-axis -->
    </joint>
    <joint name="right_motor_to_pulley" type="continuous">
        <parent link="right_motor" />
        <child link="right_bottom_pulley" />
        <origin xyz="0 0.06 0" rpy="0 0 0" />
        <axis xyz="0 1 0" />
    </joint>
    <!-- Top Pulleys (Fixed at post tops) -->
    <link name="left_top_pulley">
        <visual>
            <geometry>
                <cylinder radius="0.05" length="0.05" />
            </geometry>
            <origin xyz="0 0 0" rpy="0 1.5708 0" />
            <material name="black" />
        </visual>
        <collision>
            <geometry>
                <cylinder radius="0.05" length="0.05" />
            </geometry>
            <origin xyz="0 0 0" rpy="0 1.5708 0" />
        </collision>
        <inertial>
            <mass value="0.1" />
            <origin xyz="0 0 0" rpy="0 0 0" />
            <inertia ixx="0.03" iyy="0.03" izz="0.03" ixy="0.0" ixz="0.0" iyz="0.0" />
        </inertial>
    </link>
    <link name="right_top_pulley">
        <visual>
            <geometry>
                <cylinder radius="0.05" length="0.05" />
            </geometry>
            <origin xyz="0 0 0" rpy="0 1.5708 0" />
            <material name="black" />
        </visual>
        <collision>
            <geometry>
                <cylinder radius="0.05" length="0.05" />
            </geometry>
            <origin xyz="0 0 0" rpy="0 1.5708 0" />
        </collision>
        <inertial>
            <mass value="0.1" />
            <origin xyz="0 0 0" rpy="0 0 0" />
            <inertia ixx="0.03" iyy="0.03" izz="0.03" ixy="0.0" ixz="0.0" iyz="0.0" />
        </inertial>
    </link>
    <joint name="left_post_to_top_pulley" type="fixed">
        <parent link="left_post" />
        <child link="left_top_pulley" />
        <!-- Precise position at top of post -->
        <origin xyz="0 1.0 0.15" rpy="0 0 0" />
    </joint>
    <joint name="right_post_to_top_pulley" type="fixed">
        <parent link="right_post" />
        <child link="right_top_pulley" />
        <origin xyz="0 1.0 0.15" rpy="0 0 0" />
    </joint>
    <!-- Bridge with Belt Alignment -->
    <link name="bridge">
        <visual>
            <geometry>
                <box size="1.2 0.1 0.1" />
            </geometry>
            <origin xyz="0.6 0 0" />
            <material name="blue" />
        </visual>
        <collision>
            <geometry>
                <box size="1.2 0.1 0.1" />
            </geometry>
            <origin xyz="0.6 0 0" />
        </collision>
        <inertial>
            <mass value="2.5" />
            <origin xyz="0.6 0 0" rpy="0 0 0" />
            <inertia ixx="0.2" ixy="0" ixz="0" iyy="0.02" iyz="0" izz="0.2" />
        </inertial>
    </link>
    <!-- Bridge Joint (Y-axis movement) -->
    <joint name="bridge_joint" type="prismatic">
        <parent link="base_link" />
        <child link="bridge" />
        <origin xyz="0.6 0 0.35" rpy="0 0 0" />
        <axis xyz="0 1 0" />
        <!-- Vertical movement -->
        <limit lower="0.0" upper="1.0" effort="100" velocity="1.0" />
    </joint>
    <!-- Bridge Pulleys (for belt redirection) -->
    <link name="bridge_left_pulley">
        <visual>
            <geometry>
                <cylinder radius="0.05" length="0.05" />
            </geometry>
            <origin xyz="0 0 0" rpy="0 1.5708 0" />
            <material name="black" />
        </visual>
        <collision>
            <geometry>
                <cylinder radius="0.05" length="0.05" />
            </geometry>
            <origin xyz="0 0 0" rpy="0 1.5708 0" />
        </collision>
        <inertial>
            <mass value="0.1" />
            <origin xyz="0 0 0" rpy="0 0 0" />
            <inertia ixx="0.03" iyy="0.03" izz="0.03" ixy="0.0" ixz="0.0" iyz="0.0" />
        </inertial>
    </link>
    <link name="bridge_right_pulley">
        <visual>
            <geometry>
                <cylinder radius="0.05" length="0.05" />
            </geometry>
            <origin xyz="0 0 0" rpy="0 1.5708 0" />
            <material name="black" />
        </visual>
        <collision>
            <geometry>
                <cylinder radius="0.05" length="0.05" />
            </geometry>
            <origin xyz="0 0 0" rpy="0 1.5708 0" />
        </collision>
        <inertial>
            <mass value="0.1" />
            <origin xyz="0 0 0" rpy="0 0 0" />
            <inertia ixx="0.03" iyy="0.03" izz="0.03" ixy="0.0" ixz="0.0" iyz="0.0" />
        </inertial>
    </link>
    <joint name="bridge_to_left_pulley" type="fixed">
        <parent link="bridge" />
        <child link="bridge_left_pulley" />
        <!-- Left end of bridge -->
        <origin xyz="0.0 0 0.1" rpy="0 0 0" />
    </joint>
    <joint name="bridge_to_right_pulley" type="fixed">
        <parent link="bridge" />
        <child link="bridge_right_pulley" />
        <!-- Right end of bridge -->
        <origin xyz="1.2 0 0.1" rpy="0 0 0" />
    </joint>
    <!-- Carriage with Belt Attachment Points -->
    <link name="carriage">
        <visual>
            <geometry>
                <box size="0.2 0.15 0.1" />
            </geometry>
            <origin xyz="0.1 0 0.05" />
            <material name="red" />
        </visual>
        <collision>
            <geometry>
                <box size="0.2 0.15 0.1" />
            </geometry>
            <origin xyz="0 0 0.05" />
        </collision>
        <inertial>
            <mass value="0.7" />
            <origin xyz="0 0 0.05" rpy="0 0 0" />
            <inertia ixx="0.003" ixy="0" ixz="0" iyy="0.003" iyz="0" izz="0.003" />
        </inertial>
    </link>
    <!-- Carriage Joint (X-axis movement) -->
    <joint name="carriage_joint" type="prismatic">
        <parent link="bridge" />
        <child link="carriage" />
        <origin xyz="0.6 0 0.05" rpy="0 0 0" />
        <axis xyz="1 0 0" />
        <!-- Horizontal movement -->
        <limit lower="0.0" upper="1.2" effort="60" velocity="1.0" />
    </joint>
    <!-- Belt Attachment Points (visual only) -->
    <link name="left_belt_anchor">
        <visual>
            <geometry>
                <sphere radius="0.01" />
            </geometry>
            <origin xyz="-0.1 0 0.1" />
            <material name="black" />
        </visual>
    </link>
    <link name="right_belt_anchor">
        <visual>
            <geometry>
                <sphere radius="0.01" />
            </geometry>
            <origin xyz="0.1 0 0.1" />
            <material name="black" />
        </visual>
    </link>
    <joint name="carriage_to_left_anchor" type="fixed">
        <parent link="carriage" />
        <child link="left_belt_anchor" />
        <origin xyz="0 0 0" rpy="0 0 0" />
    </joint>
    <joint name="carriage_to_right_anchor" type="fixed">
        <parent link="carriage" />
        <child link="right_belt_anchor" />
        <origin xyz="0 0 0" rpy="0 0 0" />
    </joint>
    <!-- End Effector for MoveIt -->
    <link name="ee_link">
        <visual>
            <geometry>
                <sphere radius="0.015" />
            </geometry>
            <origin xyz="0 0 0.1" />
            <material name="red" />
        </visual>
    </link>
    <joint name="carriage_to_ee" type="fixed">
        <parent link="carriage" />
        <child link="ee_link" />
        <origin xyz="0 0 0.1" rpy="0 0 0" />
    </joint>
    <transmission name="trans_left_motor_to_pulley">
        <type>transmission_interface/SimpleTransmission</type>
        <joint name="left_motor_to_pulley">
            <hardwareInterface>hardware_interface/EffortJointInterface</hardwareInterface>
        </joint>
        <actuator name="left_motor_to_pulley_motor">
            <hardwareInterface>hardware_interface/EffortJointInterface</hardwareInterface>
            <mechanicalReduction>1</mechanicalReduction>
        </actuator>
    </transmission>
    <transmission name="trans_right_motor_to_pulley">
        <type>transmission_interface/SimpleTransmission</type>
        <joint name="right_motor_to_pulley">
            <hardwareInterface>hardware_interface/EffortJointInterface</hardwareInterface>
        </joint>
        <actuator name="right_motor_to_pulley_motor">
            <hardwareInterface>hardware_interface/EffortJointInterface</hardwareInterface>
            <mechanicalReduction>1</mechanicalReduction>
        </actuator>
    </transmission>
    <transmission name="trans_bridge_joint">
        <type>transmission_interface/SimpleTransmission</type>
        <joint name="bridge_joint">
            <hardwareInterface>hardware_interface/EffortJointInterface</hardwareInterface>
        </joint>
        <actuator name="bridge_joint_motor">
            <hardwareInterface>hardware_interface/EffortJointInterface</hardwareInterface>
            <mechanicalReduction>1</mechanicalReduction>
        </actuator>
    </transmission>
    <transmission name="trans_carriage_joint">
        <type>transmission_interface/SimpleTransmission</type>
        <joint name="carriage_joint">
            <hardwareInterface>hardware_interface/EffortJointInterface</hardwareInterface>
        </joint>
        <actuator name="carriage_joint_motor">
            <hardwareInterface>hardware_interface/EffortJointInterface</hardwareInterface>
            <mechanicalReduction>1</mechanicalReduction>
        </actuator>
    </transmission>
    <gazebo>
        <plugin name="gazebo_ros_control" filename="libgazebo_ros_control.so">
            <robotNamespace>/</robotNamespace>
        </plugin>
    </gazebo>
</robot>
cd ~/catkin_ws
catkin_make
source devel/setup.bash
roslaunch my_robot_description view_robot.launch
set the frame to base_link 
add robel model and tf from option given at the left bottom 

then, a rviz simulation is visible 
