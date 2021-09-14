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
function solution(str) {
  const alpha = [];
  let temp = 0;
  return str.split("").reduce((longest, index, initial) => {
    temp = temp <= alpha[index] ? alpha[index] + 1 : temp;
    alpha[index] = initial;
    return Math.max(longest, initial - temp + 1);
  }, 0);
}

//console.log(solve("abcd"));
//console.log(solve("abcab"));
//console.log(solve("bbbb"));
console.log(solution("asscssf"));
//console.log(solve("yeongmin"));
//console.log(solve("noooeoool"));
