/*const dfs = (x, y, word, puzzle, index) => {
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


  자바스크립트 2차원 배열 초기화
  const graph = new Array(n);
  for(let i =0; i< graph.length; i++){
    graph[i] = new Array(n);
  }

console.log(
  solution(
    [
      ["가", "나", "콜", "사"],
      ["라", "기", "로", "세"],
      ["미", "모", "리", "움"],
      ["상", "지", "곤", "타"],
    ],
    "콜로세움"
  )
);
//console.log(solution("bbbb"));
//console.log(solution("asscssf"));
//console.log(solution("yeongmin"));
//console.log(solution("noooeoool"));
const test = [
  ["가", "나", "콜", "사"],
  ["라", "기", "로", "세"],
  ["미", "모", "리", "움"],
  ["상", "지", "곤", "타"],
];

console.log(test[0][0]);*/
/*
function solution(s) {
  if (s.length === 4 || s.length === 6) {
    console.log(typeof s);
    console.log(typeof parseInt(s));
    if (isNaN(parseInt(s)) === false) {
      return true;
    }
  }
  return false;
}

console.log(solution(" 123"));
*/
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
/*
console.log(
  solution(
    [
      [3, 33, 24, 45],
      [6, 7, 9, 66],
      [3, 5, 88, 98],
      [4, 9, 55, 99],
    ],
    12
  )
);

console.log(solution([[1, 3]], 1));

console.log(solution([[3]], 1));

console.log(
  solution(
    [
      [1, 2],
      [3, 4],
    ],
    3
  )
);
console.log(
  solution(
    [
      [1, 3, 3, 4],
      [1, 5, 6, 7],
      [1, 2, 3, 99],
      [1, 2, 3, 100],
    ],
    11
  )
);

console.log(
  solution(
    [
      [4, 5, 6, 7, 8],
      [11, 12, 13, 14, 15],
      [15, 16, 19, 33, 35],
      [6, 8, 20, 22, 88],
      [8, 55, 66, 77, 100],
    ],
    11
  )
);
*/
console.log(
  solution(
    [
      [1, 2, 22],
      [3, 4, 23],
      [8, 9, 33],
    ],
    7
  )
);
