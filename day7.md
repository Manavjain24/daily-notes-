FastAPI mein multiple tasks handle karne ke do important tareeke hote hain: **Concurrency** aur **Parallelism**.

**Concurrency** mein server ek hi time par multiple tasks ko manage karta hai. Jab koi task database query, API call, ya file operation ke liye wait kar raha hota hai, tab server us wait time ko waste nahi karta aur doosre tasks ko handle karne lagta hai. Ye `async` aur `await` ki help se achieve kiya jata hai. Concurrency **I/O-bound tasks** ke liye sabse zyada useful hoti hai jahan kaafi time external resources ka wait karne mein jata hai.

**Parallelism** mein multiple tasks actual mein ek saath execute hote hain by using multiple CPU cores ya processes. Ye **CPU-bound tasks** ke liye useful hota hai, jaise image processing, machine learning computations, video encoding, ya heavy calculations, jahan zyada computation power ki zarurat hoti hai.

Ye kehna sahi nahi hoga ki concurrency hamesha slow hoti hai aur parallelism hamesha fast hota hai. Dono ka use-case alag hota hai. Agar task mein zyada waiting involved hai to concurrency better hoti hai, aur agar task mein heavy computation hai to parallelism better perform karta hai.

FastAPI dono approaches ko support karta hai. Ye `async` aur `await` ke through concurrency provide karta hai aur multiple workers ya processes ke through parallelism achieve kar sakta hai. Isliye FastAPI efficiently I/O-bound aur CPU-bound dono tarah ke workloads handle kar sakta hai.

Dependency 
FastAPI mein ye eek featurre hota hai jise hum dependency kehte hai jiske according hume jo bhi dependent kaam hota hai use dependency library import kara ke karna hota hai aur iske according 

