import pytest
from file import add_numbers  # Remplacez par le chemin de votre fichier si nécessaire.


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 5, 8),          # Test avec deux nombres positifs
        (-3, -5, -8),       # Test avec deux nombres négatifs
        (10, -4, 6),        # Test avec un positif et un négatif
        (0, 7, 7),          # Test avec zéro comme premier nombre
        (7, 0, 7),          # Test avec zéro comme deuxième nombre
        (2.5, 3.1, 5.6),    # Test avec deux nombres à virgule flottante
    ]
)
def test_add_numbers(a, b, expected):
    assert add_numbers(a, b) == pytest.approx(expected)


# if __name__ == "__main__":
#     pytest.main()