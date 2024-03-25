
inlay_level=4;

chip_rows=8;
chip_width=4.5;
chip_rowpitch=7;

chip_cols=8;
chip_length=4.5;
chip_colpitch=7;

inlay_length=chip_colpitch*(chip_cols-1)+chip_length;
inlay_width=chip_rowpitch*(chip_rows-1)+chip_width;

lidgap_level=6;

lidgap_width=inlay_width+18;
lidgap_length=inlay_length+13.8;
lidgap_length1=inlay_length+8;


lid_length=inlay_length+13;
lid_width=inlay_width+18;
lid_length1=inlay_length+7;


length=inlay_length+18;
width=inlay_width+12+9;
height=10;


module case()
{
    color("lightblue")
    difference() // case
    {
        translate([-length/2,0,0]) cube([length, width, height]); // aussen
        translate([-lidgap_length/2,-0.01,lidgap_level]) // fuehrung
            cube([lidgap_length, lidgap_width, 2.5]); 
        translate([-lidgap_length1/2,-0.01,lidgap_level]) // fuehrung1
            cube([lidgap_length1, lidgap_width, 10]); 
        
        translate([-inlay_length/2,12,inlay_level]) // inlay
            cube([inlay_length, inlay_width, 10]); 

    for(row=[0:chip_rows-1]){
        translate([-inlay_length/2-4,chip_width+row*chip_rowpitch+3+chip_width/2,inlay_level+1])
        linear_extrude(height=1) 
        scale(0.4)text(str(chip_rows-row));
    }
    
    for(col=[0:chip_cols-1]){
        translate([
        -inlay_length/2+3+col*chip_colpitch,
        13+inlay_width, inlay_level+1
        ])
        linear_extrude(height=1) 
        scale(0.4)text(chr(col+65));
    }
            
            
            
    }
    // spaltentrenner

    for(col =[0:chip_cols-2]) {
        translate([-inlay_length/2+chip_length+col*chip_colpitch,12.5,inlay_level]) 
            cube([chip_colpitch-chip_length,inlay_width-1,lidgap_level-inlay_level]);
    }

    // zeilentrenner
        for(row = [0:chip_rows-2]) {
            translate([
            -inlay_length/2+0.5,
            12+0.5+chip_width+chip_rowpitch*row,
            inlay_level]) 
                    cube([chip_colpitch*(chip_rows-1)+chip_width-1,chip_rowpitch-chip_width-1,lidgap_level-inlay_level]);
        }

}

module  lid()
{
   color("blue"){
    translate([-lid_length/2,0,0])
            cube([lid_length, lid_width, 2]); 
    difference(){
            translate([-lid_length1/2,0,0])
                cube([lid_length1, lid_width, 4]); 
            hull() {
                translate([-10,15,0])    
                    cylinder(d1=6,d2=10,h=5);
                translate([10,15,0])    
                    cylinder(d1=6,d2=10,h=5);
                }
            }
     }
    translate([0,40,4])  
    color("white")
    linear_extrude(height=1)
        scale(0.3)
        import("Photeon_semicontuctors_logo_4c.svg",center=true);

}

module compile()
{
    case();
    translate([0,-$t*80,6.25])
    lid();
}

//compile();

//echo(chr(65));
case();

