#include<iostream>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;

class Shark{
private:
    int N, size, eating, nowX, nowY, line;
    int **map;
    bool **visited;
public:
    Shark(int n){
        N = n;
        size = 2, eating = 0;
    }
    void input();
    bool bfs(int x, int y);
    void answer();
};

void Shark::input(){
    int temp;
    map = new int*[N];
    for(int i = 0; i < N; i++){
        map[i] = new int[N];
        for(int j = 0; j < N; j++){
            cin >> temp;
            map[i][j] = temp;
            if(temp == 9){
                nowX = i, nowY = j;
            }
        }
    }
}

bool Shark::bfs(int x, int y){
    int firstX = x, firstY = y;
    visited = new bool*[N];
    for(int i = 0; i < N; i++){
        visited[i] = new bool[N]{false};
    }
    int dx[4] = {-1,0,0,1};
    int dy[4] = {0,-1,1,0};
    queue<pair<int,pair<int,int>>> q; //거리,좌표 q에 저장
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
    //이동가능한 위치들 우선순위 큐에 저장->오름차순이라 맨앞이 가장 위면서 가장 왼쪽 좌표
    q.push(make_pair(0,make_pair(x,y)));
    visited[x][y] = true;
    map[x][y] = 0;
    int temp = -1;
    while(!q.empty()){
        int nX = q.front().second.first;
        int nY = q.front().second.second;
        int dis = q.front().first;
        if(dis == temp){
            break;
        }
        q.pop();
        for(int i = 0; i < 4; i++){
            int nextX = nX + dx[i];
            int nextY = nY + dy[i];
            if(nextX >= 0 && nextX < N && nextY >= 0 && nextY < N && map[nextX][nextY] <= size && !visited[nextX][nextY]){
                if(map[nextX][nextY] == 0 || map[nextX][nextY] == size){
                    q.push(make_pair(dis+1,make_pair(nextX,nextY)));
                    visited[nextX][nextY] = true;
                }
                else{
                    visited[nextX][nextY] = true;
                    if(temp == -1){
                        temp = dis+1;
                    }
                    pq.push(make_pair(nextX,nextY));
                    q.push(make_pair(dis+1,make_pair(nextX,nextY)));
                }
            }
        }
    }
    if(pq.size() == 0){
        return false;
    }
    else{
        eating += 1;
        if(size == eating){
            eating = 0;
            size += 1;
        }
        nowX = pq.top().first, nowY = pq.top().second;
        line = temp;
        return true;
    }
}

void Shark::answer(){
    int answerNum = 0;
    while(bfs(nowX,nowY)){
        answerNum += line;
    }
    cout << answerNum << "\n";
}

int main(){
    cin.tie(NULL); cout.tie(NULL);
    ios::sync_with_stdio(false);
    int inputNum;
    cin >> inputNum;
    Shark s(inputNum);
    s.input();
    s.answer();
    return 0;
}