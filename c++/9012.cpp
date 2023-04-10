#include<iostream>
#include<stack>
#include<string>
using namespace std;

bool Ps(string str){
    stack<char>VPS;
    int length=str.length();

    for(int i=0;i<length;i++){
        char c = str[i];

        if(c=='('){
            VPS.push(c);
        } else {
            if(VPS.empty()){
                return false;
            } else {
                VPS.pop();
            }
        }
    }
    // 스택이 비어있으면 YES
    return VPS.empty();
}

int main(){
    int t;
    cin>>t;

    for(int i=0;i<t;i++){
       string str;
       cin>>str;

       if(Ps(str)){
        cout<<"YES"<<endl;
       } else {
        cout<<"NO"<<endl;
       }
    }

    return 0;
}