//
//  main.cpp
//  MICEMAZE
//
//  Created by StOrM on 7/9/14.
//  Copyright (c) 2014 SPOJ. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;

int arr[110][110];
int visited[110];
int dist[110];
int N, E, T, M;
int res = 0;

void bfs(int start)
{
    
    res++;
    queue<int> q;
    q.push(start);
    int current;
    while(T--)
    {
        current = q.front();
        q.pop();
        visited[current]=1;
        for(int i=0; i<110; i++)
        {
            if ((arr[current][i] != -1) && (arr[current][i] <= (T+1)) && (visited[i]==0))
            {
                q.push(i);
                res++;
                visited[i] = 1;
                
            }
        }
    }
}

int main(int argc, const char * argv[])
{
    memset(visited, 0, sizeof(visited));
    memset(dist, INT_MAX, sizeof(dist));
    memset(arr, -1, sizeof(arr));
    
    cin >> N >> E >> T >> M;
    int src, dest, dist;
    while(M--)
    {
        
        cin >> src >> dest >> dist;
        arr[--src][--dest] = dist;
    }
    
    bfs(E-1);

    cout << res << endl;
}

