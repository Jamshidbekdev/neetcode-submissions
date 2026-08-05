/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    int lengthOfListNode (ListNode* head) {
        int cnt = 0;

        while(head) {
            cnt++;
            head = head->next;
        }

        return cnt;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int length = lengthOfListNode(head);
        int nth = length - n;

        if (head == nullptr) return head;

        if (nth == 0 && head) return head->next;

        int cnt = 0;
        ListNode* temp = head;

        while (temp) {
            if (cnt == nth - 1) {
                temp->next = temp->next->next;
            }
            cnt++;
            temp = temp->next;
        }

        return head;

    }
};
