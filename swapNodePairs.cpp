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
    ListNode* swapPairs(ListNode* head) {
        ListNode* p = head;
        int t;
        while(p && p->next){
            t = p->val;
            p->val = p->next->val;
            p->next->val = t;
            p = p->next->next;
        }
        return head;
    }
};