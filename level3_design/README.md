# Table of contents

- [Synchronous FIFO Design Verification (level3_design)](#synchronous-fifo-design-verification-level3_design)
  - [Verification Environment (Synchronous FIFO)](#verification-environment-synchronous-fifo)
  - [Design Synchronous FIFO (BUG - Free)](#design-synchronous-fifo-bug---free)
  - [Verification Results of Synchronous FIFO (BUG - Free)](#verification-results-of-synchronous-fifo-bug---free)
  - [Inserting a bug in Synchronous FIFO](#inserting-a-bug-in-synchronous-fifo)
- [References](#references)

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

![image8](https://user-images.githubusercontent.com/84765232/182144854-c5526ca3-eabe-4b36-af75-65a55c92885f.png)

After the fifo memory is filled the inputs are read. As the fifo follow First in First out principle so the value which was written first in the fifo memory is read first. Below are the results when write operation in fifo is performed

![image9](https://user-images.githubusercontent.com/84765232/182145455-a6b2f20f-205f-412b-8bb8-5d94e6bc2aac.png)

Both read and write operation test cases are passed

![image10](https://user-images.githubusercontent.com/84765232/182144950-9cffc1f2-ffd4-4e4b-b87d-d9f2a199c327.png)

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

![image11](https://user-images.githubusercontent.com/84765232/182145014-80161180-8dc9-4e75-9e59-82ed40088392.png)

## References
1. https://github.com/mihirrana620/Synchronous-FIFO-NIELIT-IITM-CTB-Verification-Hackathon.git


