/*
KMP(Knuth-Morris-Pratt)
문자열 매칭 알고리즘 - 특정한 글이 있을 때 그 글 안에서 하나의 문자열을 찾는 알고리즘
모든 경우를 다 비교하지 않아도 부분 문자열을 찾을 수 있음
접두사(prefix)와 접미사(suffix)
'반복되는 연산을 얼마나 줄일 수 있는지', 불필요한 부분은 점프
접두사와 접미사가 일치하는 최대 길이
일치하는 경우 start, end 둘다 증가 일치하지 않는 경우 end만 증기 start는 이전 0이었던 곳으로 감소
일치하는 경우에는 start의 값에서 1을 더한 값

*/
#include<iostream>
#include<vector>
using namespace std;

vector<int> makeTable(string pattern){
	int patternSize = pattern.size();
	vector<int> table(patternSize, 0);
	int j=0;
	for(int i=1; i<patternSize; i++){
		while(j >0 && pattern[i]!=pattern[j]){
			j=table[j-1];
		}
		if(pattern[i]==pattern[j]){
			table[i]= ++j;
		}
	}
	return table;
}

void KMP(string parent, string pattern){
	vector<int> table = makeTable(pattern);
	int parentSize = parent.size();
	int patternSize = pattern.size();
	int j = 0;
	for(int i=0; i<parentSize; i++){
		while(j>0 &&parent[i]!=pattern[j]){
			j=table[j-1];
		}
		if(parent[i]==pattern[j]){
			if(j==patternSize-1){
				printf("%d번째에서 찾았습니다.\n", i-patternSize +2);
				j=table[j];
			} else{
				j++;
			}
		}
	}
	
}
 
int main(void){
	string parent = "ababacabacaabacaaba";
	string pattern = "abacaaba";
	KMP(parent, pattern);
	vector<int> table = makeTable(pattern);
	for(int i=0; i<table.size(); i++){
		printf("%d", table[i]);
	}
	return 0;
}
