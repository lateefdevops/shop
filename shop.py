def products():
    return ["shirt", "shoes"]

def wishlist():
    return ["shirt"]

def search(term):
    return [p for p in products() if term.lower() in p]
