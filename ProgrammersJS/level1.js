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
//배열 추가하기 : 배열.push();

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
// 문자열 자르기 : 변수.substr(어디부터, 얼만큼)

//하샤드 수
function solution(x) {
  var answer = true;
  const strX = x.toString();
  let sumX = 0;
  for (let i = 0; i < strX.length; i++) {
    sumX = sumX + parseInt(strX[i]);
  }
  if (x % sumX !== 0) {
    answer = false;
  }
  return answer;
}
/*
int -> string : 숫자.toString()
string -> int : parseInt(문자)
string한글자씩 접근 시 배열
*/

//평균 구하기
function solution(arr) {
  var answer = 0;
  for (let i = 0; i < arr.length; i++) {
    answer = answer + arr[i];
  }
  answer = answer / arr.length;
  return answer;
}

//콜라츠 추측
function solution(num) {
  var answer = 0;
  while (num !== 1) {
    if (answer < 500) {
      if (num % 2 === 0) {
        num = num / 2;
      } else if (num % 2 == 1) {
        num = num * 3 + 1;
      }
      answer += 1;
    } else {
      answer = -1;
      return answer;
    }
  }
  return answer;
}
//짝수와 홀수
function solution(num) {
  var answer = "";
  if (num % 2 === 0) {
    answer = "Even";
  } else {
    answer = "Odd";
  }
  return answer;
}

function solution(num) {
  var answer = "";
  answer = num % 2 === 0 ? "Even" : "Odd";
  return answer;
}
//홀수가 되는 조건에는 나머지가 마이너스인 경우있음

//제일 작은 수 제거하기
function solution(arr) {
  const min = Math.min(...arr);
  for (let i = 0; i < arr.length; i++) {
    if (min === arr[i]) {
      arr.splice(i, 1);
      i--;
    }
  }
  if (arr.length === 0) {
    arr.push(-1);
  }
  return arr;
}
/*
최솟값 : Math.min(...배열)
최댓값 : Math.max(...배열)
특정 값 제거하기 : splice(인덱스, 삭제할 개수), 삭제한 뒤 배열의 길이가 바뀌므로 인덱스 하나 감소시켜야함
*/

// 정수 제곱근 판별
function solution(n) {
  const sqrtNum = Math.sqrt(n);
  if (Number.isInteger(sqrtNum) && sqrtNum > 0) {
    return (sqrtNum + 1) * (sqrtNum + 1);
  } else {
    return -1;
  }
}
/*제곱근 : Math.sqrt(숫자)
정수인지 확인하는 방법 : Number.isInteger(숫자) or 1로 나눠서 0나오는지 확인
*/

//정수 내림차순으로 배치하기
function solution(n) {
  let arr = [];
  let strNum = n.toString();
  for (let i = 0; i < strNum.length; i++) {
    arr.push(strNum[i]);
  }
  arr.sort((a, b) => b - a);
  arr = arr.join("");
  return parseInt(arr);
}
/*arr.join하면 변수에 값을 할당해 주어야함
오름차순 : 배열.sort((a,b)=>a-b);
내림차순 : 배열.sort((a,b)=>b-a);
*/

// 자연수 뒤집어 배열로 만들기
function solution(n) {
  let arr = [];
  let strN = n.toString().split("").reverse();
  for (let i = 0; i < strN.length; i++) {
    arr.push(parseInt(strN[i]));
  }
  return arr;
}
/*문자열을 배열로 나누기 : 문자열.split('')
배열 반대로 뒤집기 : .reverse();
*/

// 자릿수 더하기
function solution(n) {
  let strN = n.toString();
  let sumN = 0;
  for (let i = 0; i < strN.length; i++) {
    sumN += parseInt(strN[i]);
  }
  return sumN;
}

// 이상한 문자 만들기
function solution(s) {
  let index = 0;
  s = s.split("");
  for (let i = 0; i < s.length; i++) {
    if (s[i] == " ") {
      index = 0;
    } else {
      if (index % 2 == 0) {
        s[i] = s[i].toUpperCase();
      } else {
        s[i] = s[i].toLowerCase();
      }
      index += 1;
    }
  }
  s = s.join("");
  return s;
}
/*
대문자로 변경 : toUpperCase()
소문자로 변경 : toLowerCase()
*/

//약수의 합
function solution(n) {
  let answer = [];
  let sqrtN = Math.sqrt(n);
  let sum = 0;
  for (let i = 1; i < sqrtN + 1; i++) {
    if (n % i === 0) {
      answer.push(i);
    }
  }
  let half = answer.length;
  for (let i = 0; i < half; i++) {
    if (n / answer[i] !== answer[i]) {
      answer.push(n / answer[i]);
    }
  }
  if (answer.length !== 0) {
    sum = answer.reduce((a, b) => a + b);
  }
  return sum;
}
// 합 : 배열.reduce((a, b) => a + b);

//문자열을 정수로 바꾸기
function solution(s) {
  let answer = 0;
  if (s[0] === "-") {
    answer = parseInt(s.substr(1, s.length - 1));
    answer = answer * -1;
  } else {
    if (s[0] === "+") {
      answer = parseInt(s.substr(1, s.length - 1));
    }
    answer = parseInt(s);
  }
  return answer;
}

//수박수박수박수박수박수?
function solution(n) {
  let answer = "";
  for (let i = 0; i < n; i++) {
    if (i % 2 === 0) {
      answer += "수";
    } else {
      answer += "박";
    }
  }
  return answer;
}

//소수 찾기
function solution(n) {
  let arr = Array.from({ length: n + 1 }, () => 0);
  let cnt = 0;
  for (let i = 2; i < n + 1; i++) {
    if (arr[i] === 0) {
      cnt += 1;
      for (let j = i; j < n + 1; j += i) {
        arr[j] = 1;
      }
    }
  }
  return cnt;
}
/*
자바스크립트 Array : 객체
Array.from() : Array.from({length: 길이}, (v, i)=>i 원하는 값 반환하는 콜백함수)
*/

//서울에서 김서방 찾기
function solution(seoul) {
  for (let i = 0; i < seoul.length; i++) {
    if (seoul[i] === "Kim") {
      return "김서방은 " + i + "에 있다";
    }
  }
}
//다른 사람 좋은 풀이
function findKim(seoul) {
  var idx = seoul.indexOf("Kim");
  return "김서방은 " + idx + "에 있다";
}
// 포문보다 좋은듯
