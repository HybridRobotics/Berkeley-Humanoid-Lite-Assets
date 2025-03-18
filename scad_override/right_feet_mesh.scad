% scale(1000) import("leg_right_feet_right_feet_mesh.stl");

//translate([57, 18, 20])
//cube([40, 130, 32], center=true);

// front toe
translate([50, 70, 18])
sphere(10);

// inner palm
translate([42, 40, 12])
sphere(10);

// outer palm
translate([70, 40, 12])
sphere(10);

// heel
translate([52, -34, 18])
sphere(16);
