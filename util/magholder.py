from openscad import *
fn=20
holder1=cylinder(d=10,h=5,center=True)
holder1 |= cube([50,5,1]).front(2.5).down(2.5)
holder1 |= cylinder(d=10,h=1).right(50).down(2.5)
holder1 -= cube(5.5, center=True)
holder1 -= cylinder(d=4,h=20).right(50).down(5)

holder1.show()