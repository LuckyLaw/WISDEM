#A simple test of WISDEM using the NREL CSM
# collected some code and added input output descriptions and layout output result to show to internal discuss
 

from wisdem.lcoe.lcoe_csm_assembly import lcoe_csm_assembly

lcoe = lcoe_csm_assembly()

# NREL 5 MW turbine specifications and plant attributes
lcoe.machine_rating = 5000.0 # Float(units = 'kW', iotype='in', desc= 'rated machine power in kW')
lcoe.rotor_diameter = 126.0 # Float(units = 'm', iotype='in', desc= 'rotor diameter of the machine')
lcoe.max_tip_speed = 80.0 # Float(units = 'm/s', iotype='in', desc= 'maximum allowable tip speed for the rotor')
lcoe.hub_height = 90.0 # Float(units = 'm', iotype='in', desc='hub height of wind turbine above ground / sea level')
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
lcoe.hub_height = 90.0 #Float(90.0, units = 'm', iotype='in', desc= 'hub height of wind turbine above ground / sea level')
lcoe.altitude = 0.0 #Float(0.0, units = 'm', iotype='in', desc= 'altitude of wind plant')
#lcoe.air_density = Float(0.0, units = 'kg / (m * m * m)', iotype='in', desc= 'air density at wind plant site')  # default air density value is 0.0 - forces aero csm to calculate air density in model
lcoe.drivetrain_design = 'geared' #Enum('geared', ('geared', 'single_stage', 'multi_drive', 'pm_direct_drive'), iotype='in')
lcoe.shear_exponent = 0.1 #Float(0.1, iotype='in', desc= 'shear exponent for wind plant') #TODO - could use wind model here
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

# max is 80m/s we make a scoop from 60-100 to see the lcoe curve
        
lcoe.run()
#print to a excel file: tp_20.excel






#NREL 5MW turbine basic parameters inputed
print"---------------NREL 5 MW turbine specifications and plant attributes--------------------"
print " Rated machine power in kW (machine_rating=) ", format(lcoe.machine_rating)  # Float(units = 'kW', iotype='in', desc= 'rated machine power in kW')
print"Rotor diameter of the machine (rotor_diameter=)",format(lcoe.rotor_diameter) # Float(units = 'm', iotype='in', desc= 'rotor diameter of the machine')
print"Maximum allowable tip speed for the rotor (max_tip_speed)=", format(lcoe.max_tip_speed)   # Float(units = 'm/s', iotype='in', desc= 'maximum allowable tip speed for the rotor')
print"Hub height of wind turbine above ground / sea level (hub_height)=",format(lcoe.hub_height)  # Float(units = 'm', iotype='in', desc='hub height of wind turbine above ground / sea level')
print"Sea depth for offshore wind project (sea_depth)=", format(lcoe.sea_depth)  # Float(units = 'm', iotype='in', desc = 'sea depth for offshore wind project')

print"Drive train desin=", format(lcoe.drivetrain_design)    # Enum('geared', ('geared', 'single_stage', 'multi_drive', 'pm_direct_drive'), iotype='in')
print"Latitude to sea=", format(lcoe.altitude)        # Float(0.0, units = 'm', iotype='in', desc= 'altitude of wind plant')
print" Total number of wind turbines at the plant=",format(lcoe.turbine_number)  # Int(100, iotype='in', desc = 'total number of wind turbines at the plant')
print" Total number of years to lcoe=",format(lcoe.year)  # Int(2009, iotype='in', desc = 'year of project start')
print" Total number of month of project start=",format(lcoe.month)  # Int(12, iotype='in', desc = 'month of project start')






# Extra AEP inputs
print"-------------------- Extra AEP inputs---------------"

print" Max power coefficient of rotor for operation in regin 2=",format(lcoe.max_power_coefficient)   #Float(0.488, iotype='in', desc= 'maximum power coefficient of rotor for operation in region 2')
print"Optimum tip speed ratio for operation in region 2= ",format(lcoe.opt_tsr)  #Float(7.525, iotype='in', desc= 'optimum tip speed ratio for operation in region 2')
print"cut in wind speed for the wind turbine =",format(lcoe.cut_in_wind_speed)  #Float(3.0, units = 'm/s', iotype='in', desc= 'cut in wind speed for the wind turbine')
print"cut out wind speed for the wind turbine =",format(lcoe.cut_out_wind_speed) #Float(25.0, units = 'm/s', iotype='in', desc= 'cut out wind speed for the wind turbine')
print"'hub height of wind turbine above ground / sea level =",format(lcoe.hub_height)   #Float(90.0, units = 'm', iotype='in', desc= 'hub height of wind turbine above ground / sea level')
print"altitude of wind plant =",format(lcoe.altitude)           #Float(0.0, units = 'm', iotype='in', desc= 'altitude of wind plant')
print"drive train choice  geard, pm_direct_drive =",format(lcoe.drivetrain_design)   #Enum('geared', ('geared', 'single_stage', 'multi_drive', 'pm_direct_drive'), iotype='in')
print"shear exponent for wind plant= ",format(lcoe.shear_exponent)     #Float(0.1, iotype='in', desc= 'shear exponent for wind plant') #TODO - could use wind model here
print"mean annual wind speed at 50 m height =",format(lcoe.wind_speed_50m)     #Float(8.35, units = 'm/s', iotype='in', desc='mean annual wind speed at 50 m height')
print"'weibull shape factor for annual wind speed distribution =",format(lcoe.weibull_k)         #Float(2.1, iotype='in', desc = 'weibull shape factor for annual wind speed distribution')
print"energy losses due to blade soiling for the wind plant - average across turbines =",format(lcoe.soiling_losses)    #Float(0.0, iotype='in', desc = 'energy losses due to blade soiling for the wind plant - average across turbines')
print"energy losses due to turbine interactions - across entire plant =",format(lcoe.array_losses)      #Float(0.06, iotype='in', desc = 'energy losses due to turbine interactions - across entire plant')
print"average annual availbility of wind turbines at plant =",format(lcoe.availability)      #Float(0.94287630736, iotype='in', desc = 'average annual availbility of wind turbines at plant')
print"total number of wind turbines at the plant =",format(lcoe.turbine_number)    #Int(100, iotype='in', desc = 'total number of wind turbines at the plant')
print"thrust coefficient at rated power =",format(lcoe.thrust_coefficient) #Float(0.50, iotype='in', desc='thrust coefficient at rated power')

# Extra TCC inputs
print"---------------------- Extra TCC inputs---------------"
print"number of rotor blades =",format(lcoe.blade_number)  #Int(3, iotype='in', desc = 'number of rotor blades')
print"design for offshore boolean  =",format(lcoe.offshore)      #Bool(True, iotype='in', desc = 'boolean for offshore')
print"boolean for use of advanced blade curve =",format(lcoe.advanced_blade) # True #Bool(False, iotype='in', desc = 'boolean for use of advanced blade curve')
print"for presence of a service crane up tower =",format(lcoe.crane )        #Bool(True, iotype='in', desc = 'boolean for presence of a service crane up tower')
print"indicator for drivetrain bedplate design 0 - conventional =",format(lcoe.advanced_bedplate)  #Int(0, iotype='in', desc= 'indicator for drivetrain bedplate design 0 - conventional')   
print"advanced tower configuration =",format(lcoe.advanced_tower) #Bool(False, iotype='in', desc = 'advanced tower configuration')

# Extra Finance inputs
print"----------------------- Extra Finance inputs----------"
print"fixed charge rate for coe calculation =",format(lcoe.fixed_charge_rate)   #Float(0.12, iotype = 'in', desc = 'fixed charge rate for coe calculation')
print"construction financing rate applied to overnight capital costs =",format(lcoe.construction_finance_rate) #Float(0.00, iotype='in', desc = 'construction financing rate applied to overnight capital costs')
print"tax rate applied to operations =",format(lcoe.tax_rate)  #Float(0.4, iotype = 'in', desc = 'tax rate applied to operations')
print"applicable project discount rate =",format(lcoe.discount_rate) #Float(0.07, iotype = 'in', desc = 'applicable project discount rate')
print"number of years to complete project construction =",format(lcoe.construction_time) #Float(1.0, iotype = 'in', desc = 'number of years to complete project construction')
print"project lifetime for LCOE calculation =",format(lcoe.project_lifetime)  #Float(20.0, iotype = 'in', desc = 'project lifetime for LCOE calculation')




print"-----Calculate  Output  --------"
print "LCOE: ${0:.4f} USD/kWh".format(lcoe.lcoe)
print "COE: ${0:.4f} USD/kWh".format(lcoe.coe)
print
print "AEP per turbine: {0:1f} kWh/turbine".format(lcoe.net_aep / lcoe.turbine_number)
print "Turbine Cost: ${0:2f} USD".format(lcoe.turbine_cost)
print "BOS costs per turbine: ${0:2f} USD/turbine".format(lcoe.bos_costs / lcoe.turbine_number)
print "OPEX per turbine: ${0:2f} USD/turbine".format(lcoe.avg_annual_opex / lcoe.turbine_number)
print

