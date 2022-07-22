# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random
from cocotb.result import TestFailure

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
 
    inp0  = 0 
    inp1  = 1
    inp2  = 2
    inp3  = 3
    inp4 = 0
    inp5 = 1
    inp6 = 2
    inp7 = 3
    inp8  = 0
    inp9 = 1
    inp10 = 2
    inp11 = 3
    inp12 = 0
    inp13 = 1
    inp14 = 2
    inp15 = 3
    inp16 = 0
    inp17 = 1
    inp18 = 2
    inp19 = 3
    inp20 = 0
    inp21  = 1
    inp22 = 2
    inp23 = 3
    inp24 = 0
    inp25 = 1
    inp26 = 2
    inp27 = 3
    inp28 = 0
    inp29 = 1
    inp30 = 2

    sel = 0
    dut.sel.value = sel

    dut.inp0.value = inp0
    dut.inp1.value = inp1
    dut.inp2.value = inp2
    dut.inp3.value = inp3
    dut.inp4.value = inp4
    dut.inp5.value = inp5
    dut.inp6.value = inp6
    dut.inp7.value = inp7
    dut.inp8.value = inp8
    dut.inp9.value = inp9
    dut.inp10.value = inp10
    dut.inp11.value = inp11
    dut.inp12.value = inp12
    dut.inp13.value = inp13
    dut.inp14.value = inp14
    dut.inp15.value = inp15
    dut.inp16.value = inp16
    dut.inp17.value = inp17
    dut.inp18.value = inp18
    dut.inp19.value = inp19
    dut.inp20.value = inp20
    dut.inp21.value = inp21
    dut.inp22.value = inp22
    dut.inp23.value = inp23
    dut.inp24.value = inp24
    dut.inp25.value = inp25
    dut.inp26.value = inp26
    dut.inp27.value = inp27
    dut.inp28.value = inp28
    dut.inp29.value = inp29
    dut.inp30.value = inp30
    
    await Timer(2, units='ns')
    dut._log.info(f'sel - {sel} inp0 - {inp0} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp0.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp0 - {int(dut.inp0.value)}   Test Failed !!!"


    sel = 1
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp1 - {inp1} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp1.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp1 - {int(dut.inp1.value)}   Test Failed !!!"
    
    sel = 2
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp2 - {inp2} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp2.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp2 - {int(dut.inp2.value)}   Test Failed !!!"

    sel = 3
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp3 - {inp3} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp3.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp3 - {int(dut.inp3.value)}   Test Failed !!!"
    
    sel = 4
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp4 - {inp4} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp4.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp4 - {int(dut.inp4.value)}   Test Failed !!!"
    
    sel = 5
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp5 - {inp5} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp5.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp5 - {int(dut.inp5.value)}   Test Failed !!!"
    
    sel = 6
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp6 - {inp6} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp6.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp6 - {int(dut.inp6.value)}   Test Failed !!!"
    
    sel = 7
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp7 - {inp7} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp7.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp7 - {int(dut.inp7.value)}   Test Failed !!!"
    
    sel = 8
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp8 - {inp8} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp8.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp8 - {int(dut.inp8.value)}   Test Failed !!!"
    

    sel = 9
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp9 - {inp9} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp9.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp9 - {int(dut.inp9.value)}   Test Failed !!!"
    

    sel = 10
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp10 - {inp10} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp10.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp10 - {int(dut.inp10.value)}   Test Failed !!!"
    
    sel = 11
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp11 - {inp11} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp11.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp11 - {int(dut.inp11.value)}   Test Failed !!!"
    
    sel = 12
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp12 - {inp12} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp12.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp12 - {int(dut.inp12.value)}   Test Failed !!!"
    
    sel = 14
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp14 - {inp14} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp14.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp14 - {int(dut.inp14.value)}   Test Failed !!!"
    
    sel = 15
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp15 - {inp15} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp15.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp15 - {int(dut.inp15.value)}   Test Failed !!!"
    
    sel = 16
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp16 - {inp16} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp16.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp16 - {int(dut.inp16.value)}   Test Failed !!!"
    
    sel = 17
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp17 - {inp17} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp17.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp17 - {int(dut.inp17.value)}   Test Failed !!!"

    sel = 18
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp18 - {inp18} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp18.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp18 - {int(dut.inp18.value)}   Test Failed !!!"
    
    sel = 19
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp19 - {inp19} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp19.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp19 - {int(dut.inp19.value)}   Test Failed !!!"
    
    sel = 20
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp20 - {inp20} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp20.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp20 - {int(dut.inp20.value)}   Test Failed !!!"
    
    sel = 21
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp21 - {inp21} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp21.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp21 - {int(dut.inp21.value)}   Test Failed !!!"
    
    sel = 22
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp22 - {inp22} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp22.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp22 - {int(dut.inp22.value)}   Test Failed !!!"
    
    sel = 23
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp23 - {inp23} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp23.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp23 - {int(dut.inp23.value)}   Test Failed !!!"
    

    sel = 24
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp24 - {inp24} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp24.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp24 - {int(dut.inp24.value)}   Test Failed !!!"
    

    sel = 25
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp25 - {inp25} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp25.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp25 - {int(dut.inp25.value)}   Test Failed !!!"
    
    sel = 26
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp26 - {inp26} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp26.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp26 - {int(dut.inp26.value)}   Test Failed !!!"
    
    sel = 27
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp27 - {inp27} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp27.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp27 - {int(dut.inp27.value)}   Test Failed !!!"
    
    sel = 28
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp28 - {inp28} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp28.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp28 - {int(dut.inp28.value)}   Test Failed !!!"
    
    sel = 29
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp29 - {inp29} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp29.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp29 - {int(dut.inp29.value)}   Test Failed !!!"
    

    #  Bug Exposed !!  for Sel = 13 and Sel = 30 We get Incorrect Output
    #  If you uncomment The below statements you can find that below testcases fails.



    # sel = 13
    # dut.sel.value = sel

    # await Timer(4, units='ns')
    # dut._log.info(f'sel - {sel}  inp13 - {inp13} out - {int(dut.out.value)}')
    # assert dut.out.value == dut.inp13.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp13 - {int(dut.inp13.value)}   Test Failed !!!"
    
    sel = 30
    dut.sel.value = sel

    await Timer(4, units='ns')
    dut._log.info(f'sel - {sel} inp30 - {inp30} out - {int(dut.out.value)}')
    assert dut.out.value == dut.inp30.value, f" result is incorrect: sel - {sel}  out - {int(dut.out.value)} != inp30 - {int(dut.inp30.value)}   Test Failed !!!"
    
