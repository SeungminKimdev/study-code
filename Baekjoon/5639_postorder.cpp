#include<iostream>
using namespace std;

struct node{
    int number;
    struct node *left, *right;
};

struct node *newNode(int n){
    struct node *temp = new node;
    temp->number = n;
    temp->left = temp->right = NULL;
    return temp;
}

struct node *insert(struct node *node, int n){
    if(node == NULL){
        return newNode(n);
    }

    if(n < node->number){
        node->left = insert(node->left, n);
    }
    else{
        node->right = insert(node->right, n);
    }
    return node;
}

void postorder(struct node *node){
    if(node){
        postorder(node->left);
        postorder(node->right);
        cout << node->number << "\n";
    }
}

int main(){
    int num;
    struct node *head = NULL;
    while(cin >> num){
        head = insert(head,num);
    }
    postorder(head);
    return 0;
}