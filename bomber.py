# import detonate as det
def detonate(s,bomb_place,powers):
    for bomb_x,bomb_y in bomb_place:
        s[bomb_x][bomb_y]=' '
        curr=0
        range_power=[(0,-1),(1,0),(0,1),(-1,0)]
        if '1' in powers:
            powers.remove('1')
            range_power.extend([(0,-2),(2,0),(0,2),(-2,0)])
        if '2' in powers:
            powers.remove('2')
            for VAL in range(n):
                i,j=VAL,VAL
                range_power.extend([(-i,j),(i,-j),(i,j),(-i,-j)])
    #     print(s[bomb_x][bomb_y])
        for i,j in range_power:
            if bomb_x+i<=0 or bomb_y+j<=0 or bomb_x+i>=n-2 or bomb_y+j>=n-2:
                continue
            if(s[bomb_x+i][bomb_y+j]=='B' or s[bomb_x+i][bomb_y+j]=='V'):
                s[bomb_x+i][bomb_y+j]=" "
            elif(s[bomb_x+i][bomb_y+j]=='P'):
                curr=1
    
    return curr
    

n=int(input('Map Size: '))
s=[ [' ']* n for _ in range(n)]
char=65
for i in range(n):
    if i!=0:
        s[0][i]=chr(char)
        s[i][0]=chr(char)
        s[1][i]='*'
        s[i][1]='*'
        s[i][n-1]='*'
        s[n-1][i]='*'
        char+=1
for i in range(n):
    for j in range(n):
        if  i%2!=0 and j%2!=0:
            s[i][j]='*'
for row in s:
    for col in row:
        print(col,end=' ')
    print()

    
player=input('Player position: ')
player_x=ord(player[0].upper())-64
player_y=ord(player[1].upper())-64
# print(player_x)
s[player_x][player_y]='P'
key=input('Key position: ')
key_x=ord(key[0].upper())-64
key_y=ord(key[1].upper())-64
# print(key_x)
while s[key_x][key_y]!=' ':
    print("Element already present type another element")
    key=input('Key position: ')
    key_x=ord(key[0].upper())-64
    key_y=ord(key[1].upper())-64
    
s[key_x][key_y]='k'
villan=int(input('Villain count: '))
for _ in range(villan):
    villan=input('Villan ')
    villan_x=ord(villan[0].upper())-64
    villan_y=ord(villan[1].upper())-64
    while s[villan_x][villan_y]!=' ':
        print("Element already present type another element")
        villan=input('Villan ')
        villan_x=ord(villan[0].upper())-64
        villan_y=ord(villan[1].upper())-64
    s[villan_x][villan_y]='V'
brick_cnt=int(input('Brick count: '))
for _ in range(brick_cnt):
    brick=input('Brick ')
    brick_x=ord(brick[0].upper())-64
    brick_y=ord(brick[1].upper())-64
    while s[brick_x][brick_y]!=' ':
        print("Element already present type another element")
        brick=input('Brick ')
        brick_x=ord(brick[0].upper())-64
        brick_y=ord(brick[1].upper())-64
    s[brick_x][brick_y]='B'

rCount=int(input('Bomb Range + 1 Power '))
for _ in range(rCount):
    range1=input('range ')
    range_x=ord(range1[0].upper())-64
    range_y=ord(range1[1].upper())-64
    while s[range_x][range_y]!=' ':
        print("Element already present type another element")
        range1=input('range ')
        range_x=ord(range1[0].upper())-64
        range_y=ord(range1[1].upper())-64
    s[range_x][range_y]='1'
    
dCount=int(input('Diagonal Power '))
for _ in range(dCount):
    diag=input('Power 2 Location ')
    diag_x=ord(diag[0].upper())-64
    diag_y=ord(diag[1].upper())-64
    while s[diag_x][diag_y]!=' ':
        print("Element already present type another element")
        diag=input('Power 2 Location')
        diag_x=ord(diag[0].upper())-64
        diag_y=ord(diag[1].upper())-64
    s[diag_x][diag_y]='2'
bombCount=int(input('Bomb Count + 1 Power '))
for _ in range(bombCount):
    bombs=input('Power 2 Location ')
    bombs_x=ord(bombs[0].upper())-64
    bombs_y=ord(bombs[1].upper())-64
    while s[bombs_x][bombs_y]!=' ':
        print("Element already present type another element")
        bombs=input('Power 2 Location')
        bombs_x=ord(bombs[0].upper())-64
        bombs_y=ord(bombs[1].upper())-64
    s[bombs_x][bombs_y]='3'

    
    
for row in s:
    for col in row:
        print(col,end=' ')
    print()    
# W - Move up
# S - Move down
# A - Move left
# D - Move right
# Q - Move diagonally up left
# Z - Move diagonally down left
# E - Move diagonally up right
# C - Move diagonally down right
POWER=['1','2','3']
powers=[]
m=[]
FLAG=0
bomb_place=[]
while True:
    move=input('W - Move up\n\
S - Move down\n\
A - Move left\n\
D - Move right\n\
Q - Move diagonally up left\n\
Z - Move diagonally down left\n\
E - Move diagonally up right\n\
C - Move diagonally down right\n\
X - Plant bomb  ')[0]

    m.append(str(player_x)+'_'+str(player_y))
    
    if move=='W':
        if s[player_x-1][player_y] in POWER:
            powers.append(s[player_x-1][player_y])
            s[player_x-1][player_y]=' '
        if s[player_x-1][player_y] != ' ' :
            if s[player_x-1][player_y] == 'V':
                print('Died')
                break
            else:
                print("You can't go there is an Brick or Wall")
        else:
            s[player_x][player_y] = ' '
            s[player_x-1][player_y] ='P'
            player_x-=1
    elif move=='S':
        if s[player_x+1][player_y] in POWER:
            powers.append(s[player_x+1][player_y])
            s[player_x+1][player_y]=' '
            
        if s[player_x+1][player_y] != ' ':
            if s[player_x+1][player_y] == 'V':
                print('Died')
                break
            else:
                print("You can't go there is an Brick or Wall")
        else:
            s[player_x][player_y] = ' '
            s[player_x+1][player_y] ='P'
            player_x+=1
    elif move=='A':
        if s[player_x][player_y-1] in POWER:
            powers.append(s[player_x][player_y-1])
            s[player_x][player_y-1]=' '
            
        if s[player_x][player_y-1] != ' ':
            if s[player_x+1][player_y] == 'V':
                print('Died')
                break
            else:
                print("You can't go there is an Brick or Wall")
        else:
            s[player_x][player_y] = ' '
            s[player_x][player_y-1] ='P'
            player_y-=1
    elif move=='D':
        if s[player_x][player_y+1] in POWER:
            powers.append(s[player_x][player_y+1])
            s[player_x][player_y+1]=' '
            
        if s[player_x][player_y+1] != ' ':
            if s[player_x][player_y+1] == 'V':
                print('Died')
                break
            else:
                print("You can't go ,there is an Brick or Wall")
        else:
            s[player_x][player_y] = ' '
            s[player_x][player_y+1] ='P'
            player_y+=1

    elif move=='Q':
        if s[player_x-1][player_y-1] in POWER:
            powers.append(s[player_x-1][player_y-1])
            s[player_x-1][player_y-1]=' '
            
        if s[player_x-1][player_y-1] != ' ':
            if s[player_x-1][player_y-1] == 'V':
                print('Died')
                break
            else:
                print("You can't go ,there is an Brick or Wall")
        else:
            s[player_x][player_y] = ' '
            s[player_x-1][player_y-1] ='P'
            player_y-=1
            player_x-=1
    elif move=='C':
        if s[player_x+1][player_y+1] in POWER:
            powers.append(s[player_x+1][player_y+1])
            s[player_x+1][player_y+1]=' '
            
        if s[player_x+1][player_y+1] != ' ':
            if s[player_x+1][player_y+1] == 'V':
                print('Died')
                break
            else:
                print("You can't go ,there is an Brick or Wall")
        else:
            s[player_x][player_y] = ' '
            s[player_x+1][player_y+1] ='P'
            player_y+=1
            player_x+=1
    elif move=='Z':
        if s[player_x+1][player_y-1] in POWER:
            powers.append(s[player_x+1][player_y-1])
            s[player_x+1][player_y-1]=' '
            
        if s[player_x+1][player_y-1] != ' ':
            if s[player_x+1][player_y-1] == 'V':
                print('Died')
                break
            else:
                print("You can't go ,there is an Brick or Wall")
        else:
            s[player_x][player_y] = ' '
            s[player_x+1][player_y-1] ='P'
            player_y-=1
            player_x+=1
            
    elif move=='E':
        if s[player_x-1][player_y+1] in POWER:
            powers.append(s[player_x-1][player_y+1])
            s[player_x-1][player_y+1]=' '
            
        if s[player_x-1][player_y+1] != ' ':
            if s[player_x-1][player_y+1] == 'V':
                print('Died')
                break
            else:
                print("You can't go ,there is an Brick or Wall")
        else:
            s[player_x][player_y] = ' '
            s[player_x-1][player_y+1] ='P'
            player_y+=1
            player_x-=1
    elif move=='0':
            break
    elif move=='X':
        print('1 Plant\n\
2 Detonate ')
        value=int(input())
        
        if value==1:
            if FLAG == 1 and '3' not in powers :
                print("You Can't Plant a Bomb Already one present")
            else:
                if FLAG == 1 and '3' in powers: 
                    powers.remove('3')
                s[player_x][player_y]='X'
                bomb_place.append((player_x,player_y))
                m[-2].split('_')
                player_x=int(m[-2].split('_')[0])
                player_y=int(m[-2].split('_')[1])
                s[player_x][player_y]='P'
                FLAG=1      
        else:
                if bomb_place==[]:
                    print('No bomb Planted')
                curr=detonate(s,bomb_place,powers)
                if(curr==1):
                    print('Died')
                    break
        
    for row in s:
        for col in row:
            print(col,end=' ')
        print()
        
        
        

    
# mSize = 12;
# player = "CB";
# key = "FD";
# vCount = 3;
# villain[0]="BI";
# villain[1]="DF";
# villain[2]="BE";
# bCount = 6;  
# brick[0]="DD";
# brick[1]="ED";
# brick[2]="FB";
# brick[3]="FF";
# brick[4]="GB";
# brick[5]="HD";    
# rCount = 2; //Bomb Range + 1 Power
# range[0]="BD"; //Power 1 Location
# range[1]="EB"; //Power 1 Location
# dCount = 2;  //Diagonal Power
# diag[0]="CD"; //Power 2 Location
# diag[1]="CF"; //Power 2 Location
# bombCount = 2; //Bomb Count + 1 Power
# bombs[0]="DC"; //Power 3 Location
# bombs[1]="DE"; //Power 3 Location
#  Move to EB get Power 1, Move to DC get Power 3, Move to CD get Power 2, Move to
# BD get Power1, Move to DE get Power 3. Place a bomb one at DE and another at EB.
# Then move to BB to detonate the bombs.
# -> Destroyed  places DD,ED,DF,GB,FB,BE

