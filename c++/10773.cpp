#include<iostream>
#include<string>
#include<stack>
using namespace std;

int main(){
    int k;
    cin>>k;

    stack<int>X;

    for (int i=0;i<k;i++){
        int n;
        cin>>n;
        if(n==0){
            X.pop();
        } else {
            X.push(n);
        }
    }

    int sum=0;
    int size=X.size();

    // 왜 X.size()로 바로 쓰면 안되는거임;;
    for(int i=0;i<size;i++){
        sum+=X.top();
        X.pop();
    }
    cout<<sum<<endl;


    return 0;
}