from leetcode.p0359_logger_rate_limiter import solution


def test_first_message_is_printed():
    logger = solution.Logger()

    assert logger.shouldPrintMessage(1, "foo") is True


def test_message_is_suppressed_during_ten_second_window():
    logger = solution.Logger()

    assert logger.shouldPrintMessage(1, "foo") is True
    assert logger.shouldPrintMessage(2, "foo") is False
    assert logger.shouldPrintMessage(10, "foo") is False


def test_message_is_printed_at_exact_boundary():
    logger = solution.Logger()

    assert logger.shouldPrintMessage(1, "foo") is True
    assert logger.shouldPrintMessage(11, "foo") is True


def test_messages_have_independent_rate_limits():
    logger = solution.Logger()

    assert logger.shouldPrintMessage(1, "foo") is True
    assert logger.shouldPrintMessage(2, "bar") is True
    assert logger.shouldPrintMessage(3, "foo") is False
    assert logger.shouldPrintMessage(8, "bar") is False
    assert logger.shouldPrintMessage(11, "foo") is True
    assert logger.shouldPrintMessage(12, "bar") is True


def test_suppressed_message_does_not_restart_window():
    logger = solution.Logger()

    assert logger.shouldPrintMessage(1, "foo") is True
    assert logger.shouldPrintMessage(5, "foo") is False
    assert logger.shouldPrintMessage(10, "foo") is False
    assert logger.shouldPrintMessage(11, "foo") is True


def test_duplicate_at_same_timestamp_is_suppressed():
    logger = solution.Logger()

    assert logger.shouldPrintMessage(5, "foo") is True
    assert logger.shouldPrintMessage(5, "foo") is False
    assert logger.shouldPrintMessage(5, "bar") is True


def test_successful_print_starts_a_new_window():
    logger = solution.Logger()

    assert logger.shouldPrintMessage(1, "foo") is True
    assert logger.shouldPrintMessage(11, "foo") is True
    assert logger.shouldPrintMessage(20, "foo") is False
    assert logger.shouldPrintMessage(21, "foo") is True
