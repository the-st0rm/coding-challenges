//
//  main.cpp
//  AGGRCOW
//
//  Created by StOrM on 7/21/14.
//  Copyright (c) 2014 SPOJ. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


bool test_bin(vector<int> v, int N, int C, int Max_len)
{
    int j=0;
    int i=1;
    int n_cows = 1;
    if (n_cows==N)
    {
        return true;
    }
    while ((i <N) && (n_cows <C))
    {
        if (v[i]-v[j]<Max_len)
        {
            i++;
        }
        else
        {
            j=i;
            n_cows++;
            i++;
        }
    }
    return (n_cows==C);
}


int BinSearch(vector<int>v, int N, int C)
{
    int start =0;
    int end = v[N-1];
    while (start < end)
    {
        int mid;
        mid = (start+end)/2;
        if (test_bin(v, N, C, mid))
            start =mid+1;
        else
            end=mid;
    }
    return start-1;
}


int main(int argc, const char * argv[])
{

    
    int T;
    cin >> T;
    while (T)
    {
        int N, C;
        cin >> N >> C;
        vector<int> v;
        v.resize(N);
        for(int i=0; i<N;i++)
        {
            cin >> v[i];
        }
        sort(v.begin(), v.end());
        
        cout << BinSearch(v, N, C) << endl;
        
        T--;
    }
    return 0;
}

