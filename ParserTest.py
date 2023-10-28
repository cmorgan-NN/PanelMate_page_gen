#For testing Parsers :P
from Parser import *

parsedVisualOrders = Parser.vSIndicator('Gas Alarms\Variable-Sized_Indicator_Template.rpc')

#parsedVisualOrders = Parser.vSReadout('Drives 4\Variable-Sized_Readout_Template.rpc')

print(parsedVisualOrders)