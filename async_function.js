let fruits = ["apple", "orange", "banana"]

const display = () =>{
    fruits.map(item =>document.write(`<li>${item}</li>`))
}

const add = (fruit) =>{
        fruits.push(fruit)
        
}

const display_async = () =>{
    setTimeout(display, [2000])
}

const add_async = (fruit, cb) =>{
    setTimeout(()=>{
        add(fruit)
        cb();
    }
    , [3000])
}

const add_async2 = (fruit) =>{
    return new Promise((resolve, reject)=>{
        let error=true
        setTimeout(()=>{
           
            if(!error){
                add(fruit)
                resolve()
            }
            else{
                reject("Something went wrong")
            }
        }
        , [3000])
    })
}


