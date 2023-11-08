// 改变所有json file的标题number字符串, 用 document.querySelectorAll获取不到

// Array.prototype.forEach.call(document.getElementsByClassName('caption-number'), el=>{
//     console.log(el.parentNode.nextSibling.classList)
// })
// captionNumberNodes = document.getElementsByClassName('caption-number')
// for(let i = 0; i < captionNumberNodes.length; i++){
//     let node = captionNumberNodes[i]
//     console.log(node.parentNode.nextSibling.classList)
// // }
$(document).ready(function(){
    // $('.caption-number').each((index, el) => {
    //     console.log(el)
    //     let parent = $(el).parent('div.code-block-caption + div.highlight-json:has')
    //     console.log(parent, parent.length)
    //     if(parent.length > 0){
    //         el.text('JSON File')
    //     }
    // });
    reg = /\.json$/
    $('div.code-block-caption + div.highlight-json').prev().children('span.caption-number').each((i, el)=>{
        if(reg.test($(el).next().text())){
            $(el).text('JSON File')
        }
    })
    
})

// list(.forEach(el=>{
//     console.log(el.parentNode.nextSibling.classList)
// })

// var targets = document.getElementsByClassName('code-block-caption')
// targets.forEach(element => {
//     target = element.querySeletor()
// });
// console.log(targets)