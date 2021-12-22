#include<iostream>
#include<string>
#include<queue>
using namespace std;

class Matrix{
    int X, Y;
    int **mat, **dis;
    int dx[4] = {1,0,-1,0};
    int dy[4] = {0,1,0,-1};
public:
    Matrix(){}
    void make(int a, int b){
        X = a; Y = b;
        mat = new int*[X]; // 1 = 이동가능, 0 = 벽
        dis = new int*[X];
        for(int i = 0; i < X; i++){
            mat[i] = new int[Y];
            dis[i] = new int[Y];
            string number;
            cin >> number;
            for(int j = 0; j < number.size(); j++){
                mat[i][j] = number[j] - '0';
                dis[i][j] = 0;
            }
        }
    }
    void BFS(int x, int y);
    int answerNum(){ return dis[X-1][Y-1]; }
};

void Matrix::BFS(int x, int y){
    bool **visited = new bool*[X];
    for(int i = 0; i < X; i++){
        visited[i] = new bool[Y];
        for(int j = 0; j < Y; j++){
            visited[i][j] = false;
        }
    }
    visited[x][y] = true;
    queue<pair<int, int>> q;
    dis[x][y] = 1;
    q.push(make_pair(x,y));

    while(!q.empty()){
        int x1 = q.front().first;
        int y1 = q.front().second;

        q.pop();

        for(int i = 0; i < 4; i++){
            int nextX = x1 + dx[i];
            int nextY = y1 + dy[i];

            if(0 <= nextX && nextX < X && 0 <= nextY && nextY < Y){
                if(mat[nextX][nextY] == 1 && visited[nextX][nextY] == false){
                    dis[nextX][nextY] = dis[x1][y1] + 1;
                    visited[nextX][nextY] = true;
                    q.push(make_pair(nextX,nextY));
                }
            }
        }
    }
}

int main(){
    int n, m;
    cin >> n >> m;
    Matrix mat;
    mat.make(n,m);
    mat.BFS(0,0);
    cout << mat.answerNum() << endl;;
    return 0;
}