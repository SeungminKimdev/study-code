#include<iostream>
#include<vector>
using namespace std;

void merge(vector<int> &list, int left, int mid, int right, vector<int> &sorted){
    int i = left;
    int j = mid + 1;
    int k = left;

    while(i <= mid && j <= right){
        if(list[i] <= list[j]){
            sorted[k++] = list[i++];
        }
        else{
            sorted[k++] = list[j++];
        }
    }

    if(i > mid){
        for(int l = j; l <= right; l++){
            sorted[k++] = list[l];
        }
    }
    else{
        for(int l = i; l <= mid; l++){
            sorted[k++] = list[l];
        }
    }

    for(int l = left; l<=right; l++){
        list[l] = sorted[l];
    }
}

void mergeSort(vector<int> &list, int left, int right, vector<int> &sorted){
    int mid;
    if(left < right){
        mid = (left + right) / 2;
        mergeSort(list,left,mid,sorted);
        mergeSort(list,mid+1, right,sorted);
        merge(list, left, mid, right,sorted);
    }
}

int main(){
    int n, num;
    cin >> n;
    vector<int> list;
    vector<int> sorted(n);
    for(int i = 0; i < n; i++){
        cin >> num;
        list.push_back(num);
    }
    int listSize = list.size();
    mergeSort(list,0,listSize-1,sorted);
    for(int i = 0; i < listSize; i++){
        cout << sorted[i] << "\n";
    }
    return 0;
}