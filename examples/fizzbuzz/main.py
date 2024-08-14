from auto_impl import auto

@auto("""
Return fizz if the number is divisible by 3, buzz if the number is divisible by 5, 
and fizzbuzz if the number is divisible by both 3 and 5. Otherwise, just return
the number itself.
""", model="groq-llama3.1-70b")
def fizzbuzz(n: int) -> str:
    pass

def test_fizzbuzz():
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(15) == "fizzbuzz"
    assert fizzbuzz(1) == "1"

test_fizzbuzz() # Doesn't raise exceptions