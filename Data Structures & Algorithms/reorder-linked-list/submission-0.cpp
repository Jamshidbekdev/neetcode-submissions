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
    void reorderList(ListNode* head) {
        ListNode* temp = head;

        ListNode* fast = head->next;
        ListNode* slow = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* secondPiece = slow->next;
        slow->next = nullptr;

        ListNode* next = nullptr;
        ListNode* prev = nullptr;

        while (secondPiece) {
            next = secondPiece->next;
            secondPiece->next = prev;
            prev = secondPiece;
            secondPiece = next;
        }

        ListNode* firstPiece = head;
        secondPiece = prev; 

        while(secondPiece) {
            ListNode* temp1 = firstPiece->next;
            ListNode* temp2 = secondPiece->next;

            firstPiece->next = secondPiece;
            secondPiece->next = temp1;
            firstPiece = temp1;
            secondPiece = temp2;
        }
    }
};
