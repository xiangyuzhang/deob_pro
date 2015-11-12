module	c17 (N1,N2,N3,N4,N5,N6,N7,N8,N9,N12,N13,N14);
input N1,N2,N3,N4,N5;
output N6,N7;
wire N9,N12,N13,N14;
nand2 gate1( .a(N1), .b(N3), .O(N14) );
nand2 gate2( .a(N3), .b(N4), .O(N9) );
nand2 gate3( .a(N2), .b(N9), .O(N13) );
nand2 gate4( .a(N5), .b(N9), .O(N12) );
nand2 gate5( .a(N14), .b(N13), .O(N6) );
nand2 gate6( .a(N13), .b(N12), .O(N7) );
endmodule