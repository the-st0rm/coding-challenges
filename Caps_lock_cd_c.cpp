#include <iostream>
#include <string>
#include <ctype.h>
using namespace std;

int main()
{
	string word;
	cin >> word;
	bool flag = true;
	for(int i=1; i<word.size();i++)
	{
		if (islower(word[i]))
			flag=false;
	}
	if (flag)
	{
		string new_word = "";
		for(int i=0; i< word.size();i++)
		{
			if (islower(word[i]))
			{
				new_word+=toupper(word[i]);
			}
			else if (isupper(word[i]))
			{
				new_word+=tolower(word[i]);
			}
			else
				new_word+=word[i];
		}
		cout << new_word << endl;
	}
	else
		cout << word << endl;




	return 0;
}