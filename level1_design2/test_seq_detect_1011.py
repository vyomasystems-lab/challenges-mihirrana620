# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from cocotb.triggers import Timer
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
   
     
    # await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut.reset.value = 0
    await RisingEdge(dut.clk)
    dut._log.info(f' inp_bit = {(dut.inp_bit.value)} \n current state - {(dut.current_state.value)} \n next state - {(dut.next_state.value)} seq_seen = {(dut.seq_seen.value)}')
   
    dut.inp_bit.value = 0
    dut.reset.value = 0
    await RisingEdge(dut.clk)
    dut._log.info(f' inp_bit = {(dut.inp_bit.value)} \n current state - {(dut.current_state.value)} \n next state - {(dut.next_state.value)} seq_seen = {(dut.seq_seen.value)}')
    
    dut.inp_bit.value = 1
    dut.reset.value = 0
    await RisingEdge(dut.clk)
    dut._log.info(f' inp_bit = {(dut.inp_bit.value)} \n current state - {(dut.current_state.value)} \n next state - {(dut.next_state.value)} seq_seen = {(dut.seq_seen.value)}')
  

    
    dut.inp_bit.value = 1
    dut.reset.value = 0
    await RisingEdge(dut.clk)
    dut._log.info(f' inp_bit = {(dut.inp_bit.value)} \n  current state - {(dut.current_state.value)} \n next state - {(dut.next_state.value)} seq_seen = {(dut.seq_seen.value)}')

    ## One extra input is needed to pass the test and detect sequence. This is the bug

    # dut.inp_bit.value = 1
    # dut.reset.value = 0
    # await RisingEdge(dut.clk)
    # dut._log.info(f' inp_bit = {(dut.inp_bit.value)} \n  current state - {(dut.current_state.value)} \n next state - {(dut.next_state.value)} seq_seen = {(dut.seq_seen.value)}')
    
    assert dut.seq_seen.value == 1, f" Sequence is not seen ... Test Failed !!!"

    cocotb.log.info('#### CTB: Develop your test here! ######')
