# Bomber Game
I have created Bomber Game upto 3 levels 

mSize = 12;
player = "CB";
key = "FD";
vCount = 3;
villain[0]="BI";
villain[1]="DF";
villain[2]="BE";
bCount = 6;  
brick[0]="DD";
brick[1]="ED";
brick[2]="FB";
brick[3]="FF";
brick[4]="GB";
brick[5]="HD";    
rCount = 2; //Bomb Range + 1 Power
range[0]="BD"; //Power 1 Location
range[1]="EB"; //Power 1 Location
dCount = 2;  //Diagonal Power
diag[0]="CD"; //Power 2 Location
diag[1]="CF"; //Power 2 Location
bombCount = 2; //Bomb Count + 1 Power
bombs[0]="DC"; //Power 3 Location
bombs[1]="DE"; //Power 3 Location
 Move to EB get Power 1, Move to DC get Power 3, Move to CD get Power 2, Move to
BD get Power1, Move to DE get Power 3. Place a bomb one at DE and another at EB.
Then move to BB to detonate the bombs.
-> Destroyed  places DD,ED,DF,GB,FB,BE
