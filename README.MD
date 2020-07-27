# Passos
## 1 - Instalar o ros-kinetic: http://wiki.ros.org/kinetic/Installation/Ubuntu
## 2 - Instalar MoveIt 
```
sudo apt install ros-kinetic-moveit
```
## 3 - Clonar o repositório do github
```
https://github.com/joselitolima21/motion-planning-plot
```
## 4 - Dar make no workspace
```
cd ./motion-planning-plot/ws
catkin_make
```
## 5 - Dar source no workspace
```
source ./devel/setup.bash
```
## 6 - Instalar o joint-state-publisher
```
sudo apt install joint-state-publisher
```
## 7 - Instalar as dependencias que faltam
```
cd ./src
sudo rosdep init
rosdep update
rosdep install -y --from-paths . --ignore-src --rosdistro kinetic
```