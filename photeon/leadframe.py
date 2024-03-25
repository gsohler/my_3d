from openscad import *

lead_rows=9
lead_cols=11
lead_pitch=0.625
lead_width=0.3
lead_length=0.8

die_length=3
die_width=2.4
die_height=0.5
wire_d=0.1

pad_list ={
    "A": [[1.3,-0.1],[0.2,0.2]],
    "B": [[1.3,0.3],[0.2,0.2]],
}

bond_list = [
    ["A",25],
    ["B",26],
    ["B",27],
]

leadframe_hwidth=(lead_cols+2)*lead_pitch/2
leadframe_hheight=(lead_rows+2)*lead_pitch/2

def lead_pos(num):
    if num <= lead_rows:
        return [-leadframe_hwidth+lead_width/2,(lead_rows-2*num+1)*lead_pitch/2 ]
    elif num <= lead_rows+lead_cols:
        return [(2*(num-lead_cols)+3-lead_cols)*lead_pitch/2,-leadframe_hheight+lead_width/2 ]
    if num <= 2*lead_rows+lead_cols:
        return [leadframe_hwidth-lead_width/2,
        (2*(num-lead_cols-lead_rows)-1-lead_rows)*lead_pitch/2 ]
    elif num <= 2*lead_rows+2*lead_cols:
        return [(lead_cols - 2*(num-2*lead_cols-lead_rows)-3)*lead_pitch/2,leadframe_hheight-lead_width/2 ]
    return [0,0]

lead=square([lead_width,lead_width]).front(lead_width/2)
lead1=square([0.01,lead_width]).front(lead_width/2).right(lead_width-0.01)

leads = []
leads1 = []
centerpt=square(0.1,center=True)

for row in range(lead_rows):
    leads.append(lead.rotz(180) # right side
        .translate([leadframe_hwidth,(2*row+1-lead_rows)*lead_pitch/2]))

    leads1.append(hull(lead1.rotz(180).translate([leadframe_hwidth,(2*row+1-lead_rows)*lead_pitch/2]),centerpt))

for col in range(lead_cols):
    leads.append(lead.rotz(270) # top side
        .translate([(2*col+1-lead_cols)*lead_pitch/2,leadframe_hheight]))
    leads1.append(hull(lead1.rotz(270).translate([(2*col+1-lead_cols)*lead_pitch/2,leadframe_hheight]),centerpt))


leads1=union(leads1) - square([2*leadframe_hwidth-2*lead_length, 2*leadframe_hheight-2*lead_length], center=True)
leadframe = union(leads) | union(leads1)
leadframe = leadframe | leadframe.rotz(180)
leadframe |= square([2*leadframe_hwidth-3*lead_length, 2*leadframe_hheight-3*lead_length], center=True)
lowpt = square([lead_width/2, lead_width/2]).translate([-leadframe_hwidth+lead_width,-leadframe_hheight+lead_width]) 
leadframe |= hull(lowpt, lowpt.rotz(180))

lowpt = square([lead_width/2, lead_width/2]).translate([leadframe_hwidth-lead_width*1.5,-leadframe_hheight+lead_width]) 
leadframe |= hull(lowpt, lowpt.rotz(180))

leadframe -= square([2*leadframe_hwidth-3*lead_length-2*lead_width, 2*leadframe_hheight-3*lead_length-2*lead_width], center=True)

pads = []

for p in pad_list:
    rect=pad_list[p]
    pads.append(square(rect[1]).translate(rect[0]))
pads = union(pads).linear_extrude(0.01).up(0.5)    

die=square([die_length, die_width],center=True).linear_extrude(die_height).color("blue") | pads

bonding = []
for b in bond_list:
    padname = b[0]
    if padname in pad_list:
        die_pos=pad_list[padname]
        frame_pos=lead_pos(b[1])
        bonding.append(hull(
        sphere(d=wire_d).translate([die_pos[0][0]+die_pos[1][0]/2,die_pos[0][1]+die_pos[1][1]/2,die_height+wire_d/2]), 
        sphere(d=wire_d).translate([frame_pos[0], frame_pos[1],0.1+wire_d/2])))

assembly = leadframe.linear_extrude(0.1).color("gray")

output(assembly | die | union(bonding))