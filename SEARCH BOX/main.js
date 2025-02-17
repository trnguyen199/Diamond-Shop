let availableKeywords = [
    "Kim cương đỏ",
    "Kim cương vàng",
    "Kim cương trắng",
    "Kim cương hồng",
    "Nhẫn kim cương",
    "Vòng tay kim cương",
    "Bông tai kim cương",
    "Mặt dây chuyền kim cương"
   
];

const resultbox = document.querySelector('.result-box');
const inputBox = document.getElementById('input-box');

inputBox.onkeyup = function(){
    let result = [];
    let input = inputBox.value;
    if(input.length){
        result = availableKeywords.filter((keyword)=>{
           return keyword.toLowerCase().includes(input.toLowerCase());
        });
        console.log(result);
    }
    display(result);

    if(!result.length){
        resultbox.innerHTML = '';
    }
}

function display(result){
    const content = result.map((list)=>{
        return "<li onclick=selectInput(this)>" + list + "</li>";

    });

    resultbox.innerHTML = "<ul>" + content.join('')  + "</ul>" 
}
function selectInput(list){
    inputBox.value = list.innerHTML;
    resultbox.innerHTML = '';
}