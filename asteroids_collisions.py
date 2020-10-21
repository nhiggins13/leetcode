class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left_index = 0

        while (left_index < len(asteroids) - 1):
            right_index = left_index + 1
            a_left = asteroids[left_index]
            a_right = asteroids[right_index]

            if a_left < 0:
                left_index += 1
            else:
                if a_right < 0:
                    if abs(a_left) == abs(a_right):
                        asteroids.pop(right_index)
                        asteroids.pop(left_index)
                        left_index = max(0, left_index - 1)
                    elif abs(a_left) > abs(a_right):
                        asteroids.pop(right_index)
                    else:
                        asteroids.pop(left_index)
                        left_index = max(0, left_index - 1)
                else:
                    left_index += 1

        return asteroids