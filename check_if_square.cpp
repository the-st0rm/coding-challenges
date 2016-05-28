#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

bool check_square(vector<pair<int, int> > v)
{
	

	pair<int, int> main_p = v[0];
	vector<float> lengths;
	for(int i=1; i < v.size(); i++)
	{	
		float x = (main_p.first-v[i].first) * (main_p.first-v[i].first);
		float y = (main_p.second-v[i].second) * (main_p.second-v[i].second);
		lengths.push_back(x+y);
	}
	if (((lengths[0]==lengths[1]) && (2*lengths[0]==lengths[2])) || ((lengths[1]==lengths[2]) && (2*lengths[1]==lengths[0])) || ((lengths[0]==lengths[2]) && (2*lengths[0]==lengths[1])))
	{
		return true;
	}
	else
		return false;


}
int main()
{
	pair<int, int> p1;
	pair<int, int> p2;
	pair<int, int> p3;
	pair<int, int> p4;
	p1.first = 1, p1.second =1;
	p2.first = 1, p2.second =-1;
	p3.first =-1, p3.second =1;
	p4.first =-1, p4.second =-1;

	vector<pair<int, int> > v;
	v.push_back(p1);
	v.push_back(p2);
	v.push_back(p3);
	v.push_back(p4);

	cout << "Hello world" << endl;
	cout << check_square(v) << endl;


	return 0;
}