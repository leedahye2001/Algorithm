#include<iostream>
#include<string>
#include<stack>
using namespace std;

int main() {
        while(true){
        string str;
        getline(cin, str);  // 한 줄 읽는 함수

            if(str=="."){
                // cout<<"yes"<<endl;
                break;
            }
            
        stack<char> B;
        bool flag=0; // 이거 생각해야됨

        for(int i=0;i<str.length();i++){
            char s=str[i];

                if ((s=='(' || s=='[')) { // 여기 괄호(()) 두 개 안 넣으면 에러남
                    B.push(s);
                } else if(s==')'){
                    if(!B.empty() && B.top()=='('){
                        B.pop();
                    } else {
                        flag = 1;
                        break;
                    }
                } else if(s==']'){
                    if(!B.empty() && B.top()=='['){
                        B.pop();
                    } else {
                        flag = 1;
                        break;
                    }
                }
            }
            

           if(flag==0 && B.empty()){
            cout<<"yes"<<endl;
           } else {
            cout<<"no"<<endl;
           }
        }
    }