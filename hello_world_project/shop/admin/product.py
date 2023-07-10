from shop.models.product import Product


def get_product_list():
    return Product.Model.list()