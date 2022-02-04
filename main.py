import irsdk
import time

ir = irsdk.IRSDK()

# Camera Groups
# 0 Stay the same
# 1 Nose
# 2 Gearbox
# 3 Roll Bar
# 4 LF Susp
# 5 LR Susp
# 6 Gyro
# 7 RF Susp
# 8 RR Susp
# 9 Cockpit
# 10 Scenic
# 11 TV3
# 12 TV1
# 13 TV2
# 14 TV Static
# 15 TV Mixed
# 16 Pit Lane
# 17 Pit Lane 2
# 18 Blimp
# 19 Chopper
# 20 Chase
# 21 Far Chase
# 22 Rear Chase

ir.startup()  #dump_to="dump.bin")
ir.parse_to("dump2.txt")
print(ir["DriverInfo"])
#ir.cam_switch_num(28, 1)
# for x in range(23):
#     ir.cam_switch_num(6,x)
#     ir.freeze_var_buffer_latest()
#     print(x)
#     time.sleep(5)