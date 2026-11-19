import pytest

from geometry import polygon_clip as mod

CASES = [
    ('clip_polygon', [[[0, 0], [2, 0], [2, 2], [0, 2]], [[-1, -1], [1, -1], [1, 1], [-1, 1]]], [[0.0, 1.0], [0, 0], [1.0, 0.0], [1.0, 1.0]], False),
    ('clip_polygon', [[[0, 0], [4, 0], [4, 4]], [[0, 0], [2, 0], [2, 2], [0, 2]]], [[2.0, 2.0], [0, 0], [2.0, 0.0]], False),
    ('polygon_area', [[[0, 0], [2, 0], [2, 2], [0, 2]]], 4.0, True),
    ('polygon_area', [[[0, 0], [0, 2], [2, 2], [2, 0]]], 4.0, True),
    ('point_in_polygon', [[1, 1], [[0, 0], [2, 0], [2, 2], [0, 2]]], True, False),
    ('point_in_polygon', [[3, 3], [[0, 0], [2, 0], [2, 2], [0, 2]]], False, False),
    ('ensure_ccw', [[[0, 0], [0, 2], [2, 2], [2, 0]]], [[2, 0], [2, 2], [0, 2], [0, 0]], False),
    ('triangulate', [[[0, 0], [2, 0], [2, 2], [0, 2]]], [[[0, 0], [2, 0], [2, 2]], [[0, 0], [2, 2], [0, 2]]], False),
    ('clip_polygon', [[[0, 0], [1, 0], [1, 1], [0, 1]], [[0, 0], [3, 0], [3, 3], [0, 3]]], [[0, 0], [1, 0], [1, 1], [0, 1]], False),
    ('polygon_area', [[[0, 0], [1, 0], [1, 1]]], 0.5, True),
    ('point_in_polygon', [[0, 0], [[0, 0], [2, 0], [2, 2], [0, 2]]], True, False),
    ('ensure_ccw', [[[0, 0], [2, 0], [2, 2]]], [[0, 0], [2, 0], [2, 2]], False),
    ('ensure_ccw', [[[0, 0], [2, 2], [2, 0]]], [[2, 0], [2, 2], [0, 0]], False),
    ('triangulate', [[[0, 0], [1, 0], [1, 1], [0, 1]]], [[[0, 0], [1, 0], [1, 1]], [[0, 0], [1, 1], [0, 1]]], False),
    ('triangulate', [[[0, 0], [2, 0], [2, 2]]], [[[0, 0], [2, 0], [2, 2]]], False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_polygon_clip_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
