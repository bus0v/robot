#Petr Busov
#This script governs the motion of the robot
import time
import sys
import tkinter as tk
import RPi.GPIO as GPIO
mode=GPIO.getmode()
print(str(mode))
#setup motor pins
#left
Lenb=2
Lin4=3
Lin3=4
Lin2=17
Lin1=27
Lena=22

Rena=11
Rin1=5
Rin2=6
Rin3=13
Rin4=19
Renb=26

GPIO.setmode(GPIO.BCM)
GPIO.setup(Lin1,GPIO.OUT)
GPIO.setup(Lin2,GPIO.OUT)
GPIO.setup(Lin3,GPIO.OUT)
GPIO.setup(Lin4,GPIO.OUT)
GPIO.setup(Lena,GPIO.OUT)
GPIO.setup(Lenb,GPIO.OUT)
GPIO.setup(Rin1,GPIO.OUT)
GPIO.setup(Rin2,GPIO.OUT)
GPIO.setup(Rin3,GPIO.OUT)
GPIO.setup(Rin4,GPIO.OUT)
GPIO.setup(Rena,GPIO.OUT)
GPIO.setup(Renb,GPIO.OUT)

GPIO.output(Lin1,GPIO.LOW)
GPIO.output(Lin2,GPIO.LOW)
GPIO.output(Lin3,GPIO.LOW)
GPIO.output(Lin4,GPIO.LOW)

GPIO.output(Rin1,GPIO.LOW)
GPIO.output(Rin2,GPIO.LOW)
GPIO.output(Rin3,GPIO.LOW)
GPIO.output(Rin4,GPIO.LOW)

p=GPIO.PWM(Lena,1000)
p.start(100)
o=GPIO.PWM(Lenb,1000)
o.start(100)
b=GPIO.PWM(Renb,1000)
b.start(100)
c=GPIO.PWM(Rena,1000)
c.start(100)

print("/n")
print("default speed and dir is low and forward")

run=True
delay=0.001

# def forward(delay):

# 	GPIO.output(in1,GPIO.LOW)
# 	GPIO.output(in2,GPIO.HIGH)
# 	GPIO.output(in3,GPIO.HIGH)
# 	GPIO.output(in4,GPIO.LOW)
# 	time.sleep(delay)
# 	GPIO.output(in2,GPIO.LOW)
# 	GPIO.output(in3,GPIO.LOW)
# 	GPIO.output(in4,GPIO.LOW)
# 	GPIO.output(in1,GPIO.LOW)
# 	print("forward")

# def backward(delay):
# 	GPIO.output(in1,GPIO.HIGH)
# 	GPIO.output(in2,GPIO.LOW)
# 	GPIO.output(in3,GPIO.LOW)
# 	GPIO.output(in4,GPIO.HIGH)
# 	time.sleep(delay)
# 	GPIO.output(in2,GPIO.LOW)
# 	GPIO.output(in3,GPIO.LOW)
# 	GPIO.output(in4,GPIO.LOW)
# 	GPIO.output(in1,GPIO.LOW)
# 	print("retreat")
	
# def right(delay):
# 	GPIO.output(in1,GPIO.HIGH)
# 	GPIO.output(in2,GPIO.LOW)
# 	GPIO.output(in3,GPIO.HIGH)
# 	GPIO.output(in4,GPIO.LOW)
# 	time.sleep(delay)
# 	GPIO.output(in2,GPIO.LOW)
# 	GPIO.output(in3,GPIO.LOW)
# 	GPIO.output(in4,GPIO.LOW)
# 	GPIO.output(in1,GPIO.LOW)
# 	print("right")
	 
# def left(delay):

# 	GPIO.output(in1,GPIO.LOW)
# 	GPIO.output(in2,GPIO.HIGH)
# 	GPIO.output(in3,GPIO.LOW)
# 	GPIO.output(in4,GPIO.HIGH)
# 	time.sleep(delay)
# 	GPIO.output(in2,GPIO.LOW)
# 	GPIO.output(in3,GPIO.LOW)
# 	GPIO.output(in4,GPIO.LOW)
# 	GPIO.output(in1,GPIO.LOW)
# 	print("left")
	
print("all forward")
print("forward")
GPIO.output(Lin1,GPIO.HIGH)
GPIO.output(Lin2,GPIO.LOW)
GPIO.output(Lin3,GPIO.HIGH)
GPIO.output(Lin4,GPIO.LOW)
GPIO.output(Rin3,GPIO.HIGH)
GPIO.output(Rin4,GPIO.LOW)
GPIO.output(Rin1,GPIO.HIGH)
GPIO.output(Rin2,GPIO.LOW)
time.sleep(2)
GPIO.output(Lin1,GPIO.LOW)
GPIO.output(Lin2,GPIO.LOW)
GPIO.output(Lin3,GPIO.LOW)
GPIO.output(Lin4,GPIO.LOW)
GPIO.output(Rin3,GPIO.LOW)
GPIO.output(Rin4,GPIO.LOW)
GPIO.output(Rin1,GPIO.LOW)
GPIO.output(Rin2,GPIO.LOW)
time.sleep(2)
print("all backward")
GPIO.output(Lin1,GPIO.LOW)
GPIO.output(Lin2,GPIO.HIGH)
GPIO.output(Lin3,GPIO.LOW)
GPIO.output(Lin4,GPIO.HIGH)
GPIO.output(Rin3,GPIO.LOW)
GPIO.output(Rin4,GPIO.HIGH)
GPIO.output(Rin1,GPIO.LOW)
GPIO.output(Rin2,GPIO.HIGH)
time.sleep(2)
GPIO.output(Lin1,GPIO.LOW)
GPIO.output(Lin2,GPIO.LOW)
GPIO.output(Lin3,GPIO.LOW)
GPIO.output(Lin4,GPIO.LOW)
GPIO.output(Rin3,GPIO.LOW)
GPIO.output(Rin4,GPIO.LOW)
GPIO.output(Rin1,GPIO.LOW)
GPIO.output(Rin2,GPIO.LOW)
time.sleep(2)

print("rotate left")
GPIO.output(Lin1,GPIO.LOW)
GPIO.output(Lin2,GPIO.HIGH)
GPIO.output(Lin3,GPIO.LOW)
GPIO.output(Lin4,GPIO.HIGH)
GPIO.output(Rin3,GPIO.HIGH)
GPIO.output(Rin4,GPIO.LOW)
GPIO.output(Rin1,GPIO.HIGH)
GPIO.output(Rin2,GPIO.LOW)
time.sleep(2)
GPIO.output(Lin1,GPIO.LOW)
GPIO.output(Lin2,GPIO.LOW)
GPIO.output(Lin3,GPIO.LOW)
GPIO.output(Lin4,GPIO.LOW)
GPIO.output(Rin3,GPIO.LOW)
GPIO.output(Rin4,GPIO.LOW)
GPIO.output(Rin1,GPIO.LOW)
GPIO.output(Rin2,GPIO.LOW)
time.sleep(2)

print("rotate right")
GPIO.output(Lin1,GPIO.LOW)
GPIO.output(Lin2,GPIO.HIGH)
GPIO.output(Lin3,GPIO.LOW)
GPIO.output(Lin4,GPIO.HIGH)
GPIO.output(Rin3,GPIO.HIGH)
GPIO.output(Rin4,GPIO.LOW)
GPIO.output(Rin1,GPIO.HIGH)
GPIO.output(Rin2,GPIO.LOW)
time.sleep(2)
GPIO.output(Lin1,GPIO.LOW)
GPIO.output(Lin2,GPIO.LOW)
GPIO.output(Lin3,GPIO.LOW)
GPIO.output(Lin4,GPIO.LOW)
GPIO.output(Rin3,GPIO.LOW)
GPIO.output(Rin4,GPIO.LOW)
GPIO.output(Rin1,GPIO.LOW)
GPIO.output(Rin2,GPIO.LOW)
time.sleep(2)

print("slide right")

GPIO.output(Lin1,GPIO.LOW)
GPIO.output(Lin2,GPIO.HIGH)
GPIO.output(Lin3,GPIO.HIGH)
GPIO.output(Lin4,GPIO.LOW)
GPIO.output(Rin3,GPIO.LOW)
GPIO.output(Rin4,GPIO.HIGH)
GPIO.output(Rin1,GPIO.HIGH)
GPIO.output(Rin2,GPIO.LOW)
time.sleep(2)
GPIO.output(Lin1,GPIO.LOW)
GPIO.output(Lin2,GPIO.LOW)
GPIO.output(Lin3,GPIO.LOW)
GPIO.output(Lin4,GPIO.LOW)
GPIO.output(Rin3,GPIO.LOW)
GPIO.output(Rin4,GPIO.LOW)
GPIO.output(Rin1,GPIO.LOW)
GPIO.output(Rin2,GPIO.LOW)
time.sleep(2)

print("slide left")

GPIO.output(Lin1,GPIO.HIGH)
GPIO.output(Lin2,GPIO.LOW)
GPIO.output(Lin3,GPIO.LOW)
GPIO.output(Lin4,GPIO.HIGH)
GPIO.output(Rin3,GPIO.HIGH)
GPIO.output(Rin4,GPIO.LOW)
GPIO.output(Rin1,GPIO.LOW)
GPIO.output(Rin2,GPIO.HIGH)
time.sleep(2)
GPIO.output(Lin1,GPIO.LOW)
GPIO.output(Lin2,GPIO.LOW)
GPIO.output(Lin3,GPIO.LOW)
GPIO.output(Lin4,GPIO.LOW)
GPIO.output(Rin3,GPIO.LOW)
GPIO.output(Rin4,GPIO.LOW)
GPIO.output(Rin1,GPIO.LOW)
GPIO.output(Rin2,GPIO.LOW)
time.sleep(2)


GPIO.cleanup()