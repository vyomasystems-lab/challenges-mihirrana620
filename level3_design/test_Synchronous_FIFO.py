import os
import random
from cocotb.triggers import Timer
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

# @cocotb.test()
# async def test_Synchronous_fifo(dut):

#     clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
#     cocotb.start_soon(clock.start())        # Start the clock


    # dut.rst.value = 1
    # await FallingEdge(dut.clk)  

    # dut.rst.value = 0
    # dut.wr_en.value = 1
    # dut.rd_en.value = 0
    # dut.buf_in.value = 8
    # await FallingEdge(dut.clk)  
    # dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
   
    # dut.rst.value = 0
    # dut.wr_en.value = 1
    # dut.rd_en.value = 0
    # dut.buf_in.value = 9
    # await FallingEdge(dut.clk)   
    # dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
   
    # dut.rst.value = 0
    # dut.wr_en.value = 1
    # dut.rd_en.value = 0
    # dut.buf_in.value = 10
    # await FallingEdge(dut.clk)  
    # dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
   
    # dut.rst.value = 0
    # dut.wr_en.value = 1
    # dut.rd_en.value = 0
    # dut.buf_in.value = 11
    # await FallingEdge(dut.clk)  
    # dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
    
    # dut.rst.value = 0
    # dut.wr_en.value = 1
    # dut.rd_en.value = 0
    # dut.buf_in.value = 12
    # await FallingEdge(dut.clk)  
    # dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
   
    # dut.rst.value = 0
    # dut.wr_en.value = 1
    # dut.rd_en.value = 0
    # dut.buf_in.value = 13
    # await FallingEdge(dut.clk)  
    # dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
   
    # dut.rst.value = 0
    # dut.wr_en.value = 1
    # dut.rd_en.value = 0
    # dut.buf_in.value = 14
    # await FallingEdge(dut.clk)  
    # dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
   
    # dut.rst.value = 0
    # dut.wr_en.value = 1
    # dut.rd_en.value = 0
    # dut.buf_in.value = 15
    # await FallingEdge(dut.clk)  
    # dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
   
    # dut.rst.value = 0
    # dut.wr_en.value = 1
    # dut.rd_en.value = 0
    # dut.buf_in.value = 16
    # await FallingEdge(dut.clk)  
    # dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
   
     
    # dut.rst.value = 0
    
    # dut.rd_en.value = 1
    # dut.wr_en.value = 0
   
    # await FallingEdge(dut.clk)  
    # dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
    
    # dut.rd_en.value = 1
    # dut.wr_en.value = 0
   
    # await FallingEdge(dut.clk)  
    # dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')
   
   
@cocotb.test()
async def fifo_write_randomised_test(dut):
    """Test for random numbers """
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

@cocotb.test()
async def fifo_read_randomised_test(dut):
    """Test for random numbers """
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock  
    for i in range(8):

        dut.rst.value = 0
        dut.wr_en.value = 0
        dut.rd_en.value = 1
       
        await FallingEdge(dut.clk)  
        dut._log.info(f' buf_out - {(dut.buf_out.value)} \n buf_empty - {(dut.buf_empty.value)} \n buf_full = {(dut.buf_full.value)} \n fifo_counter = {(dut.fifo_counter.value)} \n buf_mem - {(dut.buf_mem.value)} ')


                           
                                