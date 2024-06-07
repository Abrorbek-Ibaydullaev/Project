# Defining a base class for Currency.

class Currency:
    def __init__(self, amount):
        # Initializing the currency with a given amount and validating it.
        self.set_amount(amount)

    def get_amount(self):
        # Getter method to retrieve the amount.
        return self._amount

    def set_amount(self, amount):
        # Setter method to set the amount and ensure it's non-negative.
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        self._amount = amount
    # Convert_to method could be considered to exhibit a form of overloading behavior
    def convert_to(self,target):
        if isinstance(target,Currency):
            return self._convert_to_currency(target)
        elif isinstance(target,str):
            return self._convert_to_currency_code(target)
        else:
            raise TypeError("Target must be a Currency object or string")
        
    # Placeholder method to be implemented in subclasses for converting to another Currency object.
    def _convert_to_currency(self, target_currency):
        raise NotImplementedError("Subclasses should implement this method")

    # Placeholder method to be implemented in subclasses for converting to a currency identified by a string.
    def _convert_to_currency_code(self, currency_code):
        raise NotImplementedError("Subclasses should implement this method")

    def __str__(self):
        # String representation of the currency amount.
        return f"{self._amount:.0f} {self.__class__.__name__}"


class UniversalCurrenyConverter(Currency):
    def __init__(self, amount, currency_code, exchange_rates=None):
        super().__init__(amount)
        self.currency_code = currency_code
        if exchange_rates is None:
            self.exchange_rates = {
                "USD":1.0,
                "EUR":0.85,
                "JPY":110.0,
                "GBP":0.75,
            }
        else:
            self.exchange_rates = exchange_rates
            
        if currency_code not in self.exchange_rates:
            raise ValueError(f"Unsupported currency code: {currency_code}")
        
    def add_currency(self, currency_code,exchange_rate):
        if exchange_rate <= 0:
            raise ValueError("Exchange rate must be positive.")
        self.exchange_rates[currency_code] = exchange_rate
        print(
            f"Added curreny {currency_code} with exchange rate {exchange_rate}. Current exchange rates: {self.exchange_rates}")
        
    def update_exchange_rate(self, currency_code, exchange_rate):
        if currency_code not in self.exchange_rates:
            raise ValueError(f"Currency code {currency_code} does not exist.")
        if exchange_rate <= 0:
            raise ValueError("Exchange rate must be positive.")
        self.exchange_rates[currency_code] = exchange_rate
        print(
            f"Updated exchange rate for {currency_code} to {exchange_rate}. Current exchange rates: {self.exchange_rates}")
        
    def _convert_to_currency(self, target_currency):
        if not isinstance(target_currency,UniversalCurrenyConverter):
            raise ValueError(
                "Target currency must be an instance of UniversalCurrencyConverter")
        base_amount = self._amount / self.exchange_rates[self.currency_code]
        target_amount = base_amount * \
            self.exchange_rates[target_currency.currency_code]
        return UniversalCurrenyConverter(target_amount,target_currency.currency_code,self.exchange_rates)
    
    def _convert_to_currency_code(self,currency_code):
        if currency_code not in self.exchange_rates:
            raise ValueError(f"Unsuppoted currency code: {currency_code}")
        base_amount = self._amount / self.exchange_rates[self.currency_code]
        target_amount = base_amount * self.exchange_rates[currency_code]
        return UniversalCurrenyConverter(target_amount,currency_code, self.exchange_rates)
    
    def __str__(self):
        return f"{self._amount:.2f} {self.currency_code}"

class EUR(Currency):
    def __init__(self, amount):
        # Initializing with the base class constructor.
        super().__init__(amount)

    def _convert_to_currency(self, target_currency):
        # Conversion logic from EUR to other currencies.
        if isinstance(target_currency, USD):
            return self._amount * 1.18
        elif isinstance(target_currency, GBP):
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
            raise ValueError("Conversion rate not available")


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
            return self._amount * 1.14
        else:
            return super()._convert_to_currency(target_currency)

    def _convert_to_currency_code(self, currency_code):
        # Conversion logic from GBP to currencies identified by a string.
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
        if isinstance(to_currency, Currency):
            converted_amount = from_currency.convert_to(to_currency)
            # Create a new instance of the target currency type.
            return to_currency.__class__(converted_amount)
        elif isinstance(to_currency, str):
            converted_amount = from_currency.convert_to(to_currency)
            # Return a new instance of the target currency identified by the string.
            if to_currency == 'USD':
                return USD(converted_amount)
            elif to_currency == 'EUR':
                return EUR(converted_amount)
            elif to_currency == 'GBP':
                return GBP(converted_amount)
            else:
                raise ValueError("Unknown currency code")
        else:
            raise TypeError(
                "to_currency must be a Currency object or a string")


# Class for performing operations on currency objects.
class CurrencyOperations:
    @staticmethod
    def add(c1, c2):
        # Add two currencies of the same type.
        if c1.__class__ == c2.__class__:
            # Create a new instance of the same type with the summed amount.
            return c1.__class__(c1.get_amount() + c2.get_amount())
        raise ValueError(
            "Cannot add different currencies directly. Convert them to the same type first.")

    @staticmethod
    def subtract(c1, c2):
        # Subtract two currencies of the same type.
        if c1.__class__ == c2.__class__:
            # Create a new instance of the same type with the subtracted amount.
            return c1.__class__(c1.get_amount() - c2.get_amount())
        raise ValueError(
            "Cannot subtract different currencies directly. Convert them to the same type first.")


# Custom exception class for currency-related errors.
class CurrencyError(Exception):
    """Base class for other exceptions"""
    pass


# Custom exception for handling negative amounts.
class NegativeAmountError(CurrencyError):
    """Raised when the amount is negative"""
    pass
