/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
struct ListNode {
      int val;
     struct ListNode *next;
 };
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode* head = list1->val <= list2->val? list1 : list2;
    
    if (list1 == NULL)
    {
        return list2;
    }
    else if (list2 == NULL)
    {
        return list1;
    }else if (list1->val < list2->val)
    {
        head->next = mergeTwoLists(list1->next,list2);
    }else
    {
        head->next = mergeTwoLists(list1,list2->next);        
    }

    
    
    
    
}
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    if (list1 == NULL)
    {
        return list2;
    }
    if (list2 == NULL)
    {
        return list1;
    }
    struct ListNode* head = list1->val <= list2->val? list1 : list2;
    if (list1->val < list2->val)
    {
        head->next = mergeTwoLists(list1->next,list2);
    }else
    {
        head->next = mergeTwoLists(list1,list2->next);        
    }
    return head;
}