class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 번호별 문자정보 dic
        dic = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"
        }
        # 결과를 담을 배열
        result = []

        # 예외처리 : 빈문자열일 경우, 빈배열 return
        if not digits:
            return []


        def recur(idx, l):
            #재귀함수종료조건 //  len이 같으면 해당 마지막 dic[num]의 문자열 순서대로 삽입 및 반환
            if len(l) == len(digits):
                result.append(l)
                return
            
            # idx 옵션으로 2중 for을 돌려 dfs로 깊이 탐색 및 재귀함수 실행 
            for i in range(idx, len(digits)):
                for j in dic[digits[i]]:
                    recur(i+1, l + j)
        
        # 초기 재귀함수 시작점
        recur(0, "")

        return result
