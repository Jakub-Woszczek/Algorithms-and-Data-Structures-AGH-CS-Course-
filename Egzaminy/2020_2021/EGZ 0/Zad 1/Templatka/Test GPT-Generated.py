def tanagram(x, y, t):

    pass


def run_tests():
    tests = [
        # Testy podstawowe
        {
            "x": "kotomysz",
            "y": "tokmysoz",
            "t": 3,
            "expected": True
        },
        {
            "x": "kotomysz",
            "y": "tokmysoz",
            "t": 2,
            "expected": False
        },
        # Testy krawędziowe
        {
            "x": "a",
            "y": "a",
            "t": 0,
            "expected": True
        },
        {
            "x": "a",
            "y": "b",
            "t": 0,
            "expected": False
        },
        {
            "x": "abcde",
            "y": "edcba",
            "t": 4,
            "expected": True
        },
        {
            "x": "abcde",
            "y": "edcba",
            "t": 3,
            "expected": False
        },
        # Testy złożone
        {
            "x": "abcdefgh",
            "y": "hgfedcba",
            "t": 7,
            "expected": True
        },
        {
            "x": "abcdefgh",
            "y": "hgfedcba",
            "t": 6,
            "expected": False
        },
        {
            "x": "abcdefghij",
            "y": "jihgfedcba",
            "t": 9,
            "expected": True
        },
        {
            "x": "abcdefghij",
            "y": "jihgfedcba",
            "t": 8,
            "expected": False
        },
        # Testy dla dużych wartości t
        {
            "x": "abcdeabcdeabcdeabcde",
            "y": "edcbaedcbaedcbaedcba",
            "t": 19,
            "expected": True
        },
        {
            "x": "abcdeabcdeabcdeabcde",
            "y": "edcbaedcbaedcbaedcba",
            "t": 18,
            "expected": False
        },
    ]

    passed = 0
    for i, test in enumerate(tests):
        result = tanagram(test["x"], test["y"], test["t"])
        if result == test["expected"]:
            print(f"Test {i + 1} PASSED")
            passed += 1
        else:
            print(f"Test {i + 1} FAILED: expected {test['expected']}, got {result}")

    print(f"\nLiczba zaliczonych testów: {passed}/{len(tests)}")


if __name__ == "__main__":
    run_tests()
