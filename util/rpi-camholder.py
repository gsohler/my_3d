from openscad import *

fn=20
d=10 # durchmesser
h=15 # hoehe
l=50 # lange ab mitte

holder=cube([d/2+7+l,d+5,h]) + [-d/2-7,-d/2-2.5,0]
holder -= cylinder(d=d,h=h+2).down(1)
holder |=cube([10,15,30]) + [l-10,-7.5,0]
holder -=cube([12,8,30]) + [l-11,-3.5,h]

holder -= cylinder(d=3,h=d+10).rotx(-90) ^[[-d/2-3,d/2+3,l-5],-d/2-5,h/2]

holder -= cylinder(d=4,h=d+10).rotx(90) ^[l-5,d/2+5,25]

holder_h = holder & (cube([100,100,100]) + [-50,0.5,0])

holder1 = holder_h.mirror([0,1,0])
holder2 = holder_h | cube([10,21,3]).translate([40,0.5,h-3])
holder2 -= cylinder(d=4,h=10).translate([45,17,10])

holder3=cube([50,10,2]).translate([-0,-5,0])
holder3 |= cube([10,10,5]).translate([40,-5,0])
holder3 -= cube([5.5,5.5,6.5]).translate([42.25,-5+2.25,-1])
holder3 |= cylinder(d=10,h=8).down(6)
holder3 -=  cylinder(d=4,h=10).down(7)


parts=[]
parts.append(holder2)
parts.append(holder3.rotz(90).translate([45,17,21]))
parts.append(holder1)
parts[0].show()



compile=union(parts) 
compile.show()
export({"part1": holder1, "part2": holder2, "part3": holder3}, "rpi-camhodler.3mf")
