/*
KMP(Knuth-Morris-Pratt)
���ڿ� ��Ī �˰��� - Ư���� ���� ���� �� �� �� �ȿ��� �ϳ��� ���ڿ��� ã�� �˰���
��� ��츦 �� ������ �ʾƵ� �κ� ���ڿ��� ã�� �� ����
���λ�(prefix)�� ���̻�(suffix)
'�ݺ��Ǵ� ������ �󸶳� ���� �� �ִ���', ���ʿ��� �κ��� ����
���λ�� ���̻簡 ��ġ�ϴ� �ִ� ����
��ġ�ϴ� ��� start, end �Ѵ� ���� ��ġ���� �ʴ� ��� end�� ���� start�� ���� 0�̾��� ������ ����
��ġ�ϴ� ��쿡�� start�� ������ 1�� ���� ��

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
				printf("%d��°���� ã�ҽ��ϴ�.\n", i-patternSize +2);
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
