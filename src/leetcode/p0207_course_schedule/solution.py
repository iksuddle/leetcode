# course schedule


from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        prerequisites contains [a, b], indicating you must take b before a
        """
        pre = defaultdict(list)
        for a, b in prerequisites:
            pre[a].append(b)

        taken = set()
        checked = set()

        # checks if a cycle is found
        def check_cycle(n):
            if n in taken:
                return True

            if n in checked:
                return False

            taken.add(n)

            for p in pre[n]:
                if check_cycle(p):
                    return True

            taken.remove(n)
            checked.add(n)

            return False

        for c in range(numCourses):
            if check_cycle(c):
                return False

        return True
