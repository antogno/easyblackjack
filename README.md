# EasyBlackjack

<p>
    <a href="https://github.com/antogno/easyblackjack/blob/master/LICENSE"><img src="https://img.shields.io/github/license/antogno/easyblackjack" alt="License"></a>
    <a href="https://github.com/antogno/easyblackjack/commits"><img src="https://img.shields.io/github/last-commit/antogno/easyblackjack" alt="Last commit"></a>
    <a href="https://github.com/antogno/easyblackjack/releases/latest"><img src="https://img.shields.io/github/v/tag/antogno/easyblackjack?label=last%20release" alt="Last release"></a>
</p>

EasyBlackjack is a Single-Deck Blackjack hand generator and calculator.

---

## Installation

Use the package manager [Pip](https://pip.pypa.io/en/stable/) to install EasyBlackjack.

```console
$ pip install EasyBlackjack
```

## Usage

```python
from easyblackjack import EasyBlackjack
```

```python
EasyBlackjack.generate_cards()
# Returns two random cards with their value.
# For example:
# {
#     'card_one': {
#         'value': '10',
#         'suit': 'H'
#     },
#     'card_two': {
#         'value': '4',
#         'suit': 'S'
#     },
#     'points': 14
# }
```

```python
EasyBlackjack.calculate_points(['A', '6', '3'])
# Returns the hand value.
# For example:
# 20
```

## License

EasyBlackjack is licensed under the terms of the [Creative Commons Zero v1.0 Universal license](https://github.com/antogno/easyblackjack/blob/master/LICENSE).

For more information, see the [Creative Commons website](https://creativecommons.org/publicdomain/zero/1.0/).
