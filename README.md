# challenges-mihirrana620

## MUX Design Verification

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

 ![ alt text](https://github.com/vyomasystems-lab/challenges-mihirrana620/blob/master/images/image1.png)

 ## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (MUX 32 X 1) which takes in 32 2-bit inputs mentioned below and gives 2-bit output *out*. The *out* is determined by input signal *sel*. 
Below are example of few input ports who are assigned values. Total there are 32 input ports which are assigned 2 bit value and sel (select line) which is assigned 5 bit value.  

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
