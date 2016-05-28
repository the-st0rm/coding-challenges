//
//  main.cpp
//  PIE
//
//  Created by StOrM on 7/21/14.
//  Copyright (c) 2014 SPOJ. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <cmath>
#define PI 3.14159265358
using namespace std;

inline double round( double val )
{
    if( val < 0 ) return ceil(val - 0.5);
    return floor(val + 0.5);
}

float calc_vol(float r)
{
    return PI * (r*r);
}

bool test_val(vector<float> v, float mid, int N, int F)
{
    int counter =0;
    int no_f =0;
    vector<float> v_copy;
    v_copy.resize(N);
    for(int i=0;i<N;i++)
    {
        v_copy[i]=v[i];
    }
    
    while ((counter < N) && (no_f!=F))
    {
        if (v_copy[counter]-mid >=0)
        {
            no_f++;
            v_copy[counter]-=mid;
        }
        else
        {
            counter++;
        }
    }
    
    return (no_f==F);
    
}


float BinSearch(vector<float> v, int N, int F)
{
    double end = *max_element(v.begin(), v.end());
    
    double start=0;
    double mid;
    while((start < end) && (int(start*1000000) != int(end*1000000)))
    {
        mid = (start+end)/2.0;
        if (test_val(v, mid, N, F+1))
        {
            start = mid + 0.0000001;
        }
        else
        {
            end = mid;
        }
    }

    return float(start);//-0.0000001;
    
}
int main(int argc, const char * argv[])
{
    int T;
    cin >> T;
    
    while (T)
    {
        int N;int F;
        cin >> N >> F;
        vector<float> v;
        v.resize(N);
        for(int i=0;i<N;i++)
        {
            float r;
            cin >> r;
            v[i] = calc_vol(r);
        }
        cout <<  round(BinSearch(v, N, F)*10000.0)/10000.0 << endl;
        
        
        T--;
    }
    return 0;
}

