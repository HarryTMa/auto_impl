# auto_impl

Automatically implements functions using ChatGPT.

## Install

    pip install curl_cffi --upgrade

## Usage

Get ChatGPT API key and set it to your environment variable `OPENAI_API_KEY` before run.

### @auto

Syntax:

```python
@auto($prompt)
$function
```

where `$prompt` is a prompt string literal, and `$function` is the target function.

Example:

```python
from auto_impl import auto


@auto("Return fizz if the number is divisible by 3, buzz if the number is divisible by 5, and fizzbuzz if the number is divisible by both 3 and 5.")
def fizzbuzz(n: int) -> str:
    pass


def test_fizzbuzz():
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(15) == "fizzbuzz"
    assert fizzbuzz(1) == "1"


test_fizzbuzz() # Doesn't raise exceptions
```

## Acknowledgement

- Idea originated from [retrage/gpt-macro](https://github.com/retrage/gpt-macro), which is under the MIT license.

## License

auto_impl is released under the MIT license.
