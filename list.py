List = []
 
word = 'Programming'

   p   r   o   g   r   a   m   m   i   n  g
   0   1   2   3   4   5   6   7   8   9  10
 -11  -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
 word [0]
 word [-2]
 word [3:5]
 word [:2] + word [3:]

 len(word)
 #Len = Length 
 square = 'square'
 len(square)
 len(word) + len(square)

  cube = [10 ,20, 30, 45, 50]
>>> cube
[10, 20, 30, 45, 50]
 cube.reverse()
>>> cube
[75, 60, 50, 45, 24, 20, 10]
>>> cube.sort ()
>>> cube
[10, 20, 24, 45, 50, 60, 75]
>>> cube.remove (24)
>>> cube
[10, 20, 45, 50, 60, 75]
>>> cube.pop()
75
>>> cube.pop()
60

cube1 = [10, 20, 30, 45, 50]
cube2 = [1, 2, 3, 4, 5]
cube1.extend(cube2)

del cube1[3]
del cube1[1:3]
del cube1[:]

programA = ['A', 'B', 'C', 'D', 'E']
programB = ['a', 'b', 'c', 'd', 'e']
programC = programA + programB
programC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
programD = [1, 2, 3, 4, 5]
programC = programC + programD
programC[9:] = []
programC[5:9] = programD
programC
len(programC)

a = [10,20,30,40,50]
b = [60,70,80,90,100]
c = [110,120,130,140,150]
x = [a,b,c]
x

 x[0][2]
 x[][3]
 x[1][2]
 x[1:2][1:2]
 x[][]
