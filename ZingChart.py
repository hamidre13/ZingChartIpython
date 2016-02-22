from __future__ import print_function
import os
import argparse
from IPython.core.magic import (Magics, magics_class, line_magic,cell_magic, line_cell_magic) 
from IPython.core.display import HTML
try: 
  import simplejson as json
except:
  import json
import random

class Ipython():
  def __init__(self):
    self.source = "<script src='http://cdn.zingchart.com/zingchart.min.js'/>"
    self.isZingSource = False
  def Draw (self,ChartData,width = 600,height = 400,**Name ):
    if self.isZingSource:
      self.source = ''
    if 'DivName' in Name:
      DivId = Name['DivName']
    else :
      DivId = random.getrandbits(128)
    output = """
    <script type='text/javascript'>
      zingchart.render({
        id:'%(divId)s',
        data:%(data)s,
        height:%(height)s,
        width:%(width)s
      });
      </script>
      <div id="%(divId)s"></div>
    """%{'divId':DivId,'data':json.dumps(ChartData,sort_keys=True),'height':height,'width': width}
    self.isZingSource = True
    return HTML(self.source+output)
    
