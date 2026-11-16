from shop import products, wishlist
assert len(products()) == 2, "products broken"
assert wishlist() == ["shirt"], "wish list should contain 1 item"
print("all tests passed")
