"""
Program 3: Positive, Negative, or Zero
Classify a number as Positive, Negative, or Zero.
"""


def classify_number(number):
    """Return 'Positive', 'Negative', or 'Zero' based on the input number."""
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


if __name__ == "__main__":
    print(classify_number(5))   # Positive
    print(classify_number(-3))  # Negative
    print(classify_number(0))   # Zero
