# Passos
## 1 - Instalar o ros-kinetic: http://wiki.ros.org/kinetic/Installation/Ubuntu
## 2 - Instalar MoveIt 

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
echo "source ./devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
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
# Transformar para python
```
pyuic4 ./programa/untitled.ui -o ./programa/index.py
```
```
import sys
import subprocess

self.pushButton_4.clicked.connect(self.executeLaunch)
self.pushButton_5.clicked.connect(self.killLaunch)
def executeLaunch(self):
        self.thread = My_Thread(self.label)
        self.thread.start()
    
    def killLaunch(self):
        subprocess.call('kill -INT `cat /tmp/demo.pid`',shell =True)
        self.label.setText('O RViz foi finalizado com sucesso!')


class My_Thread(QtCore.QThread):

    def __init__(self,label):
        self.label = label
        super(My_Thread,self).__init__(label)

    def run(self):
        self.label.setText('O RViz foi inicializado com sucesso! \nAguarde alguns segundos para aparecer')
        return_code = subprocess.call('roslaunch --pid=/tmp/demo.pid panda_moveit_config demo.launch',shell=True)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window =  QtGui.QMainWindow()
    classe = Ui_MainWindow()
    classe.setupUi(window)
    window.show()
    sys.exit(app.exec_())
```
```
roslaunch panda_moveit_config demo.launch
```
https://www.learnpyqt.com/courses/concurrent-execution/multithreading-pyqt-applications-qthreadpool/

# Concertar
1 - impedir de abrir vários