import unittest
from main import *
# Currency class tests


class TestCurrency(unittest.TestCase):
    def test_initialization_and_amount_setting(self):
        c = Currency(100)
        self.assertEqual(c.get_amount(),100)
    
    def test_amount_setting_with_invalid_values(self):
        with self.assertRaises(ValueError):
            Currency(-100)
    
    def test_conversion_methods_raise_not_implemented_error(self):
        c = Currency(100)
        with self.assertRaises(NotImplementedError):
            c._convert_to_currency(Currency(100))
        with self.assertRaises(NotImplementedError):
            c._convert_to_currency("USD")

# Universal currency converter class

class TestUniversalCurrencyConverter(unittest.TestCase):
    def test_initialization_with_default_exchange_rate(self):
        uc = UniversalCurrenyConverter(100,"USD")
        self.assertEqual(uc.get_amount(),100)
        self.assertEqual(uc.currency_code,"USD")
        self.assertIn("USD",uc.exchange_rates)
        
    def test_initialization_with_custom_exchange_rates(self):
        custom_rates = {"USD":1.0,"CAD":1.25}
        uc = UniversalCurrenyConverter(100, "USD", custom_rates)
        self.assertEqual(uc.exchange_rates,custom_rates)
    
    def test_add_currency(self):
        uc = UniversalCurrenyConverter(100,"USD")
        uc.add_currency("CAD",1.25)
        self.assertIn("CAD",uc.exchange_rates)
        self.assertEqual(uc.exchange_rates["CAD"],1.25)
        
    def test_update_exchange_rates(self):
        uc = UniversalCurrenyConverter(100,"USD")
        uc.update_exchange_rate("EUR",0.9)
        self.assertEqual(uc.exchange_rates["EUR"],0.9)
        
    def test_convert_to_currency(self):
        uc1 = UniversalCurrenyConverter(100,"USD")
        uc2 = UniversalCurrenyConverter(0,"EUR")
        converted = uc1._convert_to_currency(uc2)
        self.assertEqual(converted.get_amount(),85.0)
        self.assertEqual(converted.currency_code,"EUR")
    
    def test_convert_to_currency_code(self):
        uc = UniversalCurrenyConverter(100,"USD")
        converted = uc._convert_to_currency_code("EUR")
        self.assertEqual(converted.get_amount(),85.0)
        self.assertEqual(converted.currency_code,"EUR")
        
if __name__ == "__main__":
    unittest.main()