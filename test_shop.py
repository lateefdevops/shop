from shop import products, wishlist, search
assert len(products()) == 2, "products broken"
assert wishlist() == ["shirt"], "wish list should contain 1 item"
assert search("SHIRT") == ["shirt"], "search should ignore case"
print("all tests passed")
