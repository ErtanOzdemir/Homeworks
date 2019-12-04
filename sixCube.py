from turtle import *
num1=0
num2=0
for i in range(50):
  forward(10)
  right(120)
  forward(10)
  left(60)
  forward(10)
  right(120)
  forward(10)
  right(60)

  num1=num1+1
  num2=num2+1

  if num1%2==0:
    left(180)
  else:
    continue
  if num2%4==0:
    right(180)
  else:
    continue