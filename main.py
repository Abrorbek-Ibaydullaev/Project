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
  
  def _convert_to_currency_code(self, currency_code):
    # Conversion logic from USD to currencies identified by a string.
    if currency_code == 'EUR':
      return self._amount * 0.85
    elif currency_code == 'GBP':
      return self._amount * 0.75
    else:
      raise ValueError("Conversion rate not available")

# Subclass for EUR currency.
class EUR(Currency):
  def __init__(self,amount):
    # Initializing with the base class constructor.
    super().__init__(amount)
    
  def _convert_to_currency(self, target_currency):
    # Conversion logic from EUR to other currencies.
    if isinstance(target_currency,USD):
      return self._amount * 1.18
    elif isinstance(target_currency,GBP):
      return self._amount * 0.88
    else:
      return super()._convert_to_currency(target_currency)
  
  def _convert_to_currency_code(self, currency_code):
    # Conversion logic from EUR to currencies identified by a string.
    if currency_code == 'USD':
      return self._amount * 1.18
    elif currency_code == 'GBP':
      return self._amount * 0.88
    else:
      raise ValueError('Conversion rate not available')

# Subclass for GBP currency.
class GBP(Currency):
  def __init__(self, amount):
    # Initializing with the base class constructor.
    super().__init__(amount)
  
  def _convert_to_currency(self, target_currency):
    # Conversion logic from GBP to other currencies.
    if isinstance(target_currency, USD):
      return self._amount * 1.33
    elif isinstance(target_currency, EUR):
      return self._amount *1.14
    else:
      return super()._convert_to_currency(target_currency)
  
  def _convert_to_currency_code(self,currency_code):
    # Conversion logic from GBP to currencies identified by a string
    if currency_code == 'USD':
      return self._amount * 1.33
    elif currency_code == 'EUR':
      return self._amount * 1.14
    else:
      raise ValueError("Conversion rate not available")

# Class for converting between different currencies.
class CurrencyConverter:
  @staticmethod
  def convert(from_currency, to_currency):
    # Convert from one currency to another.
    if isinstance(to_currency,Currency):
      converted_amount = from_currency.convert_to(to_currency)
      # Create a new instance of the target currency type.
      return to_currency.__class__(converted_amount)
    elif isinstance(to_currency,str):
      converted_amount = from_currency.convert_to(to_currency)
      # Return a new instance of the target currency identified by the string.
      if to_currency == 'USD':
        return USD(converted_amount)
      elif to_currency == 'EUR':
        return EUR(converted_amount)
      elif to_currency == 'GBP':
        return GBP(converted_amount)
      else:
        raise ValueError("Uknown currency code")
    else:
      raise TypeError("to_currency must be a Currency object or a string")

# Class for performing operations on currency objects.
class CurrencyOperations:
  @staticmethod
  def add(c1,c2):
    # Add 2 currencies of the sum type.
    if c1.__class__ == c2.__class__:
      # Create a new instance of the same type with the summed amount.
      return c1.__class__(c1.get_amount()+c2.get_amount())
    else:
      raise ValueError("Cannot add different currencies directly. Convert them to the same type first")
    
  @staticmethod
  def subtract(c1,c2):
    # subtract 2 currencies of the same type.
    if c1.__class__ ==c2.__class__:
      # Create a new instance of the same type with the subtracted amount.
      return c1.__class__(c1.get_amount()-c2.get_amount())
    else:
      raise ValueError("Cannot subtract different currencies directly. Convert them to the same type first")

# Custom exception class for currency-related errors.
class CurrencyError(Exception):
  """Base class for other exceptions"""
  pass

# Custom exception for handling negative amounts.
class NegativeAmountError(CurrencyError):
  """Raised when the amount is negative"""
  pass
