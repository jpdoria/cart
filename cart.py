#!/usr/bin/env python


class ShoppingCart:
    def __init__(self):
        self.products = {
            'ult_small': [
                {
                    'name': 'Unlimited 1GB',
                    'price': 24.90
                }
            ],
            'ult_medium': [
                {
                    'name': 'Unlimited 2GB',
                    'price': 29.90
                }
            ],
            'ult_large': [
                {
                    'name': 'Unlimited 5GB',
                    'price': 44.90
                }
            ],
            '1gb': [
                {
                    'name': '1GB Data-pack',
                    'price': 9.90
                }
            ]
        }
        self.cart = {}

    def add(self, item, qty):
        """
        Add item to cart
        """
        try:
            name = self.products[item][0]['name']
            price = float('{:.2f}'.format(self.products[item][0]['price']))

            self.cart[item] = [{'price': price * qty, 'quantity': qty}]

            # Offers and promotions
            if item == 'ult_small' and qty == 3:
                new_price = '{:.2f}'.format(float(price) * 2)
                self.cart[item][0]['price'] = float(new_price)
            elif item == 'ult_large' and qty > 3:
                new_price = '{:.2f}'.format(39.90 * qty)
                self.cart[item][0]['price'] = float(new_price)
            elif item == 'ult_medium':
                self.cart[item][0]['freebie'] = '1 GB Data-pack'
                self.cart[item][0]['frbqty'] = qty
        except Exception:
            raise

    def total(self, promo_code=None):
        """
        Compute total and apply discount if there's a promo code
        """
        try:
            prices = [self.cart[key][0]['price'] for key in self.cart]

            if promo_code:
                total = sum(prices)
                new_total = total - (total * 0.10)

                print('PromoCode: {}'.format(promo_code))
                print('Discount: 10%')
                print('Total: ${:.2f}'.format(new_total))
            else:
                total = sum(prices)
                ult_medium = self.cart.get('ult_medium', None)

                if ult_medium:
                    freebie = self.cart['ult_medium'][0]['freebie']
                    frbqty = self.cart['ult_medium'][0]['frbqty']

                    print('Total: ${:.2f}'.format(total))
                    print('Freebie(s): {0} x {1}'.format(freebie, frbqty))
                else:
                    print('Total: ${:.2f}'.format(total))
        except Exception:
            raise

    def items(self):
        """
        Show cart
        """
        try:
            print('Cart:')
            for key in self.cart:
                name = self.products[key][0]['name']
                qty = self.cart[key][0]['quantity']

                print('- {0} x {1}'.format(name, qty))
        except Exception:
            raise


def main():
    # Feel free to edit this section
    cart = ShoppingCart()
    item1 = 'ult_small'
    item2 = '1gb'
    promo_code = 'I<3AMAYSIM'

    cart.add(item1, 1)
    cart.add(item2, 1)
    cart.total(promo_code)
    cart.items()


if __name__ == '__main__':
    main()
