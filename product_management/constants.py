class QuantityType:
    ADD = 0
    EXPIRED = 1
    INVENTORY = 2

    ACTION_CHOICES = (
        (ADD, 'Add quantity'),
        (EXPIRED, 'Expired quantity'),
        (INVENTORY, 'Inventory quantity')
    )

    QuantityType = dict(ACTION_CHOICES)


# class ProductChoice:
#
#     PRODUCT_CHOICE = (
#
#     )
#
#     PRODUCT_CHOICE_DICT = dict(PRODUCT_CHOICE)