class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 결과값 배열 선언
        result = []

        # 0 ~ len개수 조합
        # itertools의 combinations 사용하여 담기
        for i in range(len(nums)+1):
            result += list(itertools.combinations(nums,i))
 
        return result