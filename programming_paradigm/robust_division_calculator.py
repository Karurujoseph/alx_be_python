# programming_paradigm/robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling division by zero and non-numeric inputs.

    Args:
        numerator: The dividend (string or numeric)
        denominator: The divisor (string or numeric)

    Returns:
        A message string indicating either the result or the type of error.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Perform division safely
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
