#include<iostream>
#include<stack>
#include<string>
using namespace std;

int main(){
	int n;
	cin >> n;
	string str;

	stack<int> S;
	int init=0;

	while(n--){
		int value;
		cin>>value;

		if(value>init){
			while(value>init){
				S.push(++init);
				str+='+';
			}
			S.pop();
			str+='-';
		} else {
			bool flag = false;
			if(!S.empty()){
				if(value==S.top()){
					flag=true;
				}
				S.pop();
				str+='-';
			}
			if(!flag){
				cout<<"NO"<<endl;
				return 0;
			}
		}
	}

	// 이걸 사용해야 배열 출력 됨
	for (auto value : str) {
		cout << value << '\n';
	}
	return 0;
}