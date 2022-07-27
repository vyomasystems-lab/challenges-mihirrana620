# challenges-mihirrana620

## MUX Design Verification (level1_design1)

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

 ![ alt text](https://github.com/vyomasystems-lab/challenges-mihirrana620/blob/master/images/image1.png)

 ### Verification Environment (MUX)

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

### Capturing the BUG (MUX)

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

![ alt text](https://github.com/vyomasystems-lab/challenges-mihirrana620/blob/master/images/image2.png)

In BUG-2 , We can observe that there is no sel = 5'b11110 (30) is defined in Cases. For selecting inp30 we need to define a case for sel = 5'b11110 (30). Hence when we verify the MUX at sel 30 (5'b11110) we get the below error.

![ alt text](https://github.com/vyomasystems-lab/challenges-mihirrana620/blob/master/images/image3.png)

In BUG-3 , We know that when the sel line is of 5 bits there should be 32 inputs in the MUX. Hence we need to add one more input i.e. inp31 in input port list. As well as we also need to define a case for sel =  5'b11110 (31) to select inp31.


Apart from the above bugs , All other test cases are passed i.e. by changing sel we are able to correctly fetch the input and the output of DUT matches the input value. Below shown are the Test cases which are passed.

![ alt text](https://github.com/vyomasystems-lab/challenges-mihirrana620/blob/master/images/image4.png)

### Resolving the BUG (MUX)

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

![ alt text](https://github.com/vyomasystems-lab/challenges-mihirrana620/blob/master/images/image5.png)

## Sequence Detector Design Verification (level1_design2)


### Verification Environment (Sequence Detector)

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Sequence Detector) which takes in input bit and detect whether 1011 sequnece is seen or not. 
Below shown is example how 1 bit input is drived.

```
 """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 1
    dut.reset.value = 0
    await RisingEdge(dut.clk)
    dut._log.info(f' inp_bit = {(dut.inp_bit.value)} \n current state - {(dut.current_state.value)} \n next state - {(dut.next_state.value)} seq_seen = {(dut.seq_seen.value)}')
```

### Capturing the BUG (Sequence Detector)

```
module seq_detect_1011(seq_seen, inp_bit, reset, clk);

  output seq_seen;
  input inp_bit;
  input reset;
  input clk;

  parameter IDLE = 0,
            SEQ_1 = 1, 
            SEQ_10 = 2,
            SEQ_101 = 3,
            SEQ_1011 = 4;           //  ##### BUG1  ########

  reg [2:0] current_state, next_state;

  // if the current state of the FSM has the sequence 1011, then the output is
  // high
  assign seq_seen = current_state == SEQ_1011 ? 1 : 0;

  // state transition
  always @(posedge clk)
  begin
    if(reset)
    begin
      current_state <= IDLE;
    end
    else
    begin
      current_state <= next_state;
    end
  end

  // state transition based on the input and current state
  always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;                    // #### BUG - 2  ###### 
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;                    //  #### BUG - 3 ####            
        else
          next_state = IDLE;                      
      end
      SEQ_1011:                            
      begin                                             // ### REDUNDANT STATE #####
        next_state = IDLE;
      end
    endcase
  end
endmodule

```

BUG-1 : As we know 1011 mealy overllapping sequence requires only 4 states the last state SEQ_1011 is redundant.

BUG-2 : Here next_state should be equal SEQ_1 when input bit is equal to 1 in order to detect overlapping 1011 sequence.

BUG-3 : Here next_state should be equal SEQ_1 when input bit is equal to 1 and next_state should be equal SEQ_10 when input bit is equal to 0 in order to detect overlapping 1011 sequence.

Below result show that the test case fails beacuse of above bugs and is unable to detect 1011 sequence

![ alt text](https://github.com/vyomasystems-lab/challenges-mihirrana620/blob/master/images/image6.png)

###  Resolving the BUG (Sequence Detector)

```
module Bug_free_seq_detect_1011(seq_seen, inp_bit, reset, clk);

  output seq_seen;
  input inp_bit;
  input reset;
  input clk;

  parameter IDLE = 0,
            SEQ_1 = 1, 
            SEQ_10 = 2,
            SEQ_101 = 3;
            

  reg [2:0] current_state, next_state;

  // if the current state of the FSM has the sequence 1011, then the output is
  // high
  assign seq_seen = current_state == SEQ_101 ? 1 : 0;

  // state transition
  always @(posedge clk)
  begin
    if(reset)
    begin
      current_state <= IDLE;
    end
    else
    begin
      current_state <= next_state;
    end
  end

  // state transition based on the input and current state
  always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end
    endcase
  end
endmodule

```

All the bugs mentioned in the previous section are resolved and now only 4 states are used to detect 1011 overllapping Sequence.
As it overllaping sequnece next_state values are assigned in such way that allows overlap so the final bits of one sequence can be the start of another sequence. 

Below shows the results when the BUG free Sequence Detector is verified. It can be observed that it detects the overlaaping sequence.

![ alt text](https://github.com/vyomasystems-lab/challenges-mihirrana620/blob/master/images/image7.png)

## Bitmanipulation Coprocessor Design Verification (level2_design)


## Synchronous FIFO Design Verification (level3_design)

### Verification Environment (Synchronous FIFO)

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Synchronous FIFO) which takes in input bit and fifo memory is filled. When the fifo is full buf_full becomes 1 and when the fifo is empty buf_empty becomes 1.

Below code shows how the input_bits are written in fifo memory
```
@cocotb.test()
async def fifo_write_randomised_test(dut):
    """ Fifo write test """
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock


    dut.rst.value = 1
    await FallingEdge(dut.clk)  
    for i in range(8):

        dut.rst.value = 0
        dut.wr_en.value = 1
        dut.rd_en.value = 0
        dut.buf_in.value = random.randint(0, 15)
        await FallingEdge(dut.clk)  
        dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
```
Below code shows how the input_bits are read from fifo memory
```
@cocotb.test()
async def fifo_read_randomised_test(dut):
    """ Fifo read """
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock  
    for i in range(8):

        dut.rst.value = 0
        dut.wr_en.value = 0
        dut.rd_en.value = 1
       
        await FallingEdge(dut.clk)  
        dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')

```
### Design Synchronous FIFO (BUG - Free)

```
`timescale 1ns / 1ps

`define BUF_WIDTH 3    
`define BUF_SIZE ( 1<<`BUF_WIDTH )

module Synchronous_FIFO( clk, rst, buf_in, buf_out, wr_en, rd_en, buf_empty, buf_full, fifo_counter );

input                 rst, clk, wr_en, rd_en;   

input [7:0]           buf_in;                   

output[7:0]           buf_out;                  

output                buf_empty, buf_full;      

output[`BUF_WIDTH :0] fifo_counter;             
   

reg[7:0]              buf_out;
reg                   buf_empty, buf_full;
reg[`BUF_WIDTH :0]    fifo_counter;
reg[`BUF_WIDTH -1:0]  rd_ptr, wr_ptr;           
reg[7:0]              buf_mem[`BUF_SIZE -1 : 0];  

always @(fifo_counter)
begin
   buf_empty = (fifo_counter==0);   
   buf_full = (fifo_counter== `BUF_SIZE);  

end

always @(posedge clk or posedge rst)
begin
   if( rst )
       fifo_counter <= 0;	

   else if( (!buf_full && wr_en) && ( !buf_empty && rd_en ) )  
       fifo_counter <= fifo_counter;			

   else if( !buf_full && wr_en )			
       fifo_counter <= fifo_counter + 1;

   else if( !buf_empty && rd_en )		
       fifo_counter <= fifo_counter - 1;

   else
      fifo_counter <= fifo_counter;			
end

always @( posedge clk or posedge rst)
begin
   if( rst )
      buf_out <= 0;		
   else
   begin
      if( rd_en && !buf_empty )
         buf_out <= buf_mem[rd_ptr];

      else
         buf_out <= buf_out;		

   end
end

always @(posedge clk)
begin
   if( wr_en && !buf_full )
      buf_mem[ wr_ptr ] <= buf_in;		

   else
      buf_mem[ wr_ptr ] <= buf_mem[ wr_ptr ];
end

always@(posedge clk or posedge rst)
begin
   if( rst )
   begin
      wr_ptr <= 0;
      rd_ptr <= 0;		
   end
   else
   begin
      if( !buf_full && wr_en )    
			wr_ptr <= wr_ptr + 1;		
      else  
			wr_ptr <= wr_ptr;

      if( !buf_empty && rd_en )   
			rd_ptr <= rd_ptr + 1;		
      else 
			rd_ptr <= rd_ptr;
   end

end
endmodule
```

### Verification Results of Synchronous FIFO (BUG - Free)

Firstly Fifo memory is filled with randomized inputs and with each input fifo_counter increases by 1. When the fifo is full buf_full becomes 1 and when the fifo was empty buf_empty was 1. Below are the results when write operation in fifo is performed.


![ alt text](https://github.com/vyomasystems-lab/challenges-mihirrana620/blob/master/images/image8.png)


After the fifo memory is filled the inputs are read. As the fifo follow First in First out principle so the value which was written first in the fifo memory is read first. Below are the results when write operation in fifo is performed

![ alt text](https://github.com/vyomasystems-lab/challenges-mihirrana620/blob/master/images/image9.png)

Both read and write operation test cases are passed

![ alt text](https://github.com/vyomasystems-lab/challenges-mihirrana620/blob/master/images/image10.png)


### Inserting a bug in Synchronous FIFO

```
`timescale 1ns / 1ps

`define BUF_WIDTH 3    
`define BUF_SIZE ( 1<<`BUF_WIDTH )

module Buggy_Synchronous_FIFO( clk, rst, buf_in, buf_out, wr_en, rd_en, buf_empty, buf_full, fifo_counter );

input                 rst, clk, wr_en, rd_en;   

input [7:0]           buf_in;                   

output[7:0]           buf_out;                  

output                buf_empty, buf_full;      

output[`BUF_WIDTH :0] fifo_counter;             
   

reg[7:0]              buf_out;
reg                   buf_empty, buf_full;
reg[`BUF_WIDTH :0]    fifo_counter;
reg[`BUF_WIDTH -1:0]  rd_ptr, wr_ptr;           
reg[7:0]              buf_mem[`BUF_SIZE -1 : 0];  

always @(fifo_counter)
begin
   buf_empty = (fifo_counter==0);   
   buf_full = (fifo_counter == `BUF_SIZE);  

end

always @(posedge clk or posedge rst)
begin
   if( rst )
       fifo_counter <= 0;	

   else if( (!buf_full && wr_en) && ( !buf_empty && rd_en ) )  
       fifo_counter <= fifo_counter;			

   else if( !buf_full && wr_en )			
       fifo_counter <= fifo_counter + 1;

   else if( !buf_empty && rd_en )		
       fifo_counter <= fifo_counter - 1;

   else
       fifo_counter <= fifo_counter;			
end

always @( posedge clk or posedge rst)
begin
   if( rst )
      buf_out <= 0;		
   else
   begin
      if( rd_en && !buf_empty )
         buf_out <= buf_mem[rd_ptr];

      else
         buf_out <= buf_out;		

   end
end

always @(posedge clk)
begin
   if( wr_en && !buf_full )
      buf_mem[ wr_ptr ] <= buf_in;		

   else
      buf_mem[ wr_ptr ] <= buf_mem[ wr_ptr ];
end

always@(posedge clk or posedge rst)
begin
   if( rst )
   begin
      wr_ptr <= 0;
      rd_ptr <= 0;		
   end
   else
   begin
      if( !buf_full && wr_en )    
			wr_ptr <= wr_ptr + 1;		
      else  
			wr_ptr <= wr_ptr;

      if( !buf_empty && rd_en )   
			rd_ptr <= rd_ptr - 1;		            // #### BUG IS INSERTED HERE #####
      else 
			rd_ptr <= rd_ptr;
   end

end
endmodule

```
Here in the above design bug is inserted by changing "+" to "-" i.e. we are decreasing the rd_ptr instead by 1 instead of increasing it by 1. Because of this we get error while verifying Synchronous fifo for read operation. Below shown are the results when we tried to verify Buggy Synchronous FIFO. Firstly we have filled the fifo memory performing the write operation and then while performing read operation we got error.

![ alt text](https://github.com/vyomasystems-lab/challenges-mihirrana620/blob/master/images/image11.png)





