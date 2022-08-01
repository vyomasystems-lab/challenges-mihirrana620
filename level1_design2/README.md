# Sequence Detector Design Verification (level1_design2)


## Verification Environment (Sequence Detector)

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

## Capturing the BUG (Sequence Detector)

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

##  Resolving the BUG (Sequence Detector)

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


## State Diagram 

![ alt text](https://github.com/vyomasystems-lab/challenges-mihirrana620/blob/master/images/image14.png)