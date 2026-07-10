from engine.terrain.interpolation import lerp, smoothstep


def test_lerp_returns_start_value_when_t_is_zero() -> None:
    assert lerp(10.0, 20.0, 0.0) == 10.0


def test_lerp_returns_end_value_when_t_is_one() -> None:
    assert lerp(10.0, 20.0, 1.0) == 20.0


def test_lerp_returns_midpoint() -> None:
    assert lerp(10.0, 20.0, 0.5) == 15.0


def test_smoothstep_preserves_endpoints() -> None:
    assert smoothstep(0.0) == 0.0
    assert smoothstep(1.0) == 1.0


def test_smoothstep_is_symmetric_around_midpoint() -> None:
    assert smoothstep(0.5) == 0.5