#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int blue = 0, white = 0;

void cutting(int **paper, int num, int startX,int startY){
    int check = paper[startX][startY];
    for(int i = startX; i < startX + num; i++){
        for(int j = startY; j < startY + num; j++){
            if(paper[i][j] != check){
                cutting(paper,num/2,startX,startY);
                cutting(paper,num/2,startX+num/2,startY);
                cutting(paper,num/2,startX,startY+num/2);
                cutting(paper,num/2,startX+num/2,startY+num/2);
                return;
            }
        }
    }
    if(check == 1){
        blue += 1;
    }
    else{
        white += 1;
    }
    return;
}

int main(){
    cin.tie(NULL); cout.tie(NULL);
    ios::sync_with_stdio(false);
    int n;
    cin >> n;
    int **paper = new int*[n];
    for(int i = 0; i < n; i++){
        paper[i] = new int[n];
        for(int j = 0; j < n; j++){
            cin >> paper[i][j];
        }
    }
    cutting(paper,n,0,0);
    cout << white << "\n" << blue << "\n";
    return 0;
}