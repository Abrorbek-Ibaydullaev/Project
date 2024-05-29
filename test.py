import unittest
from main import USD, EUR, GBP, CurrencyConverter, CurrencyOperations


class TestCurrency(unittest.TestCase):

    def test_usd_creation(self):
        usd = USD(100)
        self.assertEqual(usd.get_amount(), 100)
        self.assertEqual(str(usd), "100 USD")

    def test_eur_creation(self):
        eur = EUR(85)
        self.assertEqual(eur.get_amount(), 85)
        self.assertEqual(str(eur), "85 EUR")

    def test_gbp_creation(self):
        gbp = GBP(75)
        self.assertEqual(gbp.get_amount(), 75)
        self.assertEqual(str(gbp), "75 GBP")

    def test_usd_to_eur_conversion(self):
        usd = USD(100)
        eur = CurrencyConverter.convert(usd, 'EUR')
        self.assertEqual(eur.get_amount(), 85)
        self.assertEqual(str(eur), "85 EUR")

    def test_eur_to_gbp_conversion(self):
        eur = EUR(85)
        gbp = CurrencyConverter.convert(eur, 'GBP')
        # 85 * 0.88 = 74.8, rounded to 75
        self.assertEqual(gbp.get_amount(), 74.8)
        self.assertEqual(str(gbp), "74.8 GBP")

    def test_gbp_to_usd_conversion(self):
        gbp = GBP(75)
        usd = CurrencyConverter.convert(gbp, 'USD')
        # 75 * 1.33 = 99.75, rounded to 100
        self.assertEqual(usd.get_amount(), 99.75)
        self.assertEqual(str(usd), "99.75 USD")

    def test_add_usd(self):
        usd1 = USD(100)
        usd2 = USD(50)
        added_usd = CurrencyOperations.add(usd1, usd2)
        self.assertEqual(added_usd.get_amount(), 150)
        self.assertEqual(str(added_usd), "150 USD")

    def test_subtract_usd(self):
        usd1 = USD(100)
        usd2 = USD(30)
        subtracted_usd = CurrencyOperations.subtract(usd1, usd2)
        self.assertEqual(subtracted_usd.get_amount(), 70)
        self.assertEqual(str(subtracted_usd), "70 USD")

    def test_negative_amount_error(self):
        with self.assertRaises(ValueError):
            USD(-100)

    def test_different_currency_addition(self):
        usd = USD(100)
        eur = EUR(85)
        with self.assertRaises(ValueError):
            CurrencyOperations.add(usd, eur)

    def test_different_currency_subtraction(self):
        usd = USD(100)
        eur = EUR(85)
        with self.assertRaises(ValueError):
            CurrencyOperations.subtract(usd, eur)


if __name__ == '__main__':
    unittest.main()
