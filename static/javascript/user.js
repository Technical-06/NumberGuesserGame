// document.onload=async function(){
//   let apiUrl="/generateapi";
//   let res=await fetch(apiUrl);
//   console.log(res)
//   let genNumber=await res.json();
//   console.log(genNumber)
  
// }
let computerguess;
let flag=0;
const request = new Request(
  "/generateapi" ,
  {
    method: "GET",
  }
);
fetch(request)
  .then((response) => {
    if (response.status === 200) {
      return response.json();
    } else {
      throw new Error("Something went wrong on API server!");
    }
  })
  .then((response) => {
  computerguess=response.computerguess;
  console.log(computerguess);

})
  .catch((error) => {
    console.log(error);
  });



async function test(){ 
  let userNumber=document.getElementById("result").value;
  let apiUrl="/checkapi?userans="+userNumber.toString()+"&computerguess="+computerguess+"&flag="+flag;
  let res=await fetch(apiUrl);
  let result=await res.json();
  flag=result.flag;
  document.getElementById("set1").innerText=result.finalResult;
}

     