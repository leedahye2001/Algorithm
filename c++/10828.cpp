#include<iostream>
#include<stack>
#include<string>
using namespace std;

int main(){
    stack<int> X;
    string str;
    // 명령의 수(스택의 수)
    int n;
    cin >> n;

    for (int i=0;i<n;i++){
        cin >> str;
        if(str=="push"){
            int s;
            cin>>s;
            X.push(s);
        } else if(str=="pop"){
            if(X.empty()){
                cout<<"-1"<<endl;
            } else{
                cout<<X.top()<<endl;
                X.pop();
            }
        } else if(str=="size"){
            cout<<X.size()<<endl;
        } else if(str=="empty"){
            if(X.empty()){
                cout<<"1"<<endl;
            } else{
                cout<<"0"<<endl;
            }
        } else if(str=="top"){
            if(X.empty()){
                cout<<"-1"<<endl;
            } else {
                cout<<X.top()<<endl;
            }
        }
    }
    return 0;
}