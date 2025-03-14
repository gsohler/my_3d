from openscad import *

fn=20
d=10 # durchmesser
h=15 # hoehe
l=50 # lange ab mitte

holder=cube([d/2+7+l,d+5,h]) + [-d/2-7,-d/2-2.5,0]
holder -= cylinder(d=d,h=h+2).down(1)
holder |=cube([10,7,30]) + [l-10,-3.5,0]
holder -= cylinder(d=4,h=d+10).rotx(-90) ^[[-d/2-3,d/2+3,l-5],-d/2-5,h/2]

holder -= cylinder(d=4,h=d+7).rotx(90) ^[l-5,d/2+1,25]

holder_h = holder & (cube([100,100,100]) + [-50,0.5,0])

holder_h.show()
