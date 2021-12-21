//백준 1260번 문제, DBF,BFS 구하기
#include<iostream>
#include<list>
#include<vector>
#include<stack>
#include<functional>
#include<queue>
#include<algorithm>
using namespace std;

class Graph{
    int V;
    vector<int>* adj;
    void DFS(int v, bool visisted[]);

public:
    Graph(int a){
        V=a;
        adj = new vector<int>[V];
    }
    void addEdge(int v, int w){ adj[v].push_back(w); adj[w].push_back(v); }
    void listSort();
    void BFS(int s);
    void topologicalSort(int s);
};

void Graph::listSort(){
    for(int i = 0; i < V; i++){
        sort(adj[i].begin(),adj[i].end());
    }
}

void Graph::DFS(int v, bool visited[]){
    visited[v] = true;
    vector<int>::iterator i;
    cout << v+1 << " ";
    for(i = adj[v].begin(); i != adj[v].end(); ++i){
        if (!visited[*i]){
            DFS(*i, visited);
        }
    }
}
void Graph::topologicalSort(int s){
    bool *visited = new bool[V];
    for(int i= 0; i < V; i++){
        visited[i] = false;
    }
    DFS(s, visited);
}

void Graph::BFS(int s){
    bool *visited = new bool[V];
    for(int i= 0; i < V; i++){
        visited[i] = false;
    }
    list<int> queue;
    visited[s] = true;
    queue.push_back(s);

    vector<int>::iterator i;
    while(!queue.empty()){
        s = queue.front();
        cout << s + 1 << " ";
        queue.pop_front();

        for(i = adj[s].begin(); i != adj[s].end(); ++i){
            if(!visited[*i]){
                visited[*i] = true;
                queue.push_back(*i);
            }
        }
    }
}

int main(){
    int x, y, start, n, m;
    cin >> n >> m >> start;
    Graph g(n);
    start -= 1;
    for(int i = 0; i < m; i++){
        cin >> x >> y;
        x -= 1;
        y -= 1;
        g.addEdge(x,y);
    }
    g.listSort();
    g.topologicalSort(start);
    cout << "\n";
    g.BFS(start);
    return 0;
}
