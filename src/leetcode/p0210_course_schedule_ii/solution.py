from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # dependency map
        pre = defaultdict(list)
        for a, b in prerequisites:
            pre[a].append(b)

        path, checked = set(), set()
        result = []

        # checks if a cycle is found
        def check_cycle(n):
            if n in path:
                return True

            if n in checked:
                return False

            path.add(n)

            for p in pre[n]:
                if check_cycle(p):
                    return True

            path.remove(n)
            checked.add(n)

            result.append(n)

            return False

        for c in range(numCourses):
            if check_cycle(c):
                return []


        return result
