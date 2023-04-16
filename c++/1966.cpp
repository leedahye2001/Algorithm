#include<iostream>
#include<queue>
using namespace std;

int main(){
    int test_case;
    cin>>test_case;
    

    for(int i=0;i<test_case;i++){
        // 문서의 개수, 궁금한 자료의 위치 (정수)
        int count;
        int n, m;
        count=0;
        cin>>n>>m;

        priority_queue<int> Q;
        queue< pair<int,int> > QI;

        
        for(int j=0;j<n;j++){
            int importance;
            cin>>importance;
            // {인덱스,값}
            QI.push(make_pair(j, importance));
            Q.push(importance);
        }
        

        while(!QI.empty()){
            int index=QI.front().first;
            int value=QI.front().second;
            QI.pop();

            if(Q.top()==value){
                Q.pop();
                ++count;

                if(index==m){
                    cout<<count<<endl;
                    break;
                }
            } else {
                QI.push(make_pair(index, value));
            }
        }

    }


    return 0;
}