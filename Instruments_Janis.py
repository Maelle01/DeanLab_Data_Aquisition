# from qcodes.instrument_drivers.stanford_research.SR830 import SR830
# from qcodes.instrument_drivers.stanford_research.SR86x import SR86x
# from qcodes.instrument_drivers.yokogawa.GS200 import GS200
# from qcodes.instrument_drivers.tektronix.Keithley_2400 import Keithley_2400
# from qcodes.instrument_drivers.tektronix.Keithley_2450 import Keithley2450
# from lakeshore331_test import LakeShore331
# from lakeshore_625_magnet_driver import Model_625
# from PyANC350v4 import Positioner
#from test_instr import TestInstr
from Measurement_Instruments import SR830_inst, SR860_inst, K2400_inst, SIM_inst, yoko_inst
from Oxford_3He_instr import MercuryiTC, AMI430
from Teslatron_instr import MercuryiTC_teslatron, MercuryiPS_teslatron
from Janis_Instruments import LakeShore335, LakeShore625
#import time
# import visa

# Name=V13_15
# Instrument=SR860
# GPIB=6
# channels=[True, False, False, True, False, False, False, False]

# rm = visa.ResourceManager()

class Instruments:
    
    def __init__(self):
        
        self.dic={}
        self.list_names=[];self.list_instr=[];self.list_gpib=[];self.list_ch=[]
        self.instr=[]
        self.lockins=[]
        self.not_lockins=[]
        self.read_file()
        
        # self.T_controller=LakeShore331('GPIB0::2::INSTR')
        # self.B_controller = Model_625('B','GPIB0::12::INSTR')
        
        for ind in range(len(self.list_names)):
            gpib='GPIB0::'+self.list_gpib[ind]+'::INSTR'
            if self.list_instr[ind]=='SR830':
                li=SR830_inst(self.list_names[ind],gpib,self.list_ch[ind])
                self.instr.append(li)
                self.lockins.append(li)
            elif self.list_instr[ind]=='SR860':
                li860=SR860_inst(self.list_names[ind],gpib,self.list_ch[ind])
                self.instr.append(li860)
#                self.lockins.append(li860)    
            elif self.list_instr[ind]=='Keithley 2400':
                k=K2400_inst(self.list_names[ind],gpib,self.list_ch[ind])
                self.instr.append(k)
                self.not_lockins.append(k)
            elif self.list_instr[ind]=='Yoko':
                y=yoko_inst(self.list_names[ind],gpib,self.list_ch[ind])
                self.instr.append(y)
                self.not_lockins.append(y)
            elif self.list_instr[ind]=='iTC 3He':
                itc=MercuryiTC(self.list_names[ind],self.list_ch[ind])
                self.instr.append(itc)
                self.not_lockins.append(itc)
            elif self.list_instr[ind]=='AMI 430 3He':
                ami430=AMI430(self.list_names[ind])
                self.instr.append(ami430)
                self.not_lockins.append(ami430)
            elif self.list_instr[ind]=='iPS Teslatron':
                ips_tt=MercuryiPS_teslatron(self.list_names[ind],self.list_ch[ind])
                self.instr.append(ips_tt)
                self.not_lockins.append(ips_tt)
            elif self.list_instr[ind]=='iTC Teslatron':
                itc_tt=MercuryiTC_teslatron(self.list_names[ind],self.list_ch[ind])
                self.instr.append(itc_tt)
                self.not_lockins.append(itc_tt)
            elif self.list_instr[ind]=='Janis Temperature':
                temp=LakeShore335(self.list_names[ind],self.list_ch[ind])
                self.instr.append(temp)
                self.not_lockins.append(temp)
            elif self.list_instr[ind]=='Janis Magnet':
                temp=LakeShore625(self.list_names[ind])
                self.instr.append(temp)
                self.not_lockins.append(temp)
            elif self.list_instr[ind]=='SIM':
                sim=SIM_inst(self.list_names[ind],gpib,self.list_ch[ind])
                self.instr.append(sim)
                self.not_lockins.append(sim)
            #elif self.list_instr[ind]=='tester':
                #self.instr.append(TestInstr(self.list_names[ind],self.list_gpib[ind],self.list_ch[ind]))
                
            else:
                pass
        self.hdr=self.header()
        
        # if self.dic[' lockin1\n'] == 'None'+'\n':
        #     pass
        # else:
        #     self.gpib_l1 = 'GPIB0::'+str(self.dic[' lockin1\n']).rstrip('\r\n')+'::INSTR'
        #     self.model_l1 = rm.open_resource(self.gpib_l1).query('*IDN?')
        #     if '830' in self.model_l1:
        #         self.SR_lockin1 = SR830('SR_1', self.gpib_l1)
        #     else:
        #         self.SR_lockin1 = SR86x('SR_1', self.gpib_l1, 10e6)
        # if self.dic[' lockin2\n'] == 'None'+'\n':
        #     pass
        # else:
        #     self.gpib_l2 = 'GPIB0::'+str(self.dic[' lockin2\n']).rstrip('\r\n')+'::INSTR'
        #     self.model_l2 = rm.open_resource(self.gpib_l2).query('*IDN?')
        #     if '830' in self.model_l2:
        #         self.SR_lockin2 = SR830('SR_2', self.gpib_l2)
        #     else:
        #         self.SR_lockin2 = SR86x('SR_2', self.gpib_l2, 10e6)
        # if self.dic[' lockin3\n'] == 'None'+'\n':
        #     pass
        # else:
        #     self.gpib_l3 = 'GPIB0::'+str(self.dic[' lockin3\n']).rstrip('\r\n')+'::INSTR'
        #     self.model_l3 = rm.open_resource(self.gpib_l3).query('*IDN?')
        #     if '830' in self.model_l3:
        #         self.SR_lockin3 = SR830('SR_3', self.gpib_l3)
        #     else:
        #         self.SR_lockin3 = SR86x('SR_3', self.gpib_l3, 10e6)
        # if self.dic[' lockin4\n'] == 'None'+'\n':
        #     pass
        # else:
        #     self.gpib_l4 = 'GPIB0::'+str(self.dic[' lockin4\n']).rstrip('\r\n')+'::INSTR'
        #     self.model_l4 = rm.open_resource(self.gpib_l4).query('*IDN?')
        #     if '830' in self.model_l4:
        #         self.SR_lockin4 = SR830('SR_4', self.gpib_l4)
        #     else:
        #         self.SR_lockin4 = SR86x('SR_4', self.gpib_l4, 10e6)
        # if self.dic[' lockin5\n'] == 'None'+'\n':
        #     pass
        # else:
        #     self.gpib_l5 = 'GPIB0::'+str(self.dic[' lockin5\n']).rstrip('\r\n')+'::INSTR'
        #     self.model_l5 = rm.open_resource(self.gpib_l5).query('*IDN?')
        #     if '830' in self.model_l5:
        #         self.SR_lockin5 = SR830('SR_5', self.gpib_l5)
        #     else:
        #         self.SR_lockin5 = SR86x('SR_5', self.gpib_l5, 10e6)
        # if self.dic[' lockin6\n'] == 'None'+'\n':
        #     pass
        # else:
        #     self.gpib_l6 = 'GPIB0::'+str(self.dic[' lockin6\n']).rstrip('\r\n')+'::INSTR'
        #     self.model_l6 = rm.open_resource(self.gpib_l6).query('*IDN?')
        #     if '830' in self.model_l6:
        #         self.SR_lockin6 = SR830('SR_6', self.gpib_l6)
        #     else:
        #         self.SR_lockin6 = SR86x('SR_6', self.gpib_l6, 10e6)
        # if self.dic[' lockin7\n'] == 'None'+'\n':
        #     pass
        # else:
        #     self.gpib_l7 = 'GPIB0::'+str(self.dic[' lockin7\n']).rstrip('\r\n')+'::INSTR'
        #     self.model_l7 = rm.open_resource(self.gpib_l7).query('*IDN?')
        #     if '830' in self.model_l7:
        #         self.SR_lockin7 = SR830('SR_7', self.gpib_l7)
        #     else:
        #         self.SR_lockin7 = SR86x('SR_7', self.gpib_l7, 10e6)
        # if self.dic[' lockin8\n'] == 'None'+'\n':
        #     pass
        
        # else:
        #     self.gpib_l8 = 'GPIB0::'+str(self.dic[' lockin8\n']).rstrip('\r\n')+'::INSTR'
        #     self.model_l8 = rm.open_resource(self.gpib_l8).query('*IDN?')
        #     if '830' in self.model_l8:
        #         self.SR_lockin8 = SR830('SR_8', self.gpib_l8)
        #     else:
        #         self.SR_lockin8 = SR86x('SR_8', self.gpib_l8, 10e6)
            
        # if self.dic[' keithley1\n'] == 'None'+'\n':
        #     pass
        # else:
        #     self.gpib_k1 = 'GPIB0::'+str(self.dic[' keithley1\n']).rstrip('\r\n')+'::INSTR'
        #     self.model_k1 = rm.open_resource(self.gpib_k1).query('*IDN?')
        #     if '2400' in self.model_k1:
        #         self.keithley1 = Keithley_2400('keithley1', self.gpib_k1)
        #     elif '2450' in self.model_k1:
        #         self.keithley1 = Keithley2450('keithley1', self.gpib_k1)
        #     else:
        #         pass
        # if self.dic[' keithley2\n'] == 'None'+'\n':
        #     pass
        # else:
        #     self.gpib_k2 = 'GPIB0::'+str(self.dic[' keithley2\n']).rstrip('\r\n')+'::INSTR'
        #     self.model_k2 = rm.open_resource(self.gpib_k2).query('*IDN?')
        #     if '2400' in self.model_k1:
        #         self.keithley2 = Keithley_2400('keithley2', self.gpib_k2)
        #     elif '2450' in self.model_k2:
        #         self.keithley2 = Keithley2450('keithley2', self.gpib_k2)
        #     else:
        #         pass
            
        # if self.dic[' yoko\n'] == 'None'+'\n':
        #     pass
        # else:
        #     self.gpib_y = 'GPIB0::'+str(self.dic[' yoko\n']).rstrip('\r\n')+'::INSTR'
        #     self.yoko1 = GS200('yoko1', self.gpib_y)
            
        # if self.dic[' sim\n'] == 'None'+'\n':
        #     pass
        # else:
        #     self.gpib_sim = 'GPIB0::'+str(self.dic[' sim\n']).rstrip('\r\n')+'::INSTR'
        #     self.sim = rm.open_resource(self.gpib_sim)
        #     print(self.sim.query('*IDN?'))
        # if self.dic[' rotator\n'] == 'None'+'\n':
        #     pass
        # else:
        #     self.rotator=Positioner()
        
        #self.T_control = MercuryiPS('mips', 'TCPIP0::255.255.255.255::7020::SOCKET')
    def header(self):
        hdr=[]
        for inst in self.instr:
            hdr.extend(inst.header())
        return hdr
    def measure(self):
        # st=time.time()
        msmt=[]
        for inst in self.instr:
            msmt.extend(inst.measure())
            # print(time.time()-st)
            
        return msmt
    def read_file(self):
        with open('Instruments.txt', 'rt') as f:
            for line in f:
                if line.startswith('Name')==True:
                    self.list_names.append(line.split('=')[1].rstrip())
                elif line.startswith('Instrument')==True:
                    self.list_instr.append(line.split('=')[1].rstrip())
                elif line.startswith('GPIB')==True:
                    self.list_gpib.append(line.split('=')[1].rstrip())
                elif line.startswith('channels')==True:
                    self.list_ch.append(line.split('=')[1].rstrip())
                else:
                    pass
    def get_instr(self, name):
        return self.instr[self.list_names.index(name)]
        