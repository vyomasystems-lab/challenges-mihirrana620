import os
import random
from cocotb.triggers import Timer
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_Buggy_Synchronous_fifo(dut):

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock


    dut.rst.value = 1
    await FallingEdge(dut.clk)  

    dut.rst.value = 0
    dut.wr_en.value = 1
    dut.rd_en.value = 0
    dut.buf_in.value = 8
    await FallingEdge(dut.clk)  
    dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
   
    dut.rst.value = 0
    dut.wr_en.value = 1
    dut.rd_en.value = 0
    dut.buf_in.value = 7
    await FallingEdge(dut.clk)  
    dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
    
    dut.rst.value = 0
    dut.wr_en.value = 1
    dut.rd_en.value = 0
    dut.buf_in.value = 9
    await FallingEdge(dut.clk)  
    dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
    
    dut.rst.value = 0
    dut.wr_en.value = 1
    dut.rd_en.value = 0
    dut.buf_in.value = 10
    await FallingEdge(dut.clk)  
    dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
    
    dut.rst.value = 0
    dut.wr_en.value = 1
    dut.rd_en.value = 0
    dut.buf_in.value = 11
    await FallingEdge(dut.clk)  
    dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
    
    dut.rst.value = 0
    dut.wr_en.value = 1
    dut.rd_en.value = 0
    dut.buf_in.value = 12
    await FallingEdge(dut.clk)  
    dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
    
    dut.rst.value = 0
    dut.wr_en.value = 1
    dut.rd_en.value = 0
    dut.buf_in.value = 13
    await FallingEdge(dut.clk)  
    dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
    
    dut.rst.value = 0
    dut.wr_en.value = 1
    dut.rd_en.value = 0
    dut.buf_in.value = 14
    await FallingEdge(dut.clk)  
    dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
    
    dut.rst.value = 0
    dut.wr_en.value = 0
    dut.rd_en.value = 1
    await FallingEdge(dut.clk)  
    dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
    assert dut.buf_out.value == dut.buf_mem[0].value, f" result is incorrect:   buf_out - {dut.buf_out.value} != buf_mem - {dut.buf_mem[0].value}   Test Failed !!!"
    
    dut.rst.value = 0
    dut.wr_en.value = 0
    dut.rd_en.value = 1
    await FallingEdge(dut.clk)  
    dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
    assert dut.buf_out.value == dut.buf_mem[1].value, f" result is incorrect:   buf_out - {dut.buf_out.value} != buf_mem[1] - {dut.buf_mem[1].value}   Test Failed !!!"
    
    