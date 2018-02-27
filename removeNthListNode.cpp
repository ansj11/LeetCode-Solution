/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* preHead = new ListNode(0);
        preHead->next = head;
        int length  = 0;
        ListNode* first = head;
        while (first != nullptr) {
            length++;
            first = first->next;
        }
        length -= n;
        first = preHead;
        while (length > 0) {
            length--;
            first = first->next;
        }
        first->next = first->next->next;
        return preHead->next;
    }
};