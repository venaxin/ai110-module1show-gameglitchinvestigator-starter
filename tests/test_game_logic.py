from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score

# ── check_guess ──────────────────────────────────────────────────────────────

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_winning_guess_returns_correct_message():
    outcome, message = check_guess(50, 50)
    assert "Correct" in message

def test_too_high_returns_higher_message():
    outcome, message = check_guess(80, 50)
    assert "HIGHER" in message

def test_too_low_returns_lower_message():
    outcome, message = check_guess(10, 50)
    assert "LOWER" in message

def test_guess_boundary_low():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

def test_guess_boundary_high():
    outcome, _ = check_guess(100, 100)
    assert outcome == "Win"

def test_guess_one_below_secret():
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"

def test_guess_one_above_secret():
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"

def test_check_guess_string_secret_win():
    # On even attempts, secret is passed as string
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win"

def test_check_guess_string_secret_too_high():
    outcome, _ = check_guess(60, "50")
    assert outcome == "Too High"

def test_check_guess_string_secret_too_low():
    outcome, _ = check_guess(40, "50")
    assert outcome == "Too Low"


# ── parse_guess ───────────────────────────────────────────────────────────────

def test_parse_valid_integer():
    ok, value, err = parse_guess("50")
    assert ok is True
    assert value == 50
    assert err is None

def test_parse_none_input():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_float_rejected():
    ok, value, err = parse_guess("100.1")
    assert ok is False
    assert value is None

def test_parse_float_whole_number_rejected():
    # 100.0 should also be rejected since it contains a decimal point
    ok, value, err = parse_guess("100.0")
    assert ok is False

def test_parse_letters_rejected():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None

def test_parse_mixed_input_rejected():
    ok, value, err = parse_guess("50abc")
    assert ok is False

def test_parse_negative_number():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5

def test_parse_large_number():
    ok, value, err = parse_guess("9999")
    assert ok is True
    assert value == 9999

def test_parse_returns_int_not_string():
    ok, value, err = parse_guess("42")
    assert isinstance(value, int)


# ── get_range_for_difficulty ──────────────────────────────────────────────────

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

def test_unknown_difficulty_defaults_to_normal():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100

def test_easy_range_is_smaller_than_normal():
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert easy_high < normal_high

def test_hard_range_is_smaller_than_normal():
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high < normal_high


# ── update_score ──────────────────────────────────────────────────────────────

def test_win_increases_score():
    new_score = update_score(0, "Win", 1)
    assert new_score > 0

def test_win_earlier_attempt_gives_more_points():
    score_attempt_1 = update_score(0, "Win", 1)
    score_attempt_5 = update_score(0, "Win", 5)
    assert score_attempt_1 > score_attempt_5

def test_win_score_minimum_10_points():
    # Even on a very late attempt, win should give at least 10 points
    new_score = update_score(0, "Win", 100)
    assert new_score >= 10

def test_too_high_even_attempt_adds_points():
    new_score = update_score(0, "Too High", 2)
    assert new_score == 5

def test_too_high_odd_attempt_subtracts_points():
    new_score = update_score(10, "Too High", 1)
    assert new_score == 5

def test_too_low_subtracts_points():
    new_score = update_score(10, "Too Low", 1)
    assert new_score == 5

def test_unknown_outcome_score_unchanged():
    new_score = update_score(50, "Unknown", 1)
    assert new_score == 50

def test_score_starts_from_existing_value():
    new_score = update_score(100, "Win", 1)
    assert new_score > 100
