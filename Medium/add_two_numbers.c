#include <stdio.h>
#include <stdlib.h>
//   Definition for singly-linked list.
struct ListNode {
      int val;
      struct ListNode *next;
};


//21.48%
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* cur = malloc(sizeof(struct ListNode));
    struct ListNode* ptr = cur;
    ptr->val = 0;
    ptr->next = NULL;
    int carry = 0;
    while (l1 != NULL || l2 != NULL || carry != 0)
    {
        int a = (l1 == NULL) ? 0 : l1->val;
        int b = (l2 == NULL) ? 0 : l2->val;
        ptr->val = a + b + carry;
        carry = ptr->val / 10;
        ptr->val = ptr->val %10;

        if (l1 != NULL)
        {
            l1 = (l1->next ==NULL)? NULL: l1->next;
        }
        if (l2 != NULL)
        {
           l2 = (l2->next ==NULL)? NULL: l2->next;
        }
        if(l1 != NULL || l2!=NULL || carry !=0){
            ptr->next = malloc(sizeof(struct ListNode));
            ptr->next->next=NULL;
            ptr = ptr->next;
        }
    }
    return cur;
}

//23.84%

struct ListNode* getNewNode(int val) {
    struct ListNode* newNode = (struct ListNode*) malloc(sizeof(struct ListNode));
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* result = getNewNode(0);
    struct ListNode* resCurr = result;
    int carry = 0;
    
    while (l1 || l2 || carry) {
        if (l1) {
            carry += l1->val;
            l1 = l1->next;
        }
        if (l2) {
            carry += l2->val;
            l2 = l2->next;
        }
        
        resCurr->next = getNewNode(carry % 10);
        resCurr = resCurr->next;
        
        carry = carry / 10;
    }
    
    return result->next;
}