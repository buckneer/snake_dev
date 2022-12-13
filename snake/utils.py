

def generate_letters(x, y, width=50, height=100):

    return \
    {
        "a": [
            {"break": {"x": x, "y": y}},
            {"draw": {"x": x + (width / 2), "y": y + height}},
            {"draw": {"x": x + width, "y": y}},
            {"break": {"x": x + (width * 0.8), "y": y + (height * 0.4)}},
            {"draw": {"x": x + (width * 0.2), "y": y + (height * 0.4)}},
            {"break": {"x": x + (width * 1.1),  "y": y}},
            {"draw": {"x": x + (width * 0.9), "y": y}},
            {"break": {"x": x - (width * 0.1), "y": y}},
            {"draw": {"x": x + (width * 0.1), "y": y}},
        ],
        "b": [
            {"break": {"x": x, "y": y}},
            {"draw": {"x": x, "y": y + height}},
            {"draw": {"x": x + width, "y": y + height}},
            {"draw": {"x": x + width, "y": y + (height * 0.9)}},
            {"break": {"x": x, "y": y + (height / 2)}},
            {"draw": {"x": x + (width / 2), "y": y + (height / 2)}},
            {"break": {"x": x, "y": y}},
            {"draw": {"x": x + (width / 2), "y": y}},
            {"circle": {"radius": (width / 2), "angle": 182}},
        ]
    }