// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

//// Replace this comment with your code.

    // sum = 0
    @sum
    M=0

    // i = 0
    @i
    M=0

(LOOP)
    // if (i >= R1) goto STOP
    @i
    D=M
    @R1
    D=D-M
    @STOP
    D;JGE

    // sum = sum + R0
    @R0
    D=M
    @sum
    M=D+M

    // i = i + 1
    @i
    M=M+1
    @LOOP
    0;JMP

(STOP)
    // R2 = sum
    @sum
    D=M
    @R2
    M=D

(END)
    @END
    0;JMP
