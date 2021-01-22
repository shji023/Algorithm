#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using  namespace  std;
const int MAX = 10000000;
bool check[MAX];
bool index_check[MAX];
bool two[MAX];
// 정답넣을 벡터 만듬 
//벡터에 중복 제거하는 게 있어서 벡터로 만들어봄  
vector<int> v;

//소수 판별
bool isPrime(int num){
	if (num<=1) return false;
    for (int i = 2; i < num; i++) {
        if (num % i ==0){
        	return false;
		}
    }
    return true;
}


void dfs(string numbers,string sum, int s,int e){
    //자릿수 만큼 오면  그 수가 소수인지 판별할거야! 여기서 s는 현재 자릿수 e는 내가 만들어야하는자릿수
	//내가 만들어야하는 자릿수가 현재 자릿수와 같으면
	//int로 바꾼 sum을 정답벡터에다가 넣음  
    if(s==e){
        v.push_back(stoi(sum));
    }
    //아닐경우 dfs 돌림  
	else{
		for(int i = 0; i < numbers.size(); i++){
	       if(index_check[i] == false){
	        	index_check[i] = true;
	        	dfs(numbers,sum+numbers[i],s+1,e);
	        	index_check[i] = false;
	       }
    	}
	}
}


int solution(string numbers) {
   //정답 개수 변수  
   int answer = 0;

   //조합으로 자릿수 여러개 되니까 일단 이거 만들었고
    for(int i = 1; i <= numbers.size(); i++) {
        dfs(numbers, "", 0, i);
    }
    //정답 벡터 v에들어간 수들 중복제거하는 코든데 erase랑 unique쓰면된대 
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(),v.end()),v.end());
    // 중복이 제거되면 남은 수들 가지고 소수판별 진행
	// isPrime 에 넣고 소수면 answer+=1 
    for(int j=0; j<v.size();j++){
    	if (isPrime(v[j])){
    		answer +=1;
		}
	}
    return answer;
}

int main(){
    cout<<solution("125");

}
