# main class
class Currency:
  def __init__(self,value,symbol=None,abbreviation=None):
    self.value = value
    self.symbol = symbol
    self.abbreviation = abbreviation
  def __repr__(self) -> str:
    return "This is just for test and returns Main Class"
# inhereted from main class
class Convertor(Currency):
  def Convert():
    return "Converting is on the process"
# Converting EUR to USD class
class EUR_Conversion(Convertor):
  pass 
  
