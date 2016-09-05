#include  <iostream>
#include  <vector>


using std::vector;
using std::cin;
using std::cout;

int MaxPairWiseProduct(const vector<int> & numbers){
	int result = 0;
	int n = numbers.size();
	int temp;
	for(int i=0 ;i < n;i++)
	{
		for(int j = i+1; j<n; j++)
		{
			temp = numbers[i] * numbers[j];
			if( temp > result)
        	{
        		result =temp;
        	}
		}
	}
	return result; 
}

int main() {
	int n;
	cin >> n;
	vector<int> numbers(n);
	for (int i=0;i<n;i++)
	{
		cin >> numbers[i];
	}

	int result = MaxPairWiseProduct(numbers);
	cout << result ;
	return 0;

}
