from openscad import *

t=8 # final thickness
h=80 #height
d=80 # diameter
s=3
w=12  # wings


crucible_out=cylinder(d1=d-20,d2=d,h=h)
crucible_in = cylinder(d1=d-20-2*t,d2=d-2*t,h=h).translate([0,0,t])
crucible_in &= cylinder(d=100,h=h)

crucible_in1 = cylinder(d1=d-20-2*s,d2=d-2*s,h=h).translate([0,0,s])

crucible = crucible_out - crucible_in


net=crucible_out - crucible_in1
net |= cylinder(d=12,h=t+10).down(10) # Mittelsteg
net &= cube([100,2,100]).translate([0,-1,-10]) #nur ein slice
net -= cube([20,5,20]).translate([-5,0,-11]).rotz(180/w).right(0.25) # zuspitzen
net -= cube([20,5,20]).translate([-5,-5,-11]).rotz(-180/w).right(0.25) #zuspitzen

arc=(cylinder(r=s+3,h=2,center=True)-cylinder(r=3,h=3,center=True)) & cube([10,10,2]).down(1)
net |= arc.rotate([0,-90,90]).translate([3+d/2-0.25,0,h])



compile1=cube([120,120,1]).translate([-60,-60,0])
compile1 |= crucible_in.rotx(180).up(h+1)
for i in range(w):
    compile1 -= cube([s+1,2+1,3]).translate([d/2-s-0.75,-1.5,-1]).rotz(360*i/w)
compile1 -= cylinder(d1=d-20,d2=0,h=h-6).down(1)


compile2 = net.rotx(180).up(h+1)
for i in range(w):
    compile2 |= net.rotx(180).up(h+1).rotz(360*i/w)

#output(compile1 | compile2)
output(net)

#output(crucible-cube(100))