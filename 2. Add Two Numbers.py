# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def parseLink(self,list):
        temp=list
        count=0
        listRealNumber=0
        while(temp):
            powLevel= pow(10,count)
            listRealNumber = listRealNumber + powLevel*temp.val
            count+=1
            temp=temp.next
        return listRealNumber

    def i2l(self,val:int):
        valsplit = [int(i) for i in str(val)]
        valsplit =  valsplit[::-1] #array reverse
        return valsplit


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1Val = self.parseLink(l1)
        l2Val = self.parseLink(l2)
        tSum = l1Val + l2Val
        ans = self.i2l(tSum)
        return (ans)