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

# Transaction class tests
class TestTransaction(unittest.TestCase):
    def test_initialization(self):
        t = Transaction(100,"USD")
        self.assertEqual(t.amount,100)
        self.assertEqual(t.currency_code,"USD")
        
    def test_send_and_recieve_money(self):
        t1 = Transaction(100,"USD")
        t2 = Transaction(50,"USD")
        t1.send_money(t2,30)
        self.assertEqual(t1.amount,70)
        self.assertEqual(t1.amount,70)
        
# International Transaction class tests 

class TestInternationalTransaction(unittest.TestCase):
    def test_initialization(self):
        rates = {"USD":1.0,"EUR":0.85,"JYP":110.0,"GBP":0.75}
        it = InternationalTransaction(100,"USD",rates)
        self.assertEqual(it.amount,100)
        self.assertEqual(it.currency_code,"USD")
        self.assertEqual(it.exchange_rates,rates)
        
    def test_send_and_recieve_money_with_conversion(self):
        rates = {"USD":1.0,"EUR":0.85,"JYP":110.0,"GBP":0.75}
        it1 = InternationalTransaction(100,"USD",rates)
        it2 = InternationalTransaction(0,"EUR",rates)
        it1.send_money(it2,50,"EUR")
        self.assertEqual(it1.amount,50)        
        self.assertEqual(it2.amount,0)
    
    def test_convert_currency(self):
        rates = {"USD":1.0,"EUR":0.85,"JYP":110.0,"GBP":0.75}
        it = InternationalTransaction(100,"USD",rates)
        converted_amount = it.convert_currency(100,"USD","EUR")
        self.assertEqual(converted_amount,85.0)
                
if __name__ == "__main__":
    unittest.main()
