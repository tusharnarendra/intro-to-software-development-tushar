def find_average(numbers):
    return sum(numbers)/len(numbers)


def gardners_equation(velocity: float) -> float:
    """Calculate bulk density from P-wave velocity using Gardner's equation.

    Args:
        velocity

    Returns:
        Bulk density

    Raises:
        ValueError
    """
    
    if velocity < 0:
        raise ValueError("Velocity cannot be negative")

    return 0.31 * velocity**0.25


def inverse_gardners_equation(density: float) -> float:
    if density < 0:
        raise ValueError("Density cannot be negative")

    return (density / 0.31) ** 4
