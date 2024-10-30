from openscad import *
fn=50

mac=cube([20,20,36])
base=cube([15,20,3])+ [0,-10,0]
base |= cylinder(d=20,h=3)
base |= square([10,20]).left(15).linear_extrude(height=40,scale=[0.5,1])+[20,-10,0]
base |=cube([20,20,3])+ [14,-10,37]
base -= cylinder(d=4,h=10,center=True)

bracket= base 

compile = bracket 
compile.show()