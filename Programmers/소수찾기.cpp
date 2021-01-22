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
// ������� ���� ���� 
//���Ϳ� �ߺ� �����ϴ� �� �־ ���ͷ� ����  
vector<int> v;

//�Ҽ� �Ǻ�
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
    //�ڸ��� ��ŭ ����  �� ���� �Ҽ����� �Ǻ��Ұž�! ���⼭ s�� ���� �ڸ��� e�� ���� �������ϴ��ڸ���
	//���� �������ϴ� �ڸ����� ���� �ڸ����� ������
	//int�� �ٲ� sum�� ���交�Ϳ��ٰ� ����  
    if(s==e){
        v.push_back(stoi(sum));
    }
    //�ƴҰ�� dfs ����  
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
   //���� ���� ����  
   int answer = 0;

   //�������� �ڸ��� ������ �Ǵϱ� �ϴ� �̰� �������
    for(int i = 1; i <= numbers.size(); i++) {
        dfs(numbers, "", 0, i);
    }
    //���� ���� v���� ���� �ߺ������ϴ� �ڵ絥 erase�� unique����ȴ� 
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(),v.end()),v.end());
    // �ߺ��� ���ŵǸ� ���� ���� ������ �Ҽ��Ǻ� ����
	// isPrime �� �ְ� �Ҽ��� answer+=1 
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
