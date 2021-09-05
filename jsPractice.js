// 배열, 해시
function solution(mistake) {
  let answer = [];
  let original = Array.from({ length: mistake.length }, (v, i) => i + 1);
  let newList = original.reduce((acc, c) => {
    acc[c] = acc[c] ? acc[c] + 1 : 1;
    return acc;
  }, {});
  mistake.find((c) => {
    if (newList[c]) {
      newList[c] = 0;
    }
  });
  for (let i = 1; i < mistake.length + 1; i++) {
    if (newList[i] === 1) {
      answer.push(i);
    }
  }
  return answer;
}
/*
  reduce : 배열.reduce((누적값, 현재 처리할 요소, 인덱스-optional, reduce()를 호출한 배열-optional), 초깃값-optional);
  reduce는 '초기값'에 '배열의 요소' 누적
  자바스크립트는 객체의 키를 배열처럼 접근 가능
  let a = [1, 2, 3, 4]
  let b = a.reduce((x,y) => {
    x[y] = x[y]? x[y]+1: 1;
    return x;
  },{}); // {'1': 1, '2' : 1, '3' : 1, '4' : 1}
  //기존에 key로 존재하지 않으면 1, 있으면 다음 key;

  그러면 reduce와 hash를 사용하여 배열의 요소 갯수 찾기는 어떻게 해야할까?
  let a = [1, 1, 2, 2, 3, 3, 3, 3, 4]
  let b = a.reduce((x,y) => {
    x[y] = (x[y] ||0)+1;
    return x;
  },{}); // { '1': 2, '2': 2, '3': 4, '4': 1 }
  //기존에 key로 존재하지 않으면 0, 있으면 기존값에 +=1;
*/

//배열, 이진탐색, 큐
function solution(arr, num) {
  let total = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[0].length; j++) {
      total.push(arr[i][j]);
    }
  }
  total.sort((a, b) => a - b);
  return total[num - 1];
}
//런타임에러날듯

//부분배열, 슬라이딩 윈도우
function solution(str) {
  let arr = str.split("");
  let duplicate = {};
  let max_length = 0;
  let start = 0;
  for (const [index, element] of arr.entries()) {
    if (
      Object.keys(duplicate).includes(element) &&
      start <= duplicate[element]
    ) {
      start = duplicate[element] + 1;
    } else {
      max_length = Math.max(max_length, index - start + 1);
    }
    duplicate[element] = index;
  }
  return max_length;
}

/*
  Objects.entries : [key, value]쌍의 배열을 반환 
  배열에서 [key, value]쌍의 배열을 반환 하기 : const [index, element] of 배열.entries()
  객체 key값 있는지 확인 : Object.keys(객체).includes(찾고자하는요소)
*/

//배열, 그리디, 힙
