<h1>Learning Java Script</h1>
array-It is an collection of multiple Data Type and it is a mutable.

```

let arr=[1,2,3,4,5]
console.log(arr);
console.log(arr.length)

```
<h2>Array Method</h2>
.toString()- We can convert an array to a string 

```

console.log(arr.toString())

```
join()-It will join all the element using the sepeator


```

console.log(arr.join(" and "))

```
pop()- It will pop out the or return me the last element.

```

a=[1,2,3,4,5]
a.pop()

```
push()- It will add a element at the end and also show the current length.

```

a=[1,2,3,4,5]
a.push(10)

```

<h2>Loop in JS</h2>

```


let a=[1,2,3,4,5,6]
for (let i=0; i<a.length; i++>){
    const element =a[i];
    console.log(element);

}

```

```

a.forEach(value, index, arr)=>{
    console.log(value, index, arr)
}

```
for of- It can be use to get the values from an array 
```

a=[1,2,3,4,5]
for (const iterator of a){
    console.log(iterator)
}

```
for in-It can be used to get the key form the array
```

let obj={
    a:1,
    b:2,
    c:3
}
for (const key in obj){
    if (Object.hasOwnProperty.call(obj,key)){
        const element = obj[key];
        console.log(element)
    }
}

```
map()- Create a new array by performing some operation on each array element.

```

let arr = [1,2,3,4,5]
let newArr=[]
for (let i=0; i<arr.length; i++){
    const element = arr[i];
    newArr.push(element**2)
}
       or
let newArr= arr.map((e)=>{
    return e**2
})
console.log(newArr)

```
```
arr=[1,12,3,23,4,5,34]
const greaterThenSeven=(e)=>{
    if(e>7){
        return true
    }
    return false
}
console.log(arr.filter(greaterThenSeven))
```
reduce an array to a single value.
```

let arr2=[1,2,3,4,5,6]
const red = (a,b)=>{
    return a*b
}
console.log(app2.reduce(red))

```
array from- used to create an array from any other object 

```

Array.from("Tenzin")

```


<h2> Github Commands</h2><br>
Links it to the GitHub repository

```

 git remote add origin git@github.com:tenzin65/Intern.git

```
Displays the list of remote repositories linked to your project along with their URLs.
The -v (verbose) flag shows both fetch and push URLs

```

git remote -v

```
Renames the current branch to main.

```

git branch -m main

```
Shows the commit history of the current branch.

```

git log

```
It sets the remote tracking branch, meaning your local branch (main) will now track origin/main.

```

git branch --set-upstream-to=origin/main

```
Pulls changes from the remote repository (origin/main).

```

git pull --rebase

```
