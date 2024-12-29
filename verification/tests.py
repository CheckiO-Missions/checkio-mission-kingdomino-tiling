"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [0, 0],
            "answer": 192,
        },
        {
            "input": [0, 1],
            "answer": 0,
        },
        {
            "input": [0, 2],
            "answer": 192,
        },
        {
            "input": [1, 1],
            "answer": 112,
        },
        {
            "input": [1, 2],
            "answer": 0,
        },
        {
            "input": [2, 2],
            "answer": 196,
        },
    ],
    "Extra": [
        {
            "input": [2, 3],
            "answer": 0,
        },
        {
            "input": [3, 2],
            "answer": 0,
        },
        {
            "input": [3, 3],
            "answer": 112,
        },
        {
            "input": [4, 4],
            "answer": 192,
        },
    ]
}
