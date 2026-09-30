from leetcode.p0207_course_schedule import solution


def test_no_prerequisites():
    assert solution.Solution().canFinish(3, []) is True


def test_single_prerequisite():
    assert solution.Solution().canFinish(2, [[1, 0]]) is True


def test_cycle():
    assert solution.Solution().canFinish(2, [[1, 0], [0, 1]]) is False


def test_long_dependency_chain():
    prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3]]

    assert solution.Solution().canFinish(5, prerequisites) is True


def test_cycle_in_disconnected_component():
    prerequisites = [[1, 0], [3, 2], [4, 3], [2, 4]]

    assert solution.Solution().canFinish(5, prerequisites) is False


def test_shared_prerequisite():
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

    assert solution.Solution().canFinish(4, prerequisites) is True


def test_course_is_its_own_prerequisite():
    assert solution.Solution().canFinish(1, [[0, 0]]) is False
