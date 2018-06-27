// 把每个要操纵的dom都变成操作对象，这样理解的话 代码也更加清晰
new Vue({
    el: ".vuej",
    data: {
        vueData:[
            {name: "youngdee" ,from: "China"},
            {name: "Scado" ,from: "China"},
            {name: "Jack" ,from: "China"},
            {name: "Mona" ,from: "China"},
            {name: "Howkins" ,from: "China"},
        ]
    }
});

new Vue({
    el: ".vuej2",
    data: {
        vueData:[
            {name: "Jack" ,from: "China"},
            {name: "Mona" ,from: "China"},
            {name: "Howkins" ,from: "China"},
            {name: "youngdee" ,from: "China"},
            {name: "Scado" ,from: "China"},
        ]
    }
});

console.log('向下执行到这里');