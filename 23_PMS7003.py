import machine, time
from pms7003 import PMS7003
from aqi import AQI

u2=machine.UART(2, baudrate=9600, rx=16, tx=17)
#time.sleep_ms(500)
pms = PMS7003(u2)
#time.sleep_ms(500)

pms_data = pms.read()


#print (pms_data)
aqi = AQI.aqi(pms_data['PM2_5_ATM'], pms_data['PM10_0_ATM'])
print("***************")
print("PMS7003 values:")
print("***************")

print('PM  1.0:', pms_data['PM1_0_ATM'])
print('PM  2.5:', pms_data['PM2_5_ATM'])
print('PM 10.0:', pms_data['PM10_0_ATM'])
print('AQI    :',aqi)

