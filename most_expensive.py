prices = {
    "apple" : 3 ,
    "banana" : 2 ,
    "milk" : 5 ,
    "bread" : 4 ,
    "egg" : 2
}
most_expensive_thing = "apple"
most_expensive_price = prices["apple"]
for thing, price in prices.items():
    if price > most_expensive_price:
        most_expensive_thing = thing
        most_expensive_price = price
print("most expencive:", most_expensive_thing)
print("price:", most_expensive_price)