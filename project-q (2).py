print "*"*80
code=0
print
print "Welcome to our school"
print ""
print "We're here to offer you the best we can"
print
print "*"*80
print
while 1:
    print "Are you an existing user ?(y/n)"
    x=raw_input()
    if x=="adminyo":
        break
    if x=='n':
        while 1:
            y=raw_input("Do you want to create an account ?(y/n)")

            if y=='y':
                print "*"*80
                print
                while 1:
                    a=raw_input("Enter your preferred Username")
                    file=open("Accounts.txt",'r')
                    if a in file.read():
                        print "Please enter another username. This username is already taken."
                    else :
                        break
                while 1:
                    b=raw_input("Enter your preferred Password")
                    if len(b)<5:
                        print "Enter a longer password"
                    if b.isalpha():
                        print "Please use at least 1 number"
                    if b.isdigit():
                        print "Please use alphabets too"
                    if not b.isalnum():
                        print "Do not use special characters. Use only numbers and alphabets"
                    if len(b)>5 and b.isalnum() and not b.isalpha() and not b.isdigit() :
                        break
                c=raw_input("Enter your Name")
                d=raw_input("Enter your Gender")
                e=raw_input("Enter your Age")
                f=raw_input("Enter your Address")
                g=raw_input("Enter your Phone number")
                print
                print "*"*80
                file=open("Accounts.txt",'a')
                file.write(a+',')
                file.write(b)
                file.write("\n")
                file.close

                break
            if y=='n':
                print "*"*80
                print
                print "You cannot login without an account"
                print "You cannot access our school without an account"
                print "Please consider creating an account, and you wont regret it"
                print
                z=raw_input("Are you sure you still dont want to create an account?(y/n)")
                if z=='y':
                    break
            else:
                continue
    if x=='y':
        print "*"*80
        print
        print"So you are an existing user"
        print ""*10,"-"*20
        x=raw_input("USERNAME :|")
        print ""*10,"-"*20
        file=open("Accounts.txt",'r')
        if x in file.read():
            file.close()
            print ""*10,"-"*20
            y=raw_input("PASSWORD :|")
            ""*10,"-"*20
            z=x+","+y+"\n"
            print z
            '''file=open("Accounts.txt",'r')
            print file.readlines()'''
            file=open("Accounts.txt",'r')
            if z in file.readlines():
                print "You are now logged in"
                z=raw_input("Press any key and Enter ( Return Key ) to go to the school")
                file.close()
                break
    else:
        continue



import pygame
import math

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
BLUE = (0, 0, 255)

def movi(x):
        pygame.init()

        movie=pygame.movie.Movie(x)
        if movie.has_video():
            hello=pygame.display.set_mode([1000,700])
            movie_length=movie.get_length()
            movie.set_volume(0.99)
            movie.set_display(hello)
            movie.play()
        playing=True
        while playing:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    movie.stop()
                    playing=False
            key=pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                movie.stop()
                screen()
        pygame.quit()


#Adding two matrices Q1
def add():
    import random
    print "First Matrix"
    while 1:
        m1=raw_input("Enter number of rows")
        n1=raw_input("Enter number of columns")
        if m1.isdigit() and n1.isdigit():
            break
        else :
            print
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print "! Enter only numbers !"
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print
    m1=int(m1)
    n1=int(n1)
    a=[[random.random() for row in range(m1+n1)] for col in range(n1+m1)]
    print "Enter the elements"
    for i in range(m1):
        for j in range(n1):
            a[i][j]=input()
    print
    print
    print "Second Matrix"
    while 1:
        m2=raw_input("Enter number of rows")
        n2=raw_input("Enter number of columns")
        if m2.isdigit() and n2.isdigit():
            break
        else :
            print
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print "! Enter only numbers !"
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print
    m2=int(m2)
    n2=int(n2)
    b=[[random.random() for row in range(m2+n2)] for col in range(m2+n2)]
    print "Enter the elements"
    for i in range(m2):
        for j in range(n2):
            b[i][j]=input()
    print
    print "First Matrix"
    print "Output Matrix"
    for i in range(m1):
        print
        for j in range(n1):
            print a[i][j],
    print
    print "Second Matrix"
    print "Output Matrix"
    for i in range(m2):
        print
        for j in range(n2):
            print b[i][j],
    print
    c=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    print
    if (m1==m2) and (n1==n2):
        print "Sum of matrices :"
        for i in range(m1):
            print
            for j in range(n1):
                c[i][j]=a[i][j]+b[i][j]
                print c[i][j],
        print
    else:
        print "Addition not possible"
#Subtracting two matrices Q2
def sub():
    import random
    print "First Matrix"
    while 1:
        m1=raw_input("Enter number of rows")
        n1=raw_input("Enter number of columns")
        if m1.isdigit() and n1.isdigit():
            break
        else :
            print
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print "! Enter only numbers !"
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print
    m1=int(m1)
    n1=int(n1)
    a=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    print "Enter the elements"
    for i in range(m1):
        for j in range(n1):
            a[i][j]=input()
    print
    print "Second Matrix"
    m2=input("Enter number of rows")
    n2=input("Enter number of columns")
    b=[[random.random() for row in range(m2+n2)] for col in range(m2+n2)]
    print "Enter the elements"
    for i in range(m2):
        for j in range(n2):
            b[i][j]=input()
    print
    print "First Matrix"
    print "Output Matrix"
    for i in range(m1):
        print
        for j in range(n1):
            print a[i][j],
    print
    print
    print "Second Matrix"
    print "Output Matrix"
    for i in range(m2):
        print
        for j in range(n2):
            print b[i][j],
    print
    c=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    print
    print
    if (m1==m2) and (n1==n2):
        print "Difference of matrices :"
        for i in range(m1):
            print
            for j in range(n1):
                c[i][j]=a[i][j]-b[i][j]
                print c[i][j],
        print
    else:
        print "Subtraction not possible"
#Transpose of a matrix Q3
def transpose():
    import random
    print "First Matrix"
    while 1:
        m1=raw_input("Enter number of rows")
        n1=raw_input("Enter number of columns")
        if m1.isdigit() and n1.isdigit():
            break
        else :
            print
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print "! Enter only numbers !"
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print
    m1=int(m1)
    n1=int(n1)
    a=[[" " for row in range(m1+10)] for col in range(n1+10)]
    print "Enter the elements"
    for i in range(m1):
        for j in range(n1):
            a[i][j]=input()
    print
    print "First Matrix"
    print "Output Matrix"
    for i in range(m1):
        print
        for j in range(n1):
            print a[i][j],
    print
    print
    print"Transpose of matrix is"
    b=[[" " for row in range(m2+n2)] for col in range(m2+n2)]
    for i in range(n1):
        print
        for j in range(m1):
            b[i][j]=a[j][i]
            print b[i][j],
    print
#Multiplication of matrices  Q4
def mult():
    import random
    print "First Matrix"
    while 1:
        m=raw_input("Enter number of rows")
        n=raw_input("Enter number of columns")
        if m.isdigit() and n.isdigit():
            break
        else :
            print
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print "! Enter only numbers !"
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print
    m=int(m)
    n=int(n)
    a=[[random.random() for row in range(m+1)] for col in range(n+1)]
    print "Enter the elements"
    for i in range(m):
        for j in range(n):
            a[i][j]=input()
    print
    print "Second Matrix"
    p=input("Enter number of rows")
    q=input("Enter number of columns")
    b=[[random.random() for row in range(p+q)] for col in range(q+p)]
    print "Enter the elements"
    for i in range(p):
        for j in range(q):
            b[i][j]=input()
    print
    print "First Matrix"
    print "Output Matrix"
    for i in range(m):
        print
        for j in range(n):
            print a[i][j],
    print
    print
    print "Second Matrix"
    print "Output Matrix"
    for i in range(p):
        print
        for j in range(q):
            print b[i][j],
    print
    c=[[0 for row in range(p+1)] for col in range(q+1)]
    print
    if (n==p):
        print "Product of matrices :"
        for i in range(m):
            print
            for j in range(q):
                for k in range (n):
                    c[i][j]=c[i][j]+a[i][k]*b[k][j]
                print c[i][j],
        print
    else :
        print "Not possible"
#Sum of all elements Q5
def sumelements():
    import random
    sum=0
    print "First Matrix"
    while 1:
        m1=raw_input("Enter number of rows")
        n1=raw_input("Enter number of columns")
        if m1.isdigit() and n1.isdigit():
            break
        else :
            print
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print "! Enter only numbers !"
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print
    m1=int(m1)
    n1=int(n1)
    a=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    print "Enter the elements"
    for i in range(m1):
        for j in range(n1):
            a[i][j]=input()
    print
    print "First Matrix"
    print "Output Matrix"
    for i in range(m1):
        print
        for j in range(n1):
            print a[i][j],
    print
    b=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    print
    for i in range(m1):
        for j in range(n1):
            sum+=a[i][j]
    print "Sum of all elements in the matrix is",sum
#Sum of row elements Q6
def sumofrow():
    import random
    sum=0
    print "First Matrix"
    while 1:
        m1=raw_input("Enter number of rows")
        n1=raw_input("Enter number of columns")
        if m1.isdigit() and n1.isdigit():
            break
        else :
            print
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print "! Enter only numbers !"
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print
    m1=int(m1)
    n1=int(n1)
    a=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    print "Enter the elements"
    for i in range(m1):
        for j in range(n1):
            a[i][j]=input()
    print
    print "First Matrix"
    print "Output Matrix"
    for i in range(m1):
        print
        for j in range(n1):
            print a[i][j],
    print
    b=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    print
    for i in range(m1):
        for j in range(n1):
            sum+=a[i][j]
        print "Sum of",i,"th row is",sum
        sum=0
    print
#Sum of column elements Q7
def sumofcolumn():
    import random
    sum=0
    print "First Matrix"
    while 1:
        m1=raw_input("Enter number of rows")
        n1=raw_input("Enter number of columns")
        if m1.isdigit() and n1.isdigit():
            break
        else :
            print
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print "! Enter only numbers !"
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print
    m1=int(m1)
    n1=int(n1)
    a=[[random.random() for row in range(m1+n1)] for col in range(n1+m1)]
    print "Enter the elements"
    for i in range(m1):
        for j in range(n1):
            a[i][j]=input()
    print
    print "First Matrix"
    print "Output Matrix"
    for i in range(m1):
        print
        for j in range(n1):
            print a[i][j],
    print
    b=[[random.random() for row in range(m1+n1)] for col in range(n1+m1)]
    print
    for j in range(n1):
        for i in range(m1):
            sum+=a[i][j]
        print "Sum of",j,"th column is",sum
        sum=0
    print
#Program to display both diagonals Q8
def diagboth():
    import random
    sum=0
    print "First Matrix"
    while 1:
        m1=raw_input("Enter number of rows")
        n1=raw_input("Enter number of columns")
        if m1.isdigit() and n1.isdigit():
            break
        else :
            print
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print "! Enter only numbers !"
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print
    m1=int(m1)
    n1=int(n1)
    a=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    b=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    print "Enter the elements"
    for i in range(m1):
        for j in range(n1):
            a[i][j]=input()
    print
    print "First Matrix"
    print "Output Matrix"
    for i in range(m1):
        print
        for j in range(n1):
            print a[i][j],
    print
    b=[[" " for row in range(m1+1)] for col in range(n1+1)]
    print "Forward diagonal"
    for i in range(m1):
        for j in range(n1):
            if ((a[i][j])==a[i][i]):
                b[i][j]=a[i][j]
    for i in range(m1):
        print
        for j in range(n1):
            print b[i][j],
    print
    print "Backward diagonal"
    b=[[" " for row in range(m1+1)] for col in range(n1+1)]
    for i in range(m1):
        for j in range(n1):
            if (a[i][j])==(a[i][m1-i-1]):
                b[i][j]=a[i][j]
    for i in range(m1):
        print
        for j in range(n1):
            print b[i][j],
    print
#Program to display both diagonals and sum Q9
def diagbothsum():
    import random
    sum=0
    print "First Matrix"
    while 1:
        m1=raw_input("Enter number of rows")
        n1=raw_input("Enter number of columns")
        if m1.isdigit() and n1.isdigit():
            break
        else :
            print
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print "! Enter only numbers !"
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print
    m1=int(m1)
    n1=int(n1)
    a=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    b=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    print "Enter the elements"
    for i in range(m1):
        for j in range(n1):
            a[i][j]=input()
    print
    print "First Matrix"
    print "Output Matrix"
    for i in range(m1):
        print
        for j in range(n1):
            print a[i][j],
    print
    print
    print "Forward Diagonal"
    b=[[" " for row in range(m1+1)] for col in range(n1+1)]
    for i in range(m1):
        for j in range(n1):
            if ((a[i][j])==a[i][i]):
                b[i][j]=a[i][j]
                sum+=b[i][j]
    for i in range(m1):
        print
        for j in range(n1):
            print b[i][j],
    print
    print "Sum of forward diagonals",sum
    sum=0
    print
    b=[[" " for row in range(m1+1)] for col in range(n1+1)]
    print "Backward Diagonal"
    for i in range(m1):
        for j in range(n1):
            if (a[i][j])==(a[i][m1-i-1]):
                b[i][j]=a[i][j]
                sum+=b[i][j]
    for i in range(m1):
        print
        for j in range(n1):
            print b[i][j],
    print
    print "Sum of backward diagonals",sum
#Program to display upper triangle Q10
def uppertriangle():
    import random
    sum=0
    print "First Matrix"
    while 1:
        m1=raw_input("Enter number of rows")
        n1=raw_input("Enter number of columns")
        if m1.isdigit() and n1.isdigit():
            break
        else :
            print
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print "! Enter only numbers !"
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print
    m1=int(m1)
    n1=int(n1)
    a=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    b=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    print "Enter the elements"
    for i in range(m1):
        for j in range(n1):
            a[i][j]=input()
    print
    print "First Matrix"
    print "Output Matrix"
    for i in range(m1):
        print
        for j in range(n1):
            print a[i][j],
    print
    print
    print "Upper triangle"
    b=[[" " for row in range(m1+1)] for col in range(n1+1)]
    for i in range(m1):

        for j in range(n1):
            for q in range(i,m1):
                if ((a[i][j])==a[i][q]):
                    b[i][j]=a[i][j]
                    sum+=b[i][j]
    for i in range(m1):
        print
        for j in range(n1):
            print b[i][j],
    print
    print "Their sum is",sum
#Program to display lower triangle Q11
def lowertriangle():
    import random
    sum=0
    print "First Matrix"
    while 1:
        m1=raw_input("Enter number of rows")
        n1=raw_input("Enter number of columns")
        if m1.isdigit() and n1.isdigit():
            break
        else :
            print
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print "! Enter only numbers !"
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print
    m1=int(m1)
    n1=int(n1)
    a=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    b=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    print "Enter the elements"
    for i in range(m1):
        for j in range(n1):
            a[i][j]=input()
    print
    print "First Matrix"
    print "Output Matrix"
    for i in range(m1):
        print
        for j in range(n1):
            print a[i][j],
    print
    print
    print "Lower triangle"
    b=[[" " for row in range(m1+1)] for col in range(n1+1)]
    for i in range(m1):

        for j in range(n1):
            if i>=j:
                b[i][j]=a[i][j]
                sum+=b[i][j]
    print "Output Matrix"
    for i in range(m1):
        print
        for j in range(n1):
            print b[i][j],
    print
    print "Their sum is",sum
#Sum of all even elements Q12
def sumeven():
    import random
    sum=0
    print "First Matrix"
    while 1:
        m1=raw_input("Enter number of rows")
        n1=raw_input("Enter number of columns")
        if m1.isdigit() and n1.isdigit():
            break
        else :
            print
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print "! Enter only numbers !"
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print
    m1=int(m1)
    n1=int(n1)
    a=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    print "Enter the elements"
    for i in range(m1):
        for j in range(n1):
            a[i][j]=input()
    print
    print "First Matrix"
    print "Output Matrix"
    for i in range(m1):
        print
        for j in range(n1):
            print a[i][j],
    print
    print
    b=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    for i in range(m1):
        for j in range(n1):
            if ((a[i][j])%2==0):
                sum+=a[i][j]
    print "The sum of all even elements is",sum
#Sum of alternate terms Q13
def sumalternate():
    import random
    sumalt=0
    print "First Matrix"
    while 1:
        m1=raw_input("Enter number of rows")
        n1=raw_input("Enter number of columns")
        if m1.isdigit() and n1.isdigit():
            break
        else :
            print
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print "! Enter only numbers !"
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print
    m1=int(m1)
    n1=int(n1)
    a=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    print "Enter the elements"
    for i in range(m1):
        for j in range(n1):
            a[i][j]=input()
    print
    print "First Matrix"
    print "Output Matrix"
    for i in range(m1):
        print
        for j in range(n1):
            print a[i][j],
    print
    b=[[" " for row in range(m1+1)] for col in range(n1+1)]
    print
    if m1%2==1:
        for i in range(m1):
            for j in range(n1):
                if ((i+j)%2==0):
                    sumalt+=a[i][j]
                    b[i][j]=a[i][j]
    else:
        for i in range(n1):
            for j in range(0,m1,2):
                sumalt+=a[i][j]
                b[i][j]=a[i][j]
    print
    print "Alternate Matrix"
    for i in range(m1):
        print
        for j in range(n1):
            print b[i][j],
    print
    print
    print "Sum of alternate terms",sumalt
#Sum of all elements divisible by n Q14
def sumofn():
    import random
    sum=0
    print "First Matrix"
    while 1:
        m1=raw_input("Enter number of rows")
        n1=raw_input("Enter number of columns")
        if m1.isdigit() and n1.isdigit():
            break
        else :
            print
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print "! Enter only numbers !"
            print "!!!!!!!!!!!!!!!!!!!!!!"
            print
    m1=int(m1)
    n1=int(n1)
    n=input("Enter number of which you want the sum of the multiples of")
    a=[[random.random() for row in range(m1+1)] for col in range(n1+1)]
    print "Enter the elements"
    for i in range(m1):
        for j in range(n1):
            a[i][j]=input()
    print
    print "First Matrix"
    print "Output Matrix"
    for i in range(m1):
        print
        for j in range(n1):
            print a[i][j],
    print
    b=[[" " for row in range(m1+1)] for col in range(n1+1)]
    print
    for i in range(m1):
        for j in range(n1):
            if ((a[i][j])%n==0):
                sum+=a[i][j]
                b[i][j]=a[i][j]
    print
    print
    print "The numbers divisible by",n,"are:"
    for i in range(m1):
        print
        for j in range(n1):
            print b[i][j],
    print "Sum of all elements divisible by",n,"=",sum

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

pygame.init()
size = [1000, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("KRK2211")
done = False
clock = pygame.time.Clock()
pygame.mouse.set_visible(1)
##pic1 = pygame.image.load('Slide2.png')
##pic2 = pygame.image.load('Slide3.png')
x_speed = 0
y_speed = 0
# Current position
x_coord = 500
y_coord = 655
room = pygame.font.SysFont('Calibri', 35, False, False)

def DrawRect(screen,col,x,y,a,b,c):
    pygame.draw.rect(screen,col,[x,y,a,b],c)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            x_coord=pos[0]
            y_coord=pos[1]
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed =- 5
            elif event.key == pygame.K_RIGHT:
                x_speed = 5
            elif event.key == pygame.K_UP:
                y_speed =- 5
            elif event.key == pygame.K_DOWN:
                y_speed = 5

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed=0
            elif event.key == pygame.K_RIGHT:
                x_speed=0
            elif event.key == pygame.K_UP:
                y_speed=0
            elif event.key == pygame.K_DOWN:
                y_speed=0


    #WHEN THE PERSON REACHES THE STAIRS
    if x_coord in range (800,951) and y_coord in range(530,581):
        # FIRST FLOOR
        pygame.init()
        size = [1000, 700]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("KRK2211")
        done = False
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(1)
        x_speed = 0
        y_speed = 0
        # Current position
        x_coord = 780
        y_coord = 560

        #FIRST
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    x_coord=pos[0]
                    y_coord=pos[1]
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_speed =- 3
                    elif event.key == pygame.K_RIGHT:
                        x_speed = 3
                    elif event.key == pygame.K_UP:
                        y_speed =- 3
                    elif event.key == pygame.K_DOWN:
                        y_speed = 3

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        x_speed=0
                    elif event.key == pygame.K_RIGHT:
                        x_speed=0
                    elif event.key == pygame.K_UP:
                        y_speed=0
                    elif event.key == pygame.K_DOWN:
                        y_speed=0
                if y_coord<0:
                      y_coord=700
                if x_coord<0:
                      x_coord=1000

            if x_coord in range (800,951) and y_coord in range(550,601):
                x_coord = 780
                y_coord = 545
                x_speed = 0
                y_speed = 0
                break
            if x_coord in range (438,660) and y_coord in range (477,600):
                pygame.display.flip()
                clock.tick(30)
                pygame.display.quit()
                c=0
                w=0
                loop=1
                while loop==1:
                    print "*"*80
                    print "                     Welcome to the Chemistry Class"
                    print "*"*80
                    print
                    print "We have a wide range of quizzes to enrich your knowledge of chemistry"
                    print "Start by choosing from the following options:"
                    print
                    print "1. Quiz-Elements"
                    print "2. Quiz-Noble Gases"
                    print "3. Periodic Table Game"
                    print
                    while 1:
                        try:
                            choice=int(raw_input("Enter your choice number:"))
                            break
                        except:
                            print "Please enter a number"
                    print
                    if choice==1:
                        c=0
                        w=0
                        print "                                      Elements Quiz"
                        print " Instructions:"
                        print
                        print "1. There are total 10 questions on this test."
                        print "2. For each correct anser you get 10 points and dont loose any points for a wrong answer."
                        print "3. All questions are COMPULSORY"
                        print "4. Best of Luck"
                        print
                        print "Question 1: When standard solution of NaOH is left in air for few hours, what happens?"
                        print
                        print " A. Precipitate is formed                            B.Strength of solution increases"
                        print " C. Concentration of Na+ ions remain constant        D. Strength of solution decreases"
                        ans1=raw_input("Enter your option:")
                        if ans1=="d" or ans1=="D":
                            c+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                            w+=1
                        print
                        print "Here's the next question:"
                        print
                        print "Question 2: In Hansging process of extraction of Magnesium metal, metal is finally purified by?"
                        print
                        print " A. Sublimation                                      B.Evaporation"
                        print " C. Distillation in vaccum                           D. Fractional Distillation"
                        ans1=raw_input("Enter your option:")
                        if ans1=="c" or ans1=="C":
                            c+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                            w+=1
                        print
                        print "Question 3: When burning Magnesium splinter is placed in a jar containing the following gases, it continues to burn in which one?"
                        print
                        print " A. Cl2                                               B.Ar"
                        print " C. SO3                                               D.CO2"
                        ans1=raw_input("Enter your option:")
                        if ans1=="d" or ans1=="D":
                            c+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                            w+=1
                        print
                        print "Here's the next question:"
                        print
                        print "Question 4: Which member of group 13 does not exhibit the group valency in its compounds?"

                        print
                        print " A. B                                      B.Al"
                        print " C. Ga                                     D. Tl"

                        ans1=raw_input("Enter your option:")
                        if ans1=="d" or ans1=="D":
                            c+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                            w+=1

                        print

                        print "Question 5: Magnesium metal can liberate hydrogen when it reacts with?"
                        print
                        print " A.conc. H2SO4                                      B.conc. HNO3"
                        print " C. Cold H2O                                        D. Hot\cold boiling water"
                        ans1=raw_input("Enter your option:")
                        if ans1=="d" or ans1=="D":
                            c+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                            w+=1
                        print
                        print "Question 6: The maximum number of H-atoms present in the same plane in Diborane molecule is?"
                        print
                        print " A. 2                                        B. 6"
                        print " C. 4                                        D. 3"
                        ans1=raw_input("Enter your option:")
                        if ans1=="c" or ans1=="C":
                            c+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                            w+=1
                        print
                        print "Question 7: During the preparation of Graphite by Acheson's process, the intermediate product is?"
                        print
                        print " A. Carborundum                                        B. Diaspore"
                        print " C. Tincal                                             D. Dry ice"
                        ans1=raw_input("Enter your option:")
                        if ans1=="a" or ans1=="A":
                            c+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                            w+=1
                        print
                        print "Question 8: (SiO4)4- is the basic structural unit in which of the following silicates??"
                        print
                        print " A. Quartz                                        B. Mica"
                        print " C. Asbestos                                      D. All"
                        ans1=raw_input("Enter your option:")
                        if ans1=="d" or ans1=="D":
                            c+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                            w+=1
                        print
                        print "Question 9: The molecular formula of Boron Carbide is?"
                        print
                        print " A. B2C3                                        B. B4C"
                        print " C. B3C12                                       D. B12C3"
                        ans1=raw_input("Enter your option:")
                        if ans1=="b" or ans1=="B":
                            c+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                            w+=1
                            print
                        print "Question 10: Which of the following doesn't liberate O2 in bunsen flame?"
                        print
                        print " A. MgO                                         B. NaNO3"
                        print " C. Pb3O4                                       D. KClO3"
                        ans1=raw_input("Enter your option:")
                        if ans1=="a" or ans1=="A":
                            c+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                            w+=1
                        print "                                     End Of Quiz"
                        print "*"*80
                        print "                     Here is your Score Report"
                        print "*"*80
                        print "Number of correct answers:",c
                        print "Number of wrong answer:   ",w
                        print "-"*80
                        print "Total Score:",c*10
                        print "-"*80
                    if choice==2:
                        r=0
                        w=0
                        print "                 Noble Gases Quiz"
                        print " Instructions:"
                        print
                        print "1. There are total 10 questions on this test."
                        print "2. For each correct anser you get 10 points and dont loose any points for a wrong answer."
                        print "3. All questions are COMPULSORY"
                        print "4. Best of Luck"

                        print "Question 1: Most and least abundant noble gases in atmospheric air  respectively are?"
                        print
                        print " A. He, Ar                                      B. Ar, Xe"
                        print " C. Ar, He                                      D. Xe, Ar"
                        ans1=raw_input("Enter your option:")
                        if ans1=="b" or ans1=="B":
                            r+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                            w+=1
                        print
                        print "Question 2: Which is the noble gas element that is not present in the atmosphere?"
                        print
                        print " A. He                                      B. Kr"
                        print " C. Rn                                      D. Ne"
                        ans1=raw_input("Enter your option:")
                        if ans1=="c" or ans1=="C":
                            r+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                        print
                        print "Question 3: Out of the following which is called stranger gas?"
                        print
                        print " A. Ne                                      B. He"
                        print " C. Xe                                      D. Kr"
                        ans1=raw_input("Enter your option:")
                        if ans1=="c" or ans1=="C":
                            r+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                        print
                        print "Question 4: Rayleigh isolated which of the following inert gas from air?"
                        print
                        print " A. New Gas                                      B. Lazy Gas"
                        print " C. Hidden Gas                                   D. Stranger Gas"
                        ans1=raw_input("Enter your option:")
                        if ans1=="b" or ans1=="B":
                            r+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                        print
                        print "Question 5: Which noble gas has greater solubility in water?"
                        print
                        print " A. Xe                                      B. Ar"
                        print " C. He                                      D. Ne"
                        ans1=raw_input("Enter your option:")
                        if ans1=="a" or ans1=="A":
                            r+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                        print
                        print "Question 6: Helium-II liquid flows upward like a gas. This is because of?"
                        print
                        print " A. Small size                                      B. High Ionisation Enthalpy"
                        print " C. Low viscosity                                  D. Low molecular weight"
                        ans1=raw_input("Enter your option:")
                        if ans1=="c" or ans1=="C":
                            r+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                        print
                        print "Question 7: Bond angle is highest in which compound?"
                        print
                        print " A. XeO4                                      B. XeF2"
                        print " C. XeF4                                      D. XeO3"
                        ans1=raw_input("Enter your option:")
                        if ans1=="b" or ans1=="B":
                            r+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                        print
                        print "Question 8: At 2.2 K which gas can form a super fluid?"
                        print
                        print " A. He                                      B. Ne"
                        print " C. Ar                                      D. Xe"
                        ans1=raw_input("Enter your option:")
                        if ans1=="a" or ans1=="A":
                            r+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                        print
                        print "Question 9: The noble gas compound iso-structural with Bromate ion is?"
                        print
                        print " A. XeO3                                  B. XeOF4"
                        print " C. XeF2                                  D. XeF4"
                        ans1=raw_input("Enter your option:")
                        if ans1=="a" or ans1=="A":
                            r+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                        print
                        print "Question 10: The partial hydrolysis of XeF4 at low temperature gives?"
                        print
                        print " A. XeO3                                      B. XeOF2"
                        print " C. XeOF4                                     D. XeF2"
                        ans1=raw_input("Enter your option:")
                        if ans1=="b" or ans1=="B":
                            r+=1
                            print "Bingo! Thats the right answer !"
                        else:
                            print "Sorry that was the wrong answer !"
                        print "                                     End Of Quiz"
                        print "*"*80
                        print "                     Here is your Score Report"
                        print "*"*80
                        print "Number of correct answers:",r
                        print "Number of wrong answer:   ",w
                        print "-"*80
                        print "Total Score:",r*10
                        print "-"*80






                    if choice==3:
                        print "*"*80
                        print "         Welcome to the Periodic Table Game"
                        print "*"*80
                        print "-"*80
                        print " Instructions:"
                        print
                        print "                                             Level 1  "
                        print " The name of an element from the periodic table will be displayed and you will have to type in the symbol for it"
                        print " There are a total of 10 elements to answer and if you get 6 correct then u go to the next level"
                        print " Best of Luck"
                        print
                        c1=0
                        w1=0
                        print "-"*80
                        r=raw_input("Press enter when you are ready")
                        print

                        print '#',"1.   Symbol for Manganese"
                        ans2=raw_input()
                        if ans2=="Mn" or ans2=="mn":
                            print "That's Right!"
                            c1+=1
                        else:
                            print "Sorry, That's the wrong answer!"
                            print "Manganese - Mn"
                            w1+=1
                        print
                        print '#',"2.   Symbol for Thallium"
                        ans2=raw_input()
                        if ans2=="Tl" or ans2=="tl":
                            print "That's Right!"
                            c1+=1
                        else:
                            print "Sorry, That's the wrong answer!"
                            print "Thallium - Tl"
                            w1+=1
                        print
                        print '#',"3.   Symbol for Mercury"
                        ans2=raw_input()
                        if ans2=="Hg" or ans2=="hg":
                            print "That's Right!"
                            c1+=1
                        else:
                            print "Sorry, That's the wrong answer!"
                            print "Mercury - Hg"
                            w1+=1
                        print
                        print '#',"4.   Symbol for Tungsten"
                        ans2=raw_input()
                        if ans2=="W" or ans2=="w":
                            print "That's Right!"
                            c1+=1
                        else:
                            print "Sorry, That's the wrong answer!"
                            print "Tungsten - W"
                            w1+=1
                        print
                        print '#',"5.   Symbol for Molybdenum"
                        ans2=raw_input()
                        if ans2=="Mo" or ans2=="mo":
                            print "That's Right!"
                            c1+=1
                        else:
                            print "Sorry, That's the wrong answer!"
                            print "Molybdenum - Mo"
                            w1+=1
                        print
                        print '#',"6.   Symbol for Hafnium"
                        ans2=raw_input()
                        if ans2=="Hf" or ans2=="hf":
                            print "That's Right!"
                            c1+=1
                        else:
                            print "Sorry, That's the wrong answer!"
                            print "Hafnium - Hf"
                            w1+=1
                        print
                        print '#',"7.   Symbol for Osmium"
                        ans2=raw_input()
                        if ans2=="Os" or ans2=="os":
                            print "That's Right!"
                            c1+=1
                        else:
                            print "Sorry, That's the wrong answer!"
                            print "Osmium - Os"
                            w1+=1
                        print
                        print '#',"8.   Symbol for Flerovium"
                        ans2=raw_input()
                        if ans2=="Fl" or ans2=="fl":
                            print "That's Right!"
                            c1+=1
                        else:
                            print "Sorry, That's the wrong answer!"
                            print "Flerovium - Fl"
                            w1+=1
                        print
                        print '#',"9.   Symbol for Iridium"
                        ans2=raw_input()
                        if ans2=="Ir" or ans2=="ir":
                            print "That's Right!"
                            c1+=1
                        else:
                            print "Sorry, That's the wrong answer!"
                            print "Iridium - Ir"
                            w1+=1
                        print
                        print '#',"10.   Symbol for Bismuth"
                        ans2=raw_input()
                        if ans2=="Bi" or ans2=="bi":
                            print "That's Right!"
                            c1+=1
                        else:
                            print "Sorry, That's the wrong answer!"
                            print "Bismuth - Bi"
                            w1+=1
                        print
                        print " Your total score is ",c1
                        if c1>=6:
                            print " Level Passed "
                            r=raw_input("Press enter to go to the next level")
                        if c1<6:
                            print " Level Failed "
                            break
                        print " Instructions:"
                        print
                        print "-"*80

                        print "                                 Level 2  "
                        print "-> An elements atomic number is given and you have to identify the element"
                        print "-> Every correct answer fetches you 10 points and there are no negative points"
                        print "-> You need a total of 80 points to go to the next level"
                        print "-> If you get above 50 you are taken to a bonus level incase you dont have enough points"
                        print "             Best of Luck"
                        print "-"*80
                        print
                        c2=0
                        r=raw_input("Press enter when you are ready")

                        print "1. Atomic Number : 18"
                        ans3=raw_input()
                        if ans3=="Argon" or ans3=="argon":
                            print "That's right! You earn 10 points"
                            c2+=10
                        else:
                            print "Sorry that's the wrong answer!"
                        print
                        print "2. Atomic Number : 80"
                        ans3=raw_input()
                        if ans3=="Mercury" or ans3=="mercury":
                            print "That's right! You earn 10 points"
                            c2+=10
                        else:
                            print "Sorry that's the wrong answer!"
                        print
                        print "3. Atomic Number : 13"
                        ans3=raw_input()
                        if ans3=="Aluminium" or ans3=="aluminium":
                            print "That's right! You earn 10 points"
                            c2+=10
                        else:
                            print "Sorry that's the wrong answer!"
                        print
                        print "4. Atomic Number : 82"
                        ans3=raw_input()
                        if ans3=="Lead" or ans3=="lead":
                            print "That's right! You earn 10 points"
                            c2+=10
                        else:
                            print "Sorry that's the wrong answer!"
                        print
                        print "5. Atomic Number : 78"
                        ans3=raw_input()
                        if ans3=="Platinum" or ans3=="platinum":
                            print "That's right! You earn 10 points"
                            c2+=10
                        else:
                            print "Sorry that's the wrong answer!"
                        print
                        print "6. Atomic Number : 53"
                        ans3=raw_input()
                        if ans3=="Iodine" or ans3=="iodine":
                            print "That's right! You earn 10 points"
                            c2+=10
                        else:
                            print "Sorry that's the wrong answer!"
                        print
                        print "7. Atomic Number : 56"
                        ans3=raw_input()
                        if ans3=="Barium" or ans3=="barium":
                            print "That's right! You earn 10 points"
                            c2+=10
                        else:
                            print "Sorry that's the wrong answer!"
                        print
                        print "8. Atomic Number : 22"
                        ans3=raw_input()
                        if ans3=="Titanium" or ans3=="titanium":
                            print "That's right! You earn 10 points"
                            c2+=10
                        else:
                            print "Sorry that's the wrong answer!"
                        print
                        print "9. Atomic Number : 54"
                        ans3=raw_input()
                        if ans3=="Xenon" or ans3=="xenon":
                            print "That's right! You earn 10 points"
                            c2+=10
                        else:
                            print "Sorry that's the wrong answer!"
                        print
                        print "10. Atomic Number : 55"
                        ans3=raw_input()
                        if ans3=="Cesium" or ans3=="cesium":
                            print "That's right! You earn 10 points"
                            c2+=10
                        else:
                            print "Sorry that's the wrong answer!"
                        print
                        if c2>=80:
                            print "Level Passed Successfully"
                        if c2<50:
                            print "     Level Failed"
                            break
                        if c2>=50 and c2<80:
                            print "Since you have scored",c2," points, here is your chance to attempt the bonus level"
                            print
                            print "There are 4 bonus questions in this level"
                            print "If you answer a question right you get 10 points but if you answer a question wrong, 10 points are deducted"
                            print "The points that you obtain in this level will be added to your previous score and you go to the next level if you score above 80."
                            r=raw_input(" Press enter when you are ready")


                            print "^"*80
                            print "                             Bonus Level"
                            print "^"*80
                            cb=0
                            wb=0
                            print "Question 1. Which was the first element to be made artificially?"
                            ansb=raw_input()
                            if ansb=="Technetium" or ansb=="technetium":
                                print "Brilliant! You earn 10 bonus points!"
                                cb+=10
                            else:
                                print "That was the wrong the wrong answer. 10 points are deducted from your score"
                                wb+=10
                            print
                            print "Question 2. How many elements from the periodic table occur naturally?"

                            ansb=raw_input()
                            if ansb=="90":
                                print "Brilliant! You earn 10 bonus points!"
                                cb+=10
                            else:
                                print "That was the wrong the wrong answer. 10 points are deducted from your score"
                                wb+=10
                            print
                            print "Question 3. Which gas is used in arc welding?"
                            ansb=raw_input()
                            if ansb=="Argon" or ansb=="argon":
                                print "Brilliant! You earn 10 bonus points!"
                                cb+=10
                            else:
                                print "That was the wrong the wrong answer. 10 points are deducted from your score"
                                wb+=10
                            print
                            print "Question 4. Catenation is showed by which element?"
                            ansb=raw_input()
                            if ansb=="Carbon" or ansb=="carbon":
                                print "Brilliant! You earn 10 bonus points!"
                                cb+=10
                            else:
                                print "That was the wrong the wrong answer. 10 points are deducted from your score"
                                wb+=10
                            print
                            print "                         Score Report"
                            print "Total points(Level 2) ",c2
                            print "Total points in Bunus Level",cb-wb
                            print
                            ts=c2+cb-wb
                            print "Total Score: ",ts
                        if ts<80:
                            print "LEVEL FAILED"
                        if ts>=80:
                            print "Level Passed"
                            print "Welcome to the THIRD LEVEL"
                            print
                            print "Instructions:"
                            print "                                 Level 3  "
                            print "-> The details of an element such as atomic mass,group number, period or properties will be given. You have to identify the element."
                            print "-> Every correct answer fetches you 10 points and there are 5 negative points for a wrong a answer."
                            #print "-> You need a total of 80 points to go to the next level"
                            #print "-> If you get above 50 you are taken to a bonus level incase you dont have enough points"
                            print "             Best of Luck"
                            print "-"*80
                            r=raw_input("Press enter when you are ready")
                            c3=0
                            w3=0
                            print
                            print "Element 1:"
                            print
                            print "It is a yellowish, waxy, slightly see-through solid. Like magnesium, it is very reactive. It is used in the tips of the matchsticks."
                            ans3=raw_input("Enter the element name:")

                            if ans3=="Phosphorous" or ans3=="phosphorous":
                                print "That's the right answer. You earn 10 points!"
                                c3+=10
                            else:
                                print "That's the wrong answer!"
                                w3+=5
                            print
                            print "Element 2:"
                            print
                            print " It bonds with other atoms of its kind and links up into crystalline lattices. It is used to make semiconductors for computers."
                            ans3=raw_input("Enter the element name:")

                            if ans3=="Silicon" or ans3=="silicon":
                                print "That's the right answer. You earn 10 points!"
                                c3+=10
                            else:
                                print "That's the wrong answer!"
                                w3+=5
                            print
                            print "Element 3:"
                            print
                            print " Group         -	9 "
                            print "Melting point  -	2446 oC, 4434.8 oF, 2719.15 K"
                            print "Period         -	6 "
                            print "Boiling point  -	4428 oC, 8002.4 oF, 4701.15 K "
                            print "Block          -	d "
                            print "Density(kg m-3)-	22550"
                            print "Atomic number	77 "
                            ans3=raw_input("Enter the element name:")

                            if ans3=="Iridium" or ans3=="iridium":
                                print "That's the right answer. You earn 10 points!"
                                c3+=10
                            else:
                                print "That's the wrong answer!"
                                w3+=5
                            print
                            print "Element 4:"
                            print
                            print "Discovery date	1879"
                            print "Discovered by	L.F. Nilson "
                            print "Origin of the name	The name derives from 'Scandia', the Latin name for Scandinavia."
                            ans3=raw_input("Enter the element name:")

                            if ans3=="Scandium" or ans3=="scandium":
                                print "That's the right answer. You earn 10 points!"
                                c3+=10
                            else:
                                print "That's the wrong answer!"
                                w3+=5
                            print
                            print "Element 4:"
                            print
                            print "Discovery date	1803"
                            print "Discovered by	J.J. Berzelius and W. Hisinger  "
                            print "Origin of the name	Named after Roman God of Agriculture"
                            ans3=raw_input("Enter the element name:")

                            if ans3=="Cerium" or ans3=="cerium":
                                print "That's the right answer. You earn 10 points!"
                                c3+=10
                            else:
                                print "That's the wrong answer!"
                                w3+=5
                            print
                            print "Element 5:"
                            print
                            print " Group         -	2 "

                            print "Period         -	5 "

                            print "Block          -	s "
                            print "Density(kg m-3)-	22550"
                            print "Atomic mass   	87.62 "
                            ans3=raw_input("Enter the element name:")

                            if ans3=="Strontium" or ans3=="strontium":
                                print "That's the right answer. You earn 10 points!"
                                c3+=10
                            else:
                                print "That's the wrong answer!"
                                w3+=5
                            print
                            print "Element 6:"
                            print
                            print " Color         -	Silver-white"

                            print " State         -	Solid "

                            print "It is considered to be stable, although it is actually radioactive with an extremely slow rate of decay."
                            print "Atomic mass   	208.9 "
                            ans3=raw_input("Enter the element name:")

                            if ans3=="Bismuth" or ans3=="bismuth":
                                print "That's the right answer. You earn 10 points!"
                                c3+=10
                            else:
                                print "That's the wrong answer!"
                                w3+=5
                            print
                            print "Element 7:"
                            print
                            print "It was the  fourth synthetic transuranium element of the actinide series to be discovered."
                            print " It was first identified in 1944 by Seaborg, James and Morgan at the metallurgical laboratory at the University of Chicago. It was produced by the beta-particle decay of plutonium-241, which had been produced in a nuclear reactor by neutron bombardment of plutonium-239."
                            ans3=raw_input("Enter the element name:")

                            if ans3=="Americium " or ans3=="americium ":
                                print "That's the right answer. You earn 10 points!"
                                c3+=10
                            else:
                                print "That's the wrong answer!"
                                w3+=5
                            print
                            print "Element 8:"
                            print
                            print "It was the eighth synthetic transuranium element of the actinide series to be discovered."
                            print "Electron configuration:	[Rn] 5f12 7s2"
                            print "Half-life:                   20.07 hours"
                            ans3=raw_input("Enter the element name:")

                            if ans3=="Fermium " or ans3=="Fermium ":
                                print "That's the right answer. You earn 10 points!"
                                c3+=10
                            else:
                                print "That's the wrong answer!"
                                w3+=5
                            print
                            print "Element 9:"
                            print
                            print "French scientist Antoine Lavoisier named this element. Following is the experiment that lead to the discovery of this element."
                            print "In 1772 Lavoisier pooled resources with other chemists to buy a diamond, which they placed in a closed glass jar. They focused the sun's rays on the diamond with a remarkable giant magnifying glass and saw the diamond burn and disappear."

                            print "Lavoisier noted the overall weight of the jar was unchanged and that when it burned, the diamond had combined with oxygen to form carbon dioxide. He concluded that diamond and charcoal were made of the same element.Name this element."
                            ans3=raw_input("Enter the element name:")

                            if ans3=="Carbon " or ans3=="carbon ":
                                print "That's the right answer. You earn 10 points!"
                                c3+=10
                            else:
                                print "That's the wrong answer!"
                                w3+=5
                            print
                            print "Element 10:"
                            print
                            print "It forms in stars with a mass of eight or more Earth suns.Colorless under normal conditions, it glows a reddish-orange in a vacuum discharge tube."
                            print "It has the smallest liquid range of any element (2.6 oC). It has no stable compounds. Name this element."
                            ans3=raw_input("Enter the element name:")

                            if ans3=="Neon " or ans3=="Neon ":
                                print "That's the right answer. You earn 10 points!"
                                c3+=10
                            else:
                                print "That's the wrong answer!"
                                w3+=5

                            print "                     End of Level 3"
                            print
                            score3=c3-w3
                            print "Your Total Score in Level 3 is",score3
                            if score3>50:
                                print "****** LEVEL PASSED ******"
                                print "-"*80
                                print "                     Overall Scores"
                                print
                                print "Level 1              ",c1
                                print
                                print "Level 2              ",ts
                                print
                                print "Level 3              ",score3
                                print
                                totalscore=c1+ts+score3
                                print "TOTAL SCORE : ",totalscore
                                print
                                print "Your name and score will be added to the highscores"
                                file=open("Highscores.txt","a")
                                name=raw_input("Enter your name:")
                                file.write(name + "\n" + totalscore)
                                file.close()
                            else:
                                 print "     LEVEL FAILED"
                                 print "Better luck next time !"
                                 break

                z=raw_input("Press any key and Enter ( Return Key ) to go back to the school")
                pygame.init()
                size = [1000, 700]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("KRK2211")
                done = False
                clock = pygame.time.Clock()
                pygame.mouse.set_visible(1)
                x_coord = 700
                y_coord = 500
                x_speed = 0
                y_speed = 0
                x_coord = x_coord + x_speed
                y_coord = y_coord + y_speed



            x_coord = x_coord + x_speed
            y_coord = y_coord + y_speed
            screen.fill(RED)

            #MATHS CLASS
            if x_coord in range(440,670) and y_coord in range( 80, 230):
                pygame.display.flip()
                clock.tick(30)
                pygame.display.quit()
                while 1:
                    print "*"*80
                    print
                    print "Welcome to the Maths Class"
                    print "Here, we're gonna help you with a few of your calclations"
                    print
                    print "Enter 1 if you want to use our simple calculator"
                    print "Enter 2 if you want to view the fibonacci sequence"
                    print "Enter 3 if you want to do various operations on matrices"
                    print "Enter 4 if you want to quit"
                    c=raw_input("Enter your choice")
                    if c=='1':
                        while 1:
                            print "Welcome to Kiran's calculator"
                            print "Your options are"
                            print ""
                            print "1.) Addition"
                            print "2.) Subtraction"
                            print "3.) Multiplication"
                            print "4.) Division"
                            print "5.) Remainder"
                            print "6.) Quit Program"
                            print ""
                            print""
                            while 1:
                                try:
                                    choice = int(raw_input("Enter your option"))
                                    break
                                except:
                                    print "Enter only numbers"
                            print""

                            if choice==1:
                                A=input("Enter your first number")
                                B=input("Enter your second number")
                                print"The sum is = ", A+B

                            elif choice==2:
                                A=input("Enter your first number")
                                B=input("Enter your second number")
                                print"The difference is = ", A-B

                            elif choice==3:
                                A=input("Enter your first number")
                                B=input("Enter your second number")
                                print"The product is = ", A*B

                            elif choice==4:
                                A=input("Enter your first number")
                                B=input("Enter your second number")
                                print"The quotient is = ", A/B

                            elif choice==5:
                                A=input("Enter your first number")
                                B=input("Enter your second number")
                                print"The remainder is = ", A%B

                            elif choice==6:
                                break

                    if c=='2':
                        while 1:
                            try:
                                n=int(raw_input("Enter the number upto which you want the Fibonacci sequence"))
                                break
                            except:
                                print "Enter only numbers"

                        a,b=0,1
                        print a,
                        while a+b<n:
                            print b,
                            a,b=b,a+b

                    if c=='3':
                        while 1:
                            print"*"*80
                            print
                            print"Welcome to Kiran's Program on MATRIX OPERATIONS"
                            print
                            print"1.)  Add two matrices"
                            print"2.)  Subtract two matrices"
                            print"3.)  Transpose of a matrix"
                            print"4.)  Multiply two matrices"
                            print"5.)  Sum of all elements of a matrix"
                            print"6.)  Sum of row elements"
                            print"7.)  Sum of column elements"
                            print"8.)  Display both diagonals"
                            print"9.)  Display both diagonals and both their sums"
                            print"10.) Display the upper triangular and find their sum"
                            print"11.) Display the lower triangular and find their sum"
                            print"12.) Sum of even elements"
                            print"13.) Sum of alternate terms starting from [0][0]"
                            print"14.) Sum of elements divisible by a number 'n'"
                            print"15.) Quit"
                            print
                            print"*"*80
                            print""
                            count=input("Enter your choice")
                            print""
                            if count==1:
                                print "Adding two matrices"
                                add()
                            if count==2:
                                print "Subtracting to matrices"
                                sub()
                            if count==3:
                                print "Transpose of a matrix"
                                transpose()
                            if count==4:
                                print "Multiply two matrices"
                                mult()
                            if count==5:
                                print "Sum of all elements of a matrix"
                                sumelements()
                            if count==6:
                                print "Sum of row elements"
                                sumofrow()
                            if count==7:
                                print "Sum of column elements"
                                sumofcolumn()
                            if count==8:
                                print "Display both diagonals"
                                diagboth()
                            if count==9:
                                print "Display both diagonals and both their sums"
                                diagbothsum()
                            if count==10:
                                print "Display the upper triangular and find their sum"
                                uppertriangle()
                            if count==11:
                                print "Display the lower triangular and find their sum"
                                lowertriangle()
                            if count==12:
                                print "Sum of even elements"
                                sumeven()
                            if count==13:
                                print "Sum of alternate terms starting from [0][0]"
                                sumalternate()
                            if count==14:
                                print "Sum of elements divisible by a number 'n'"
                                sumofn()
                            if count==15:
                                break
                    if c=='4':
                        break
                z=raw_input("Press any key and Enter ( Return Key ) to go back to the school")
                for i in range(80):
                    print
                pygame.init()
                size = [1000, 700]
                screen = pygame.display.set_mode(size)
                pygame.display.set_caption("KRK2211")
                done = False
                clock = pygame.time.Clock()
                pygame.mouse.set_visible(1)
                x_coord = 675
                y_coord = 150
                x_speed = 0
                y_speed = 0
                x_coord = x_coord + x_speed
                y_coord = y_coord + y_speed

            #Physics CLASS
            if x_coord in range(440,670) and y_coord in range( 280, 430):
                pygame.display.flip()
                clock.tick(30)
                pygame.display.quit()

                z=raw_input("Press any key and Enter ( Return Key ) to go back to the school")
                for i in range(80):
                    print
                while 1:
                    pygame.init()
                    size = [1000, 700]
                    screen = pygame.display.set_mode(size)
                    pygame.display.set_caption("KRK2211")
                    done = False
                    clock = pygame.time.Clock()
                    pygame.mouse.set_visible(1)
                    x_coord = 675
                    y_coord = 150
                    x_speed = 0
                    y_speed = 0
                    x_coord = x_coord + x_speed
                    y_coord = y_coord + y_speed

                    movi('E:\Solar.mpg')

                    screen.fill(RED)
                    pygame.display.flip()
                    clock.tick(60)
                    for event in pygame.event.get():
                        if event.type == pygame.quit:
                            done = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos=pygame.mouse.get_pos()
                            x_coord=pos[0]
                            y_coord=pos[1]
                    if x_coord in range(900,1000) and y_coord in range( 600, 700):

                        break


            x_coord = x_coord + x_speed
            y_coord = y_coord + y_speed
            screen.fill(RED)


            #DRAWING OUR BUILDING

            DrawRect(screen, BLUE, 20, 60, 960, 590,0)
            DrawRect(screen, BLACK, 20, 60, 960, 590, 3)


            #HALL
            DrawRect(screen, BLACK, 50, 80, 350, 250, 3)
            #STAFF ROOM
            DrawRect(screen, BLACK, 50, 380, 350, 250, 3)
            #Class MATH
            DrawRect(screen, BLACK, 440, 80, 230, 150, 3)
            #Class Phy
            DrawRect(screen, BLACK, 440, 280, 230, 150, 3)
            #Class Quiz
            DrawRect(screen, BLACK, 440, 480, 230, 150, 3)
            #Class 4
            DrawRect(screen, BLACK, 720, 80, 230, 150, 3)
            #Class 5
            DrawRect(screen, BLACK, 720, 280, 230, 150, 3)

            #STAIRS
            DrawRect(screen, BLACK, 800, 530, 150, 50, 3)

            #THE TEXT AREA
            room = pygame.font.SysFont('Calibri', 35, False, False)
            location1 = room.render("X = "+str(x_coord), True, BLACK)
            screen.blit(location1, [720, 660])

            location2 = room.render("Y = "+str(y_coord), True, BLACK)
            screen.blit(location2, [860, 660])

            font = pygame.font.SysFont('Calibri', 35, True, False)
            schoolname = font.render("AL KHOR INTERNATIONAL SCHOOL - CBSE", True, BLACK)
            screen.blit(schoolname, [210, 10])

            stair = room.render("STAIRS",True,BLACK)
            screen.blit(stair, [829, 540])

            room = pygame.font.SysFont('Calibri', 45, False, False)
            math = room.render("MATHS",True,BLACK)
            screen.blit(math, [485, 130])

            chem = room.render("CHEMISTRY",True,BLACK)
            screen.blit(chem, [453, 510])
            quiz = room.render("QUIZ",True,BLACK)
            screen.blit(quiz, [500, 560])




            draw_stick_figure(screen, x_coord, y_coord)

            pygame.display.flip()
            clock.tick(60)

    #When at the reception
    if x_coord in range (250,401) and y_coord in range(400,501):
        pygame.display.flip()
        clock.tick(30)
        pygame.display.quit()
        l=[]
        loop=1
        count=0
        class admission():
            def enter(self):
                print "*"*80
                print
                admission.name=raw_input("Enter the name of the student")
                admission.sex=raw_input("Enter the sex of the student")
                admission.age = raw_input("Enter the age of the student")
                admission.grade=raw_input("Enter the class you want the student to join")
                admission.address = raw_input("Enter your address")
                admission.number = raw_input("Enter your contact number")
                print
                print "Thank you for visiting our school"
                print "Your child is not a part of class",self.grade
                print "He can now join the school on the 20th of March with the other students"
                print "He will have a great experience and we ensure great success in the future"
                print
                print "*"*80
                file = open("Admission.txt",'a')
                file.write(admission.name)
                file.write("\n")
                file.close()

            def pop(self):
                pass

            def display(self):
                print
                print "*"*80
                print "                                 AL KHOR INTERNATIONAL SCHOOL"
                print "                                      Admission Details"
                print "*"*80
                print
                print "Student's Name:     ",admission.name
                print "Sex:                ",admission.sex
                print "Age:                ",admission.age
                print "Grade:              ",admission.grade
                print "Address:            ",admission.address
                print "Admission No.:      ",admission.number
                print "*"*80
                print

        s=admission()
        s.enter()
        count=0
        while 1:
            count = raw_input("Enter 1 if you want to see the student details you entered, to verify")
            if count=='1':
                s.display()
            count=raw_input("Enter 1 if you want to edit the details of the student")
            if count=='1':
                s.enter()
            else :
                break
        z=raw_input("Press any key and Enter ( Return Key ) to go back to the school")
        for i in range(80):
            print
        pygame.init()
        size = [1000, 700]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("KRK2211")
        done = False
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(1)
        x_coord = 401
        y_coord = 450
        x_speed = 0
        y_speed = 0
        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed

    #AT THE HALL

    if x_coord in range (250,751) and y_coord in range (90,340):
        a=input("Enter Game")
        if a==1:

            import math
            import pygame
            black = (0, 0, 0)
            white = (255, 255, 255)
            blue = (0, 0, 255)

            # Size of break-out blocks
            block_width = 000
            block_height = 20

            class Block(pygame.sprite.Sprite):
                """This class represents each block that will get knocked out by the ball
                It derives from the "Sprite" class in Pygame """

                def __init__(self, color, x, y):

                    # Call the parent class (Sprite) constructor
                    pygame.sprite.Sprite.__init__(self)

                    # Create the image of the block of appropriate size
                    # The width and height are sent as a list for the first parameter.
                    self.image = pygame.Surface([block_width, block_height])

                    # Fill the image with the appropriate color
                    self.image.fill(color)

                    # Fetch the rectangle object that has the dimensions of the image
                    self.rect = self.image.get_rect()

                    # Move the top left of the rectangle to x,y.
                    # This is where our block will appear..
                    self.rect.x = x
                    self.rect.y = y


            class Ball(pygame.sprite.Sprite):

                speed = 10.0

                #Position
                x = 0.0
                y = 180.0

                #Direction degrees....
                direction = 200

                width = 10
                height = 10

                # Constructor. Pass in the color of the block, and its x and y position
                def __init__(self):
                    # Call the parent class (Sprite) constructor
                    pygame.sprite.Sprite.__init__(self)

                    # Create the image of the ball
                    self.image = pygame.Surface([self.width, self.height])

                    # Color the ball
                    self.image.fill(white)

                    # Get a rectangle object that shows where our image is
                    self.rect = self.image.get_rect()

                    # Get attributes for the height/width of the screen
                    self.screenheight = pygame.display.get_surface().get_height()
                    self.screenwidth = pygame.display.get_surface().get_width()

                def bounce(self, diff):
                    """ This function will bounce the ball
                        off a horizontal surface (not a vertical one) """

                    self.direction = (180 - self.direction) % 360
                    self.direction -= diff

                def update(self):
                    """ Update the position of the ball. """
                    # Sine and Cosine work in degrees, so we have to convert them
                    direction_radians = math.radians(self.direction)

                    # Change the position (x and y) according to the speed and direction
                    self.x += self.speed * math.sin(direction_radians)
                    self.y -= self.speed * math.cos(direction_radians)

                    # Move the image to where our x and y are
                    self.rect.x = self.x
                    self.rect.y = self.y

                    # Do we bounce off the top of the screen?
                    if self.y <= 0:
                        self.bounce(0)
                        self.y = 1

                    # Do we bounce off the left of the screen?
                    if self.x <= 0:
                        self.direction = (360 - self.direction) % 360
                        self.x = 1

                    # Do we bounce of the right side of the screen?
                    if self.x > self.screenwidth - self.width:
                        self.direction = (360 - self.direction) % 360
                        self.x = self.screenwidth - self.width - 1

                    # Did we fall off the bottom edge of the screen?
                    if self.y > 600:
                        return True
                    else:
                        return False

            class Player(pygame.sprite.Sprite):
                """ This class represents the bar at the bottom that the player controls. """

                def __init__(self):
                    """ Constructor for Player. """
                    # Call the parent's constructor
                    pygame.sprite.Sprite.__init__(self)

                    self.width = 75
                    self.height = 15
                    self.image = pygame.Surface([self.width, self.height])
                    self.image.fill((white))

                    # Make our top-left corner the passed-in location.
                    self.rect = self.image.get_rect()
                    self.screenheight = pygame.display.get_surface().get_height()
                    self.screenwidth = pygame.display.get_surface().get_width()

                    self.rect.x = 0
                    self.rect.y = self.screenheight-self.height

                def update(self):
                    """ Update the player position. """
                    # Get where the mouse is
                    pos = pygame.mouse.get_pos()
                    # Set the left side of the player bar to the mouse position
                    self.rect.x = pos[0]
                    # Make sure we don't push the player paddle
                    # off the right side of the screen
                    if self.rect.x > self.screenwidth - self.width:
                        self.rect.x = self.screenwidth - self.width

            # Call this function so the Pygame library can initialize itself
            pygame.init()
            screen = pygame.display.set_mode([800, 600])
            pygame.display.set_caption('Breakout')
            pygame.mouse.set_visible(0)
            font = pygame.font.Font(None, 36)
            background = pygame.Surface(screen.get_size())
            blocks = pygame.sprite.Group()
            balls = pygame.sprite.Group()
            allsprites = pygame.sprite.Group()

            # Create the player paddle object
            player = Player()
            allsprites.add(player)

            # Create the ball
            ball = Ball()
            allsprites.add(ball)
            balls.add(ball)

            # The top of the block (y position)
            top = 80

            # Number of blocks to create
            blockcount = 32

            # --- Create blocks

            # Five rows of blocks
            for row in range(5):
                # 32 columns of blocks
                for column in range(0, blockcount):
                    # Create a block (color,x,y)
                    block = Block(blue, column * (block_width + 2) + 1, top)
                    blocks.add(block)
                    allsprites.add(block)
                # Move the top of the next row down
                top += block_height + 2

            # Clock to limit speed
            clock = pygame.time.Clock()

            # Is the game over?
            game_over = False

            # Exit the program?
            exit_program = False

            # Main program loop
            while exit_program != True:

                # Limit to 30 fps
                clock.tick(30)

                # Clear the screen
                screen.fill(black)

                # Process the events in the game
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_program = True

                # Update the ball and player position as long
                # as the game is not over.
                if not game_over:
                    # Update the player and ball positions
                    player.update()
                    game_over = ball.update()

                # If we are done, print game over
                if game_over:
                    text = font.render("Game Over", True, white)
                    textpos = text.get_rect(centerx=background.get_width()/2)
                    textpos.top = 300
                    screen.blit(text, textpos)

                # See if the ball hits the player paddle
                if pygame.sprite.spritecollide(player, balls, False):
                    # The 'diff' lets you try to bounce the ball left or right
                    # depending where on the paddle you hit it
                    diff = (player.rect.x + player.width/2) - (ball.rect.x+ball.width/2)

                    # Set the ball's y position in case
                    # we hit the ball on the edge of the paddle
                    ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
                    ball.bounce(diff)

                # Check for collisions between the ball and the blocks
                deadblocks = pygame.sprite.spritecollide(ball, blocks, True)

                # If we actually hit a block, bounce the ball
                if len(deadblocks) > 0:
                    ball.bounce(0)

                    # Game ends if all the blocks are gone
                    if len(blocks) == 0:
                        game_over = True

                # Draw Everything
                allsprites.draw(screen)

                # Flip the screen and show what we've drawn
                pygame.display.flip()

            pygame.display.quit()
            pygame.init()
            size = [1000, 700]
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption("KRK2211")
            done = False
            clock = pygame.time.Clock()
            pygame.mouse.set_visible(1)
            x_coord = 401
            y_coord = 450
            x_speed = 0
            y_speed = 0
            x_coord = x_coord + x_speed
            y_coord = y_coord + y_speed
        '''import pygame
        from random import randint

        green = (35, 232, 61)
        blue = (37,241,245)
        black = (0,0,0)
        grey = (9,105,16)
        grey2 = (24,168,33)
        grey3 = (220,220,220)
        green2 = (161,255,167)
        green3 = (87,255,98)
        yellow = (246,255,0)
        white = (255,255,255)
        orange = (255,187,0)
        brown = (143,71,0)

        pygame.init()

        size = 700, 500
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Flappy Bird")

        done = False

        clock = pygame.time.Clock()

        def obstacle(xloc, xsize, yloc, ysize):
            pygame.draw.rect(screen, green, [xloc, yloc, xsize, ysize])
            pygame.draw.rect(screen, green, [xloc, yloc+ysize+space, xsize, ysize+500])
            pygame.draw.rect(screen, black, [xloc+63, yloc, 7, ysize])
            pygame.draw.rect(screen, grey, [xloc+56, yloc, 7, ysize])
            pygame.draw.rect(screen, grey2, [xloc+49, yloc, 7, ysize])
            pygame.draw.rect(screen, green2, [xloc, yloc, 7, ysize])
            pygame.draw.rect(screen, green3, [xloc+7, yloc, 7, ysize])

            pygame.draw.rect(screen, black, [xloc+63, yloc+ysize+space, 7, ysize+500])
            pygame.draw.rect(screen, grey, [xloc+56, yloc+ysize+space, 7, ysize+500])
            pygame.draw.rect(screen, grey2, [xloc+49, yloc+ysize+space, 7, ysize+500])
            pygame.draw.rect(screen, green2, [xloc, yloc+ysize+space, 7, ysize+500])
            pygame.draw.rect(screen, green3, [xloc+7, yloc+ysize+space, 7, ysize+500])


        def ball(x, y):
            pygame.draw.circle(screen, yellow, [x, int(y)], 20)
            pygame.draw.circle(screen, white, [int(x+12), int(y-12)], 10)
            pygame.draw.polygon(screen, orange, [(x+12,y+5),(x+12,y-5), (x+25, y)])
            pygame.draw.circle(screen, black, [int(x+12), int(y-12)], 1)
            pygame.draw.circle(screen,black,[int(x-12), int(y+10)], 11)
            pygame.draw.circle(screen, yellow,[int(x-12), int(y+10)], 10)

        def gameover():

            pygame.init()
            size = [1000, 700]
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption("KRK2211")
            done = False
            clock = pygame.time.Clock()
            pygame.mouse.set_visible(1)
            x_coord = 191
            y_coord = 141
            x_speed = 0
            y_speed = 0

        def Score(score):
            font = pygame.font.Font(None ,50)
            text = font.render(("Score: "+str(score)), True, black)
            screen.blit(text, [0, 0])


        def cloud(clx, cly):
            pygame.draw.circle(screen, grey3, [int(clx),int(cly)],20)
            pygame.draw.circle(screen, grey3, [int(clx+15),int(cly-10)],20)
            pygame.draw.circle(screen, grey3, [int(clx+30),int(cly)],20)
            pygame.draw.circle(screen, grey3, [int(clx+15),int(cly+10)],20)

        def Ground(ground):
            pygame.draw.rect(screen, brown, [0, ground, 700, 60])

        #def city():





        xloc = 700
        xsize = 70
        yloc = 0
        ysize = randint(0, 325)
        x = 350
        y = 250
        yspeed = 0
        ground = 494.5
        obspeed = 1
        space = 150
        limit = -80
        score = 0



        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        yspeed = -1.75

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        yspeed = 1.5

            screen.fill(blue)

            cloud(45,40)
            cloud(83, 482)
            cloud(383, 39)
            cloud(524, 23)
            cloud(467, 63)
            cloud(623, 424)
            cloud(330, 260)
            cloud(600, 150)
            cloud(150, 150)
            cloud(450, 400)
            obstacle(xloc, xsize, yloc, ysize)
            ball(x, y)
            Score(score)




            if y+20 > ground:
                gameover()
                obspeed = 0
                yspeed = 0

            else:
                xloc -= obspeed
                y += yspeed

            if x+20 > xloc and y-20 < ysize and x-15 < xsize+xloc:
                gameover()
                obspeed = 0
                yspeed = 0

            else:
                xloc -= obspeed
                y += yspeed

            if x+20 > xloc and y+20 > ysize+space and x-15 < xsize+xloc:
                gameover()
                obspeed = 0
                yspeed = 0

            else:
                xloc -= obspeed
                y += yspeed

            if xloc < limit:
                ysize = randint(0, 400)
                xloc = 700

            else:
                xloc -= obspeed
                y += yspeed

            if x > xloc and x < xloc+3:
                score = (score + 1)


            pygame.display.flip()

            clock.tick(60)


pygame.quit()
        pygame.init()
        size = [1000, 700]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("KRK2211")
        done = False
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(1)
        x_coord = 191
        y_coord = 141
        x_speed = 0
        y_speed = 0'''



    #WHEN PERSON GOES TO THE REPORT
    if x_coord in range (600,751) and y_coord in range (400,501):
        pygame.display.flip()
        clock.tick(30)
        pygame.display.quit()
        class Student(object):
            def __init__(self):
                self.name=0
                self.subject1=0
                self.subject2=0
                self.subject3=0
                self.subject4=0
                self.subject5=0
                self.total_marks=0
                self.percentage=0
            def input_data(self):
                self.name=raw_input("Enter name :")
                while 1:
                    self.subject1=raw_input("Physics :")
                    self.subject2=raw_input("Chemistry :")
                    self.subject3=raw_input("Maths :")
                    self.subject4=raw_input("English :")
                    self.subject5=raw_input("Computer Science :")
                    if self.subject1.isdigit() and self.subject2.isdigit() and self.subject3.isdigit() and self.subject4.isdigit() and self.subject5.isdigit():
                        if abs(int(self.subject1))<=100 and abs(int(self.subject2))<=100 and abs(int(self.subject3))<=100 and abs(int(self.subject4))<=100 and abs(int(self.subject5))<=100:
                            break
                        else :
                            print
                            print "-"*80
                            print
                            print "Please enter numbers less than hundred for your grades !"
                            print
                            print "-"*80
                            print
                    else :
                        print
                        print "-"*80
                        print
                        print "Please enter only numbers for the marks"
                        print
                        print "-"*80
                        print
                self.compute_percentage()
            def compute_percentage(self):
                self.total_marks=int(self.subject1)+int(self.subject2)+int(self.subject3)+int(self.subject4)+int(self.subject5)
                self.percentage=self.total_marks/5.0
            def showdata(self):
                print
                print "*"*80
                print
                print "             AL KHOR INTERNATIONAL SCHOOL"
                print "               ACADEMIC YEAR 2014-2015"
                print "                      CLASS XII"
                print "                        MARKS"
                print "Subject              Marks"
                print "Physics          :  ",self.subject1
                print "Chemistry        :  ",self.subject2
                print "Maths            :  ",self.subject3
                print "English          :  ",self.subject4
                print "Computer Science :  ",self.subject5
                print "Total marks      :  ",self.total_marks
                print "Percentage       :  ",self.percentage
                print
                print "*"*80
                print
        S1=Student()
        S1.input_data()
        S1.showdata()
        z=raw_input("Press any key and Enter ( Return Key ) to go back to the school")
        for i in range(80):
            print
        pygame.init()
        size = [1000, 700]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("KRK2211")
        done = False
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(1)
        x_coord = 580
        y_coord = 450
        x_speed = 0
        y_speed = 0
        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed



    #WHEN PERSON GOES TO THE CANTEEN
    if x_coord in range (40,191) and y_coord in range (90,191):
        pygame.display.flip()
        clock.tick(30)
        pygame.display.quit()
        loop=1
        while loop==1:
            sum=0
            print
            print "*"*80
            print
            print "WELCOME TO THE CANTEEN"
            print "What do you want to order ?"
            print "1. Breakfast"
            print "2. Lunch"
            print "3. Beverages/Dessert"
            print
            print "*"*80
            print
            while 1:
                choice1=raw_input("Enter your choice")
                if choice1.isdigit():
                    if int(choice1)<=3 and int(choice1)>0:
                        break
                    else:
                        print "Enter a number from the list"
                else :
                    print
                    print "*"*80
                    print
                    print "Please enter only numbers"
                    print
                    print "*"*80
                    print
            if choice1=='1':
                print
                print "~"*80
                print
                print "        ~~~~ Here's your breakfast menu ~~~~"
                print "  Item Number | Item name                 | Price"
                print "      1       | Pasta                     | 10 "
                print "      2       | Noodles                   |  6 "
                print "      3       | Mini Pizza                |  5 "
                print "      4       | Spring Roll               |  4 "
                print "      5       | Cutlets                   |  4 "
                print "      6       | Bread with Jam            |  6"
                print "      7       | Omlet                     |  5 "
                print "      8       | Samosas                   |  5 "
                print
                print "~"*80
                print
                while 1:
                    n1=raw_input("Enter number of items you want to order")
                    if n1.isdigit():
                        break
                    else :
                        print " Please enter only numbers "
                n1=int(n1)
                Breakfast=["Pasta","Noodles","Mini Pizza","Spring Roll","Cutlets","Bread with Jam","Omlet","Samosas"]
                Price1=[10,6,5,4,4,6,5,5]
                for i in range(n1):
                    while 1:
                        choice2=raw_input("Enter the item you want to order")
                        if choice2.isdigit():
                            break
                        else:
                            print
                            print "&&&&&&&&&&&&&&&&&&&&&&"
                            print "$                    $"
                            print "& Enter only numbers &"
                            print "$                    $"
                            print "&&&&&&&&&&&&&&&&&&&&&&"
                            print
                    choice2=int(choice2)

                    if choice2 in range(len(Breakfast)+1):
                        print "Enter the number of",Breakfast[choice2-1],"You want"
                        while 1:
                            Qty=raw_input()
                            if Qty.isdigit():
                                break
                            else:
                                print
                                print "&&&&&&&&&&&&&&&&&&&&&&"
                                print "$                    $"
                                print "& Enter only numbers &"
                                print "$                    $"
                                print "&&&&&&&&&&&&&&&&&&&&&&"

                                print
                        Qty=int(Qty)
                        sum+=Price1[choice2-1]*Qty
            if choice1=='2':
                print
                print "~"*80
                print
                print "        ~~~~ Here's your Lunch menu ~~~~"
                print "  Item Number | Item name                 | Price"
                print "      1       | Fried Rice                | 19 "
                print "      2       | Noodles                   | 10 "
                print "      3       | Veg Pizza                 | 20 "
                print "      4       | Veg. Biryani              | 24 "
                print "      5       | Chicken Biryani           | 25 "
                print "      6       | Chicken Pizza             | 23 "
                print "      7       | Mixed Veg curry           | 8 "
                print "      8       | Butter Chicken            | 10 "
                print
                print "~"*80
                print
                while 1:
                    n1=raw_input("Enter number of items you want to order")
                    if n1.isdigit():
                        break
                    else:
                            print
                            print "&&&&&&&&&&&&&&&&&&&&&&"
                            print "$                    $"
                            print "& Enter only numbers &"
                            print "$                    $"
                            print "&&&&&&&&&&&&&&&&&&&&&&"
                            print
                n1=int(n1)
                Lunch=["Fried Rice","Noodles","Veg Pizza","Veg. Biryani","Chicken Biryani","Chicken Pizza","Mixed Veg curry","Butter Chicken"]
                Price1=[19,10,20,24,25,23,8,10]
                for i in range(n1):
                    while 1:
                        choice2=raw_input("Enter the item you want to order")
                        if choice2.isdigit():
                            break
                        else:
                                print
                                print "&&&&&&&&&&&&&&&&&&&&&&"
                                print "$                    $"
                                print "& Enter only numbers &"
                                print "$                    $"
                                print "&&&&&&&&&&&&&&&&&&&&&&"
                                print
                    choice2=int(choice2)
                    if choice2 in range(len(Lunch)+1):
                        print "Enter the number of",Lunch[choice2-1],"You want"
                        while 1:
                            Qty=raw_input()
                            if Qty.isdigit():
                                break
                            else:
                                print
                                print "&&&&&&&&&&&&&&&&&&&&&&"
                                print "$                    $"
                                print "& Enter only numbers &"
                                print "$                    $"
                                print "&&&&&&&&&&&&&&&&&&&&&&"
                                print
                        Qty=int(Qty)
                        sum+=Price1[choice2-1]*Qty
            if choice1=='3':
                print
                print "~"*80
                print
                print "        ~~~~ Here's your menu ~~~~"
                print "  Item Number | Item name                 | Price"
                print "      1       | Mango Tango               | 4 "
                print "      2       | Sherley Temple            | 4 "
                print "      3       | Juice                     | 5 "
                print "      4       | Milkshake                 | 8 "
                print "      5       | Tea                       | 4 "
                print "      6       | Coffee                    | 4 "
                print "      7       | Chocolate Tart            | 5 "
                print "      8       | Mango Kulfi               | 5 "
                print
                print "~"*80
                print
                while 1:
                    n1=raw_input("Enter number of items you want to order")
                    if n1.isdigit():
                        break
                    else:
                            print
                            print "&&&&&&&&&&&&&&&&&&&&&&"
                            print "$                    $"
                            print "& Enter only numbers &"
                            print "$                    $"
                            print "&&&&&&&&&&&&&&&&&&&&&&"
                            print
                n1=int(n1)
                B=["Mango Tango","Sherley Temple","Juice","Milkshake","Tea","Coffee","Chocolate Tart","Mango Kulfi"]
                Price1=[4,4,5,8,4,4,5,5]
                for i in range(n1):
                    while 1:
                        try:
                            choice2=int(raw_input("Enter the item you want to order"))
                            break
                        except:
                            print "Enter only numbers"

                    if choice2 in range(len(B)+1):
                        print "Enter the number of",B[choice2-1],"You want"
                        while 1:
                            Qty=raw_input()
                            if Qty.isdigit():
                                break
                            else:
                                print
                                print "&&&&&&&&&&&&&&&&&&&&&&"
                                print "$                    $"
                                print "& Enter only numbers &"
                                print "$                    $"
                                print "&&&&&&&&&&&&&&&&&&&&&&"

                                print
                        Qty=int(Qty)
                        sum+=Price1[choice2-1]*Qty
            print "Your total bill is : ",sum
            print
            loop=0
        z=raw_input("Press any key and Enter ( Return Key ) to go back to the school")
        for i in range(80):
                print
        pygame.init()
        size = [1000, 700]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("KRK2211")
        done = False
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(1)
        x_coord = 191
        y_coord = 141
        x_speed = 0
        y_speed = 0



#WHEN PERSON GOES TO THE STORE
    if x_coord in range (810,961) and y_coord in range (90,191):
        pygame.display.flip()
        clock.tick(30)
        pygame.display.quit()
        loop=1
        while loop==1:
            sum=0
            print "WELCOME TO THE STORE"
            print "What items do you seek ?"
            print "1. Stationery"
            print "2. Books"
            print "3. Uniform"
            while 1:
                try:
                    choice1=int(raw_input("Enter your choice"))
                    if choice1 not in [1,2,3]:
                        print "Enter a number from 1 to 3"
                    else :
                        break
                except :
                    print
                    print "Please Enter only numbers"
                    print

            if choice1==1:
                print
                print "~"*80
                print
                print "        ~~~~ Here are the available stationary items ~~~~"
                print "  Item Number | Item name                 | Price"
                print "      1       | Pens                      | 10 "
                print "      2       | Markers                   | 25 "
                print "      3       | Dusters                   | 10 "
                print "      4       | Staplers                  |  4 "
                print "      5       | Masking Tape              |  4 "
                print "      6       | Papers A4 size Bundle     | 20 "
                print "      7       | Erasers                   | 10 "
                print "      8       | Files                     | 15 "
                print
                print "~"*80
                print
                while 1:
                        try:
                            n1=int(raw_input("Enter number of items you want to order"))
                            break
                        except:
                            print
                            print "Please enter a number"
                            print
                Stationary=["Pens","Markers","Dusters","Staplers","Masking Tape","Papers A4 size Bundle","Erasers","Files"]
                Price1=[10,25,10,4,4,20,10,15]
                for i in range(n1):
                    while 1:
                            try:
                                choice2=int(raw_input("Enter the item you want to order"))
                                break
                            except :
                                print
                                print "Please enter a number"
                                print
                    if choice2 in range(len(Stationary)+1):
                        print "Enter the number of",Stationary[choice2-1],"You want"
                        while 1:
                            try:
                                Qty=int(raw_input())
                                break
                            except:
                                print
                                print "Please enter a number"
                                print
                        sum+=Price1[choice2-1]*Qty

            if choice1==2:
                print
                print "~"*80
                print
                print "        ~~~~ Here are the available books in the store ~~~~"
                print "  Item Number | Item name                    |Grades         | Price"
                print "      1       | Science Textbook             |5,6,7,8        | 55 "
                print "      2       | Maths Textbook               |5,6,7,8        | 55 "
                print "      3       | Social Science Textbooks     |5,6            | 65 "
                print "      4       | English Textbook             |5,6,7,8        | 75"
                print "      5       | Computer Textbook            |5,6,7,8        | 50 "
                print "      6       | History Textbook             |7,8,9,10       | 30 "
                print "      7       | Civics Textbook              |7,8            | 58 "
                print "      8       | Political Science Textbook   |7,8,9,10       | 50 "
                print "      9       | Economics                    |9,10           | 39 "
                print "      10      | Physics                      |11,12          | 63 "
                print "      11      | Chemistry                    |11,12          | 81 "
                print "      12      | English Core (2 books)       |11,12          | 90 "
                print
                print "~"*80
                print


                while 1:
                        try:
                            n1=int(raw_input("Enter number of items you want to order"))
                            break
                        except:
                            print
                            print "Please enter a number"
                            print
                Books=["Science Textbook","Maths Textbook","Social Science Textbooks","English Textbook","Computer Textbook","History Textbook ","Civics Textbook ","Political Science Textbook","Economics","Physics","Chemistry","English Core (2 books)"]
                Price1=[55,55,65,75,50,30,58,50,39,63,81,90]
                for i in range(n1):
                    while 1:
                            try:
                                choice2=int(raw_input("Enter the item you want to order"))
                                break
                            except :
                                print
                                print "Please enter a number"
                                print
                    if choice2 in range(len(Books)+1):
                        print "Enter the number of",Books[choice2-1],"You want"
                        while 1:
                            try:
                                Qty=int(raw_input("Enter the item you want to order"))
                                break
                            except :
                                print
                                print "Please enter a number"
                                print
                        sum+=Price1[choice2-1]*Qty
            if choice1==3:
                print
                print "~"*80
                print
                print "        ~~~~ Uniform List ~~~~"
                print "  Item Number | Item name                        | Price"
                print "      1       | White long-sleeved shirt         | 45 "
                print "      2       | House polo sports shirt          | 40 "
                print "      3       | P.E. T-Shirt                     | 50 "
                print "      4       | School blazer                    | 80 "
                print "      5       | School jumper                    | 49 "
                print "      6       | P.E. Shorts                      | 56 "
                print "      7       | Grey trousers                    | 69 "
                print "      8       | Grey Skirts-Long                 | 55 "
                print "      9       | Grey Skirts-Short                | 50 "
                print "      10       | Grey Shorts                      | 55 "
                print "      11       | School tracksuit top             | 60 "
                print "      12       | School tracksuit pants           | 65 "
                print "      13       | School tie                       | 15 "
                print "      14       | White socks                      | 15 "
                print
                print "~"*80
                print

                while 1:
                        try:
                            n1=int(raw_input("Enter number of items you want to order"))
                            break
                        except:
                            print
                            print "Please enter a number"
                            print
                Uniform=["White long-sleeved shirt","House polo sports shirt","P.E. T-Shirt ","School blazer ","School jumper","P.E. Shorts"," Grey trousers","Grey Skirts-Long","Grey Skirts-Short","Grey Shorts","School tracksuit top","School tracksuit pant","School tie","White socks"]
                Price1=[45,40,50,80,49,56,69,55,50,60,65,15,15]
                for i in range(n1):
                    while 1:
                            try:
                                choice2=int(raw_input("Enter the item you want to order"))
                                break
                            except :
                                print
                                print "Please enter a number"
                                print
                    if choice2 in range(len(Uniform)+1):
                        print "Enter the number of",Uniform[choice2-1],"You want"
                        while 1:
                            try:
                                Qty=int(raw_input("Enter the item you want to order"))
                                break
                            except :
                                print
                                print "Please enter a number"
                                print
                        sum+=Price1[choice2-1]*Qty
            print "Your total bill is : ",sum

            loop=0
        z=raw_input("Press any key and Enter ( Return Key ) to go back to the school")
        pygame.init()
        size = [1000, 700]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("KRK2211")
        done = False
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(1)
        x_coord = 1000
        y_coord = 750
        x_speed = 0
        y_speed = 0


    #When the person goes to the Principal's office
    if x_coord in range (40,191) and y_coord in range (400,501):
        pygame.display.quit()
        print
        print "*"*80
        print
        print "Welcome to the principal's office!."
        print "Do you have an appointment ?"
        print "Enter 1 if yes, or enter 2 if you'd like to make an appointment"
        print
        print "*"*80
        print

        n=input()
        if n==1:
            print "*"*80
            print "What is your appointment code?"
            print
            while 1:
                numb=raw_input()
                if numb.isdigit():
                    break
                else :
                    print
                    print "Please enter your appointment code"
                    print
            numb=int(numb)
            print
            if numb==code:

                print "Hello! You're now talking to the principal of the school"
                print "So what is your concern?"
                ans1=raw_input()
                print "Alright. So have you informed someone about it before?"
                ans2=raw_input("Tell 'yes' or 'no'")
                if ans2=="yes":
                    print "You should consider filling in the complaint/suggestion form.If you have already done so then I shall look into the matter as soon as possible!"
                if ans2=="no":
                    print "Then please inform the concerned department/authority. Also do fill in the complaint/suggestion form so that I can personally look into the matter as soon as possible."
                print "So is there any other issue that you want to bring up right now?"
                ans3=raw_input("Enter 'yes' or 'no'")
                if ans3=="yes":
                    print "Ok. So what else do you want to discuss about?"
                    print "1. Student progress"
                    print "2. To conduct a seminar/assembly in the school"
                    print "3. Violation of school rules by a student"
                    print
                    while 1:
                        a=raw_input("Tell your choice number:")
                        if a.isdigit():
                            if int(a) in [1,2,3]:
                                break
                            else:
                                print
                                print "Please Enter a number from 1 to 3"
                                print
                        else :
                            print
                            print "Enter a number"
                            print
                    a=int(a)
                    if a==1:
                        name=raw_input("What is the student's name?")
                        cl=raw_input("Which class is he/she in?")
                        while 1:

                            g=raw_input("Ok so what was his average score the last time?")
                            if g.isdigit():
                                break

                        if int(g)>=90:
                            print "Well your ward is making an excellent progress and is very hardworking. Your ward is sure to achieve success in the due course and we are very proud of the child !"
                        if int(g)<90:
                            import random
                            var5=random.randint(1,4)

                            if var5==1:
                                print "Your child's academic progress has been really good from the beginning. But it would be really nice if he/she takes part in the co-scholastic activities as we want an overall development of the child."
                            if var5==2:
                                print "Your child is making a good progress academically. But I do get a lot of complaints from the teachers about his/her behaviour. Please ensure that your ward is disciplined and well-mannered."
                            if var5==3:
                                print "Your child is a brilliant child. Except for his mischief and notorious behaviour, he is adored by all the teachers. It would be great if he/she stays more focused."
                            print "For further report please meet the respective class teacher."

                    if a==2:
                        print "What do you want to conduct the assembly for the students about?"
                        ans4=raw_input()
                        import random
                        date=random.randint(1,31)
                        print "That's great. Since the students are busy with their exams I would like to schedule the date of your assembly to",date,"th of this month"
                    if a==3:
                        name=raw_input("What is the name of the student?")
                        print "Your child has been violating the school rules these days and I am very disappointed to say that I have to take strict action against this and suspend him/her for a week.",name," can join the classes after his/her suspension term ends!"
                print "Thank you for expressing your views and concerns. Feel free to meet me again and looking forward to see you soon :)"








        if n==2:
            print
            print
            print "*"*80
            print "At what time do you want your appointment?"
            import random
            n=raw_input()
            code=random.randint(100000,200000)
            print "Your appointment code is",code
            print "Thank you!"
            print
            print "*"*80

        z=raw_input("Press any key and Enter ( Return Key ) to go back to the school")
        pygame.init()
        size = [1000, 700]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("KRK2211")
        done = False
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(1)
        x_coord = 191
        y_coord = 451
        x_speed = 0
        y_speed = 0



    #When the person goes to the clinic
    if x_coord in range(41, 190) and y_coord in range(251, 351):
        pygame.display.quit()
        print "PYTHON PROGRAMMING LANGUAGE"
        class Hospital(object):
            def __init__(self, name, age, bloodgroup, height, weight):
                self.name=name
                self.age=age
                self.bloodgroup=bloodgroup
                self.height=height
                self.weight=weight
            def disease(self):
                pass
            def medicine(self):
                pass





        z=raw_input("Press any key and Enter ( Return Key ) to go back to the school")
        pygame.init()
        size = [1000, 700]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("KRK2211")
        done = False
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(1)
        x_coord = 195
        y_coord = 290
        x_speed = 0
        y_speed = 0
    # BACK TO GROUND FLOOR
    if x_coord <0:
        x_coord=1000

    if y_coord <0:
        y_coord=700

    if x_coord >1000:
        x_coord=0

    if y_coord >700:
        y_coord=0

    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    screen.fill(GREEN)

    #DRAWING OUR BUILDING

    DrawRect(screen, BLUE, 20, 70, 960, 560,0)
    DrawRect(screen, BLACK, 20, 70, 960, 560, 3)
    #DOOR
    DrawRect(screen, BLACK, 420, 550, 160, 80, 3)
    #STAIRS
    DrawRect(screen, BLACK, 800, 530, 150, 50, 3)
    #RECEPTION
    DrawRect(screen, BLACK, 250, 400, 150, 100, 3)
    #PRINCIPAL
    DrawRect(screen, BLACK, 40, 400, 150, 100, 3)
    #HALL
    DrawRect(screen, BLACK, 250, 90, 500, 250, 3)
    #CLINIC
    DrawRect(screen, BLACK, 40, 250, 150, 100, 3)
    #CANTEEN
    DrawRect(screen, BLACK, 40, 90, 150, 100, 3)
    #REPORT CARDS
    DrawRect(screen, BLACK, 600, 400, 150, 100, 3)
    #STORE
    DrawRect(screen, BLACK, 810, 90, 150, 100, 3)
    #LOWER
    DrawRect(screen, BLACK, 810, 250, 150, 100, 3)
    #LIBRARY
    DrawRect(screen, BLACK, 810, 400, 150, 100, 3)

    #THE TEXT AREA
    font = pygame.font.SysFont('Calibri', 35, True, False)
    schoolname = font.render("AL KHOR INTERNATIONAL SCHOOL - CBSE", True, BLACK)
    screen.blit(schoolname, [210, 19])

    room = pygame.font.SysFont('Calibri', 35, False, False)
    clinic = room.render("CLINIC",True,BLACK)
    screen.blit(clinic, [65, 283])

    canteen = room.render("CANTEEN",True,BLACK)
    screen.blit(canteen, [47, 120])

    store = room.render("STORE",True,BLACK)
    screen.blit(store, [840, 123])

    report = room.render("REPORT",True,BLACK)
    screen.blit(report, [620, 420])
    card = room.render("CARDS",True,BLACK)
    screen.blit(card, [625, 450])

    rept = pygame.font.SysFont('Calibri', 32, False, False)
    reception = rept.render("RECEPTION",True,BLACK)
    screen.blit(reception, [252, 435])

    principaloff = pygame.font.SysFont('Calibri', 30, False, False)
    principal = principaloff.render("PRINCIPAL'S",True,BLACK)
    screen.blit(principal, [44, 420])
    office = principaloff.render("OFFICE",True,BLACK)
    screen.blit(office, [70, 450])

    lib = room.render("LIBRARY",True,BLACK)
    screen.blit(lib, [825, 432])

    stair = room.render("STAIRS",True,BLACK)
    screen.blit(stair, [829, 540])

    hall = room.render("HALL",True,BLACK)
    screen.blit(hall, [465, 200])

    location1 = room.render("X = "+str(x_coord), True, BLACK)
    screen.blit(location1, [860, 635])

    location2 = room.render("Y = "+str(y_coord), True, BLACK)
    screen.blit(location2, [860, 665])

    draw_stick_figure(screen, x_coord, y_coord)

    pygame.display.flip()
    clock.tick(600)
pygame.quit()
