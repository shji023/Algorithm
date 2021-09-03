//직사각형 별찍기
process.stdin.setEncoding("utf8");
process.stdin.on("data", (data) => {
  const n = data.split(" ");
  const a = Number(n[0]),
    b = Number(n[1]);
  for (let i = 0; i < b; i++) {
    let row = "";
    for (let j = 0; j < a; j++) {
      row = row + "*";
    }
    console.log(row);
  }
});

//x만큼 간격이 있는 n개의 숫자
function solution(x, n) {
  var answer = [];
  for (let i = 1; i < n + 1; i++) {
    answer.push(x * i);
  }
  return answer;
}

//행렬의 덧셈
function solution(arr1, arr2) {
  var answer = [];
  const row = arr1.length;
  const col = arr1[0].length;
  for (let i = 0; i < row; i++) {
    answer.push([]);
    for (let j = 0; j < col; j++) {
      answer[i].push(arr1[i][j] + arr2[i][j]);
    }
  }
  return answer;
}

//핸드폰 번호 가리기
function solution(phone_number) {
  var answer = "";
  const len = phone_number.length;
  for (let i = 0; i < len - 4; i++) {
    answer = answer + "*";
  }
  answer = answer + phone_number.substr(phone_number.length - 4, 4);
  return answer;
}
