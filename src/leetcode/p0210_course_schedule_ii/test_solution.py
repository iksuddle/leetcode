from leetcode.p0210_course_schedule_ii import solution


def assert_valid_order(num_courses, prerequisites, order):
    assert len(order) == num_courses
    assert set(order) == set(range(num_courses))

    positions = {course: position for position, course in enumerate(order)}
    for course, prerequisite in prerequisites:
        assert positions[prerequisite] < positions[course]


def test_no_prerequisites():
    order = solution.Solution().findOrder(3, [])

    assert_valid_order(3, [], order)


def test_single_prerequisite():
    prerequisites = [[1, 0]]
    order = solution.Solution().findOrder(2, prerequisites)

    assert_valid_order(2, prerequisites, order)


def test_multiple_valid_orders():
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    order = solution.Solution().findOrder(4, prerequisites)

    assert_valid_order(4, prerequisites, order)


def test_disconnected_dependencies():
    prerequisites = [[1, 0], [3, 2]]
    order = solution.Solution().findOrder(5, prerequisites)

    assert_valid_order(5, prerequisites, order)


def test_cycle_returns_empty_order():
    prerequisites = [[1, 0], [0, 1]]

    assert solution.Solution().findOrder(2, prerequisites) == []


def test_cycle_in_disconnected_component_returns_empty_order():
    prerequisites = [[1, 0], [3, 2], [4, 3], [2, 4]]

    assert solution.Solution().findOrder(5, prerequisites) == []


def test_course_is_its_own_prerequisite():
    assert solution.Solution().findOrder(1, [[0, 0]]) == []
