# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/Synchronous_FIFO.v              # provide your design path

TOPLEVEL := Synchronous_FIFO          # design file
MODULE   := test_Synchronous_FIFO   # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
