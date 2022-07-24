# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/Bug_free_seq_detect_1011.v

TOPLEVEL := Bug_free_seq_detect_1011         # design
MODULE   := test_Bug_free_seq_detect_1011     # test

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
