d = {
    "name": "Alice",
    "details": {"age": 25, "city": "New York"},
    "country": "USA"
}

has_nested = any(isinstance(v, dict) for v in d.values())

print( has_nested)
