class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1, nums2 = [], []

        # l1, l2를 문자로 nums1, nums2에 삽입
        while l1 != None:
            nums1.append(str(l1.val))
            l1 = l1.next

        while l2 != None:
            nums2.append(str(l2.val))
            l2 = l2.next

        # 배열을 거꾸로 문자열로 변환
        nums1 = ''.join(nums1[::-1])
        nums2 = ''.join(nums2[::-1])

        # int로 변환 후, 합계 계산 및 배열로 변환
        sum = int(nums1) + int(nums2)
        arr = [x for x in str(sum)]

        # 반환할 ListNode생성
        result_head = ListNode()
        tail = result_head

        # 거꾸로 값을 할당해서 넣기위한 for문
        for i in range(len(arr)-1, -1, -1):
            tail.next = ListNode(int(arr[i]))
            tail = tail.next
        
        return result_head.next
