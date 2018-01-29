#-*- coding: UTF-8 -*-
#A simple test of WISDEM using the NREL CSM
# collected some code and added input output descriptions and layout output result to show to internal discuss
import xlrd
from pyExcelerator import *

from wisdem.lcoe.lcoe_csm_assembly import lcoe_csm_assembly

lcoe = lcoe_csm_assembly()

# NREL 5 MW turbine specifications and plant attributes
lcoe.machine_rating = 5000.0 # Float(units = 'kW', iotype='in', desc= 'rated machine power in kW')
lcoe.rotor_diameter = 126.0 # Float(units = 'm', iotype='in', desc= 'rotor diameter of the machine')
#lcoe.max_tip_speed = 80.0 # Float(units = 'm/s', iotype='in', desc= 'maximum allowable tip speed for the rotor')
lcoe.sea_depth = 20.0 # Float(units = 'm', iotype='in', desc = 'sea depth for offshore wind project')

# Parameters
lcoe.drivetrain_design = 'pm_direct_drive' # Enum('geared', ('geared', 'single_stage', 'multi_drive', 'pm_direct_drive'), iotype='in')
lcoe.altitude = 0.0 # Float(0.0, units = 'm', iotype='in', desc= 'altitude of wind plant')
lcoe.turbine_number = 100 # Int(100, iotype='in', desc = 'total number of wind turbines at the plant')
lcoe.year = 2009 # Int(2009, iotype='in', desc = 'year of project start')
lcoe.month = 12 # Int(12, iotype='in', desc = 'month of project start')

# Extra AEP inputs
lcoe.max_power_coefficient = 0.488 #Float(0.488, iotype='in', desc= 'maximum power coefficient of rotor for operation in region 2')
lcoe.opt_tsr = 7.525 #Float(7.525, iotype='in', desc= 'optimum tip speed ratio for operation in region 2')
lcoe.cut_in_wind_speed = 3.0 #Float(3.0, units = 'm/s', iotype='in', desc= 'cut in wind speed for the wind turbine')
lcoe.cut_out_wind_speed = 25.0 #Float(25.0, units = 'm/s', iotype='in', desc= 'cut out wind speed for the wind turbine')
#lcoe.hub_height = 90.0 #Float(90.0, units = 'm', iotype='in', desc= 'hub height of wind turbine above ground / sea level')
lcoe.altitude = 0.0 #Float(0.0, units = 'm', iotype='in', desc= 'altitude of wind plant')
#lcoe.air_density = Float(0.0, units = 'kg / (m * m * m)', iotype='in', desc= 'air density at wind plant site')  # default air density value is 0.0 - forces aero csm to calculate air density in model
lcoe.drivetrain_design = 'pm_direct_drive' #Enum('geared', ('geared', 'single_stage', 'multi_drive', 'pm_direct_drive'), iotype='in')
#lcoe.shear_exponent = 0.1 #Float(0.1, iotype='in', desc= 'shear exponent for wind plant') #TODO - could use wind model here
lcoe.wind_speed_50m = 8.02 #Float(8.35, units = 'm/s', iotype='in', desc='mean annual wind speed at 50 m height')
lcoe.weibull_k= 2.15 #Float(2.1, iotype='in', desc = 'weibull shape factor for annual wind speed distribution')
lcoe.soiling_losses = 0.0 #Float(0.0, iotype='in', desc = 'energy losses due to blade soiling for the wind plant - average across turbines')
lcoe.array_losses = 0.10 #Float(0.06, iotype='in', desc = 'energy losses due to turbine interactions - across entire plant')
lcoe.availability = 0.941 #Float(0.94287630736, iotype='in', desc = 'average annual availbility of wind turbines at plant')
lcoe.turbine_number = 100 #Int(100, iotype='in', desc = 'total number of wind turbines at the plant')
lcoe.thrust_coefficient = 0.50 #Float(0.50, iotype='in', desc='thrust coefficient at rated power')

# Extra TCC inputs
lcoe.blade_number = 3 #Int(3, iotype='in', desc = 'number of rotor blades')
lcoe.offshore = True #Bool(True, iotype='in', desc = 'boolean for offshore')
lcoe.advanced_blade = True #Bool(False, iotype='in', desc = 'boolean for use of advanced blade curve')
lcoe.crane = True #Bool(True, iotype='in', desc = 'boolean for presence of a service crane up tower')
lcoe.advanced_bedplate = 0 #Int(0, iotype='in', desc= 'indicator for drivetrain bedplate design 0 - conventional')   
lcoe.advanced_tower = False #Bool(False, iotype='in', desc = 'advanced tower configuration')

# Extra Finance inputs
lcoe.fixed_charge_rate = 0.12 #Float(0.12, iotype = 'in', desc = 'fixed charge rate for coe calculation')
lcoe.construction_finance_rate = 0.00 #Float(0.00, iotype='in', desc = 'construction financing rate applied to overnight capital costs')
lcoe.tax_rate = 0.4 #Float(0.4, iotype = 'in', desc = 'tax rate applied to operations')
lcoe.project_lifetime = 15.0 #Float(20.0, iotype = 'in', desc = 'project lifetime for LCOE calculation')

# max is 80m/s we make a scoop from 60-120 to see the lcoe curve
w=Workbook()  #创建工作簿
ws=w.add_sheet('Sheet1')  #添加工作表
i=j=0
ws.write(i,j,format("max_tip_speed"))    # tip speed 
ws.write(i,j+1, format("shear_0.1"))     #lcoe
ws.write(i,j+2, format("shear_0.15"))     #coe
ws.write(i,j+3, format("shear_0.2"))     #coe
ws.write(i,j+4, format("shear_0.25"))     #coe
ws.write(i,j+5, format("shear_0.3"))     #coe
#ws.write(i,j+6, format("lcoe.130m"))     #coe
#ws.write(i,j+7, format("lcoe.140m"))     #coe
j = 0
i = 1
lcoe.shear_exponent = 0.1 #Float(0.1, iotype='in', desc= 'shear exponent for wind plant') #TODO - could use wind model here
#begin cal and write to excel file
v_tip = 40

lcoe.hub_height = 80.0 # Float(units = 'm', iotype='in', desc='hub height of wind turbine above ground / sea level')
while (v_tip <= 120)&(lcoe.shear_exponent <=0.3):
      
    print "tip _speed=", format(v_tip)	
    lcoe.max_tip_speed = v_tip  # Float(units = 'm/s', iotype='in', desc= 'maximum allowable tip speed for the rotor')
    lcoe.run()
    print" lcoe.run done"
#write to a excel file with speed/lcoe 
    if (lcoe.shear_exponent == 0.1) :
        ws.write(i,j,format(lcoe.max_tip_speed))    # tip speed 

    ws.write(i,j+1, format(lcoe.lcoe*6.9))     #lcoe at tower hight start 
    print "loce.shear_exponent==", format(lcoe.shear_exponent)	
#	ws.write(i,j+2, format(lcoe.coe))     #coe
#	ws.write(i,j+3, format(lcoe.net_aep / lcoe.turbine_number))  #aep per turbine
#	ws.write(i,j+4, format(lcoe.turbine_cost))        # total turbine cost
#	ws.write(i,j+5, format(lcoe.bos_costs / lcoe.turbine_number)) # BOS costs per turbine 
#	ws.write(i,j+6, format(lcoe.avg_annual_opex / lcoe.turbine_number)) #OPEX per turbine

#save to excel file name  tipvslcoe

    i = i+1
    v_tip = v_tip+1
    if v_tip == 120:
        v_tip = 40
        lcoe.shear_exponent = lcoe.shear_exponent + 0.05      # Float(units = 'm', iotype='in', desc='hub height of wind turbine above ground / sea level')
        j = j+1
        i = 1
    print " ok"
else:
    w.save('tipspeedvslcoe_shear_80m.xls')
    print "-------------complete--------------"
    print " lcoe vs tip speed from 40 m/s to 100 m/s"



