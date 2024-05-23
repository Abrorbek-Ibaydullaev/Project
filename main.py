# Importing the dispatch decorator from multipledispatch to enable method overloading.
from multipledispatch import dispatch

# Defining  a base class  for Currency.
class Currency:
  def __init__(self,amount):
    # Initializing the currency with a given amount and validating it.
    self.set_amount(amount)

  def get_amount(self):
    # Getter method to retrieve the amount.
    return self._amount
  def set_amount(self,amount):
    # Setter method to set the amount and ensure it's non-negative.
    if amount < 0:
      raise ValueError("Amount cannot be negative.")
    self._amount = amount
  #  Overloaded method to convert the currency to another type.This version raises an error if target is neither a Currency object nor a string.
  @dispatch(object)
  def convert_to(self,target):
    raise TypeError("Target must be a Currency object or a string")
  
  # Overloaded method to convert to another Currency object.
  @dispatch(object)
  def convert_to(self,target:'Currency'):
    return self._convert_to_currency(target)
  
  # Overloaded method to convert to a currency identified by string.
  @dispatch(object)
  def convert_to(self,target:str):
    return self._convert_to_currency(target)
  
  # Placeholder method to be implemented in subclasses for converting to another Currency object.
  def _convert_to_currency(self,target_currency):
    raise NotImplementedError("Subclasses should inplement this method")
  
  # Placeholder method to be implemented in subclasses for converting to a currency identified by a string.
  def _convert_to_currency(self,currency_code):
    raise NotImplementedError("Subclasses should inplement this method")
  
  def __str__(self):
    # String representation of the currency amount.
    return f"{self._amount:.0f} {self.__class__.__name__}"
  
 # Subclass for USD currency.
class USD(Currency):
  def __init__(self,amount):
    # Initializing with the base class constructor.
    super().__init__(amount)
    
  def _convert_to_currency(self, target_currency):
    # Conversion logic from USD to other currencies.
    if isinstance(target_currency,EUR):
      return self._amount * 0.85
    elif isinstance(target_currency,GBP):
      return self._amount * 0.75
    else:
      return super()._convert_to_currency(target_currency)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# # inhereted from main class
# class Convertor(Currency):
#   def Convert(self):
#     return "Converting is on the process"
# # Converting EUR to USD class
# class EUR_Conversion(Convertor):
#   base_rate = 1.08
#   def Convert(self,amount):
#     return self.amount*EUR_Conversion.base_rate
    
  
