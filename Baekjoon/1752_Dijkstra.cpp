//1752번 Dijkstra 알고리즘 사용
#include<iostream>
#include<list>
#include<vector>
#include<set>
using namespace std;
#define INF 999999999

class Graph{
    int V;
    list< pair<int, int> > *adj;
    vector<int> dist;
public:
    Graph(int v){
        V = v;
        adj = new list< pair<int, int> >[V];
        vector<int> dist2(V, INF);
        dist = dist2;
    }
    int ans(int n){ return dist[n]; }
    void addEdge(int u, int v, int w);
    void shortestPath(int s);
};

void Graph::addEdge(int u, int v, int w){
    adj[u].push_back(make_pair(v,w));
}

void Graph::shortestPath(int s){
    set< pair<int, int> > setds;
    setds.insert(make_pair(0,s));
    dist[s] = 0;

    while(!setds.empty()){
        pair<int,int>tmp = *(setds.begin());
        setds.erase(setds.begin());
        int u = tmp.second;

        list<pair<int,int>>::iterator i;
        for(i = adj[u].begin(); i != adj[u].end(); ++i){
            int v = (*i).first;
            int weight = (*i).second;

            if(dist[v] > dist[u] + weight){
                if(dist[v] != INF){
                    setds.erase(setds.find(make_pair(dist[v],v)));
                }
                dist[v] = dist[u] + weight;
                setds.insert(make_pair(dist[v],v));
            }
        }
    }
    
}

int main(){
    int node, line, start, u, v, w;
    cin >> node >> line >> start;
    Graph g(node);
    for(int i = 0; i < line; i++){
        cin >> u >> v >> w;
        g.addEdge(u-1, v-1, w);
    }
    g.shortestPath(start-1);
    for(int i = 0; i < node; i++){
        int ans = g.ans(i);
        if(ans == INF){
            cout << "INF\n";
        }
        else{
            cout << ans << "\n";
        }
    }
    return 0;
}