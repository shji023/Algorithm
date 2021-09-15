// 1. 배열, 해시
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
//1 - 1
function solution(nums) {
  const length = nums.length;
  let students = [...Array(length + 1).keys()].slice(1);
  /*arr.keys()
  let arr = ['a', 'b', 'c']
  let denseKeys = [...arr.keys()] // [0,1,2]
  */
  for (disappear of nums) {
    students[disappear - 1] = -1;
  }
  /*nums 돌면서 있으면 students에 해당 값 -1, students에서 0보다 안큰 값이 정답 */
  return students.filter((total) => 0 < total);
}

//2. 배열, DFS - 수정 필요 if dfs 문이 작동하지않음
const dfs = (x, y, word, puzzle, index) => {
  if (x <= -1 || x >= 4 || y <= -1 || y >= 4) {
    return false;
  }
  if (puzzle[x][y] === word[index]) {
    index += 1;
    dfs(x - 1, y, word, puzzle, index);
    dfs(x, y - 1, word, puzzle, index);
    dfs(x + 1, y, word, puzzle, index);
    dfs(x, y + 1, word, puzzle, index);
    if (index === 4) {
      return true;
    }
  }
  return false;
};

function solution(puzzle, word) {
  let result = false;
  let index = 0;
  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < 4; j++) {
      if (dfs(i, j, word, puzzle, index) === 4) {
        result = true;
        return result;
      }
    }
  }
  return result;
}

/*
  자바스크립트 2차원 배열 초기화
  const graph = new Array(n);
  for(let i =0; i< graph.length; i++){
    graph[i] = new Array(n);
  }
*/

//3. 배열, 이진탐색, 큐 - 런타임에러날듯
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

function solution(arr, num) {
  let lastIndex = arr.length - 1;
  let min = arr[0][0];
  let max = arr[lastIndex][lastIndex] + 1;
  while (min < max) {
    let mid = Math.floor((min + max) / 2);
    let cnt = 0;
    for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < arr.length; j++) {
        if (arr[i][j] <= mid) {
          cnt++;
        } else {
          break;
        }
      }
    }
    if (cnt < num) {
      min = mid + 1;
      console.log(min);
    } else {
      max = mid;
    }
  }
  return min;
}

//4. 부분배열, 슬라이딩 윈도우
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

function solution(str) {
  const alpha = [];
  let temp = 0;
  return str.split("").reduce((longest, index, initial) => {
    temp = temp <= alpha[index] ? alpha[index] + 1 : temp;
    alpha[index] = initial;
    return Math.max(longest, initial - temp + 1);
  }, 0);
}
/*
  Objects.entries : [key, value]쌍의 배열을 반환 
  배열에서 [key, value]쌍의 배열을 반환 하기 : const [index, element] of 배열.entries()
  객체 key값 있는지 확인 : Object.keys(객체).includes(찾고자하는요소)
*/

//5.배열, 그리디, Heap - 문제 이해 실패
//6. 배열, 그리디, Sorting
const solve = (time, distance) => {
  const dist = distance.length;
  let enemy = [];
  let defense = 0;
  for (let i = 0; i < dist; i++) {
    enemy.push(distance[i] / time[i]); /*(거리/시간)*/
  }
  enemy.sort((x, y) => x - y); /*오름차순 정렬*/
  for (const soldier of enemy) {
    if (soldier - defense <= 0) {
      break;
    }
    defense++; /*속력안에 막은 적군들 수*/
  }
  return defense;
};
