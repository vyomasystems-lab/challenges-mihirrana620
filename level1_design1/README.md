# Table of contents

- [MUX Design Verification (level1_design1)](#mux-design-verification-level1_design1)
  - [Verification Environment (MUX)](#verification-environment-mux)
  - [Capturing the BUG (MUX)](#capturing-the-bug-mux)
  - [Resolving the BUG (MUX)](#resolving-the-bug-mux)

# MUX Design Verification (level1_design1)

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![image1](https://user-images.githubusercontent.com/84765232/182143795-4efe27ed-2493-41f9-b98d-7b4d0d00dfbe.png)


 ## Verification Environment (MUX)

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (MUX 32 X 1) which takes in 32 2-bit inputs mentioned below and gives 2-bit output *out*. The *out* is determined by input signal *sel*. 

```
    inp0  = 0 
    inp1  = 1
    inp2  = 2
    inp3  = 3
    sel = 0

    dut.sel.value = sel
    dut.inp0.value = inp0
    dut.inp1.value = inp1
    dut.inp2.value = inp2
    dut.inp3.value = inp3
    dut.inp4.value = inp4
```
Above are example of few input ports who are assigned values. Total there are 32 input ports which are assigned 2 bit value and sel (select line) which is assigned 5 bit value.  

## Capturing the BUG (MUX)

```
module mux(sel,inp0, inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8, 
           inp9, inp10, inp11, inp12, inp13, inp14, inp15, inp16, inp17,
           inp18, inp19, inp20, inp21, inp22, inp23, inp24, inp25, inp26,
           inp27, inp28, inp29, inp30, out);

  input [4:0] sel;
  input [1:0] inp0, inp1, inp2, inp3, inp4, inp5, inp6,
            inp7, inp8, inp9, inp10, inp11, inp12, inp13, 
            inp14, inp15, inp16, inp17, inp18, inp19, inp20,
            inp21, inp22, inp23, inp24, inp25, inp26,
            inp27, inp28, inp29, inp30;

  output [1:0] out;
  reg [1:0] out;

  // Based on sel signal value, one of the inp0-inp30 gets assigned to the 
  // output signal
  always @(sel or inp0  or inp1 or  inp2 or inp3 or inp4 or inp5 or inp6 or
            inp7 or inp8 or inp9 or inp10 or inp11 or inp12 or inp13 or 
            inp14 or inp15 or inp16 or inp17 or inp18 or inp19 or inp20 or
            inp21 or inp22 or inp23 or inp24 or inp25 or inp26 or inp27 or 
            inp28 or inp29 or inp30 )

  begin
    case(sel)
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12;           //      ########  BUG-1 PRESENT IN THIS LINE ########
      5'b01101: out = inp13;
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;               
                                      //      ########  BUG-2 , BUG-3 PRESENT IN THIS LINE ########
      default: out = 0;
    endcase
  end

endmodule 


```

In the BUG-1 , out should be equal to inp12 when select line (sel) = 5'b01100. Here in the above code sel = 5'b01101 is repeating two times which gives error while verifying the MUX at sel = 13 (5'b01101) . Below is the error shown while verfying MUX at sel = 13 (5'b01101)

![image2](https://user-images.githubusercontent.com/84765232/182143905-072dd2df-26d4-4157-ab5f-d0cf31365719.png)


In BUG-2 , We can observe that sel = 5'b11110 (30) is not defined in Cases. For selecting inp30 we need to define a case for sel = 5'b11110 (30). Hence when we verify the MUX at sel 30 (5'b11110) we get the below error.

![image3](https://user-images.githubusercontent.com/84765232/182143935-74370537-a294-4eca-817f-a519e588d70d.png)

In BUG-3 , We know that when the sel line is of 5 bits there should be 32 inputs in the MUX. Hence we need to add one more input i.e. inp31 in input port list. As well as we also need to define a case for sel =  5'b11110 (31) to select inp31.


Apart from the above bugs , All other test cases are passed i.e. by changing sel we are able to correctly fetch the input and the output of DUT matches the input value. Below shown are the Test cases which are passed.

![image4](https://user-images.githubusercontent.com/84765232/182143961-d06439d1-1be1-469e-aaeb-25d8362463c7.png)

## Resolving the BUG (MUX)

The mux.v file is modified to Bug_free_Mux.v in which all the above mentioned bugs are resolved.
```
module Bug_free_Mux(sel,inp0, inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8, 
           inp9, inp10, inp11, inp12, inp13, inp14, inp15, inp16, inp17,
           inp18, inp19, inp20, inp21, inp22, inp23, inp24, inp25, inp26,
           inp27, inp28, inp29, inp30,inp31, out);

  input [4:0] sel;
  input [1:0] inp0, inp1, inp2, inp3, inp4, inp5, inp6,
            inp7, inp8, inp9, inp10, inp11, inp12, inp13, 
            inp14, inp15, inp16, inp17, inp18, inp19, inp20,
            inp21, inp22, inp23, inp24, inp25, inp26,
            inp27, inp28, inp29, inp30,inp31;

  output [1:0] out;
  reg [1:0] out;

  // Based on sel signal value, one of the inp0-inp30 gets assigned to the 
  // output signal
  always @(sel or inp0  or inp1 or  inp2 or inp3 or inp4 or inp5 or inp6 or
            inp7 or inp8 or inp9 or inp10 or inp11 or inp12 or inp13 or 
            inp14 or inp15 or inp16 or inp17 or inp18 or inp19 or inp20 or
            inp21 or inp22 or inp23 or inp24 or inp25 or inp26 or inp27 or 
            inp28 or inp29 or inp30 or inp31 )

  begin
    case(sel)
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01100: out = inp12;
      5'b01101: out = inp13;
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
      5'b11110: out = inp30;
      5'b11111: out = inp31;
      default: out = 0;
    endcase
  end

endmodule 
```
Bug_free_Mux.v is verified using for all the test cases. All the test cases are successfully passed. Below are the results.

![image5](https://user-images.githubusercontent.com/84765232/182144003-869f8d75-4b13-407b-8410-ea355c7ff932.png)

