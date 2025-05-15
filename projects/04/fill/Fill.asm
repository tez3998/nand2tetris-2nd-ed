// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.

    // num_rams = 32 // 変更対象のRAMの総数
    @32 // 本当はディスプレイの全ての色を変更しなければならないが、時間がかかるため1行分のみ変更
    D=A
    @num_rams
    M=D

(LOOP)
    // if (KBD == 0) goto WHITHEN, else goto BLAKEN
    @KBD
    D=M
    @WHITEN
    D;JEQ
    @BLAKEN
    0;JMP

(WHITEN)
    // i = 0
    @i
    M=0

(WHITEN_LOOP)
    // if (num_rams == i) goto LOOP
    @num_rams
    D=M
    @i
    D=D-M
    @LOOP
    D;JEQ

    // *(SCREEN + i) = 0
    @i
    D=M
    @SCREEN
    A=D+A
    M=0

    // i = i + 1
    @i
    M=M+1

    @WHITEN_LOOP
    0;JMP

(BLAKEN)
    // i = 0
    @i
    M=0

(BLAKEN_LOOP)
    // if (num_rams == i) goto LOOP
    @num_rams
    D=M
    @i
    D=D-M
    @LOOP
    D;JEQ

    // *(SCREEN + i) = 0
    @i
    D=M
    @SCREEN
    A=D+A
    M=-1

    // i = i + 1
    @i
    M=M+1

    @BLAKEN_LOOP
    0;JMP