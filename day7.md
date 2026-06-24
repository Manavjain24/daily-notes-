FastAPI mein multiple tasks handle karne ke do important tareeke hote hain: **Concurrency** aur **Parallelism**.

**Concurrency** mein server ek hi time par multiple tasks ko manage karta hai. Jab koi task database query, API call, ya file operation ke liye wait kar raha hota hai, tab server us wait time ko waste nahi karta aur doosre tasks ko handle karne lagta hai. Ye `async` aur `await` ki help se achieve kiya jata hai. Concurrency **I/O-bound tasks** ke liye sabse zyada useful hoti hai jahan kaafi time external resources ka wait karne mein jata hai.

**Parallelism** mein multiple tasks actual mein ek saath execute hote hain by using multiple CPU cores ya processes. Ye **CPU-bound tasks** ke liye useful hota hai, jaise image processing, machine learning computations, video encoding, ya heavy calculations, jahan zyada computation power ki zarurat hoti hai.

Ye kehna sahi nahi hoga ki concurrency hamesha slow hoti hai aur parallelism hamesha fast hota hai. Dono ka use-case alag hota hai. Agar task mein zyada waiting involved hai to concurrency better hoti hai, aur agar task mein heavy computation hai to parallelism better perform karta hai.

FastAPI dono approaches ko support karta hai. Ye `async` aur `await` ke through concurrency provide karta hai aur multiple workers ya processes ke through parallelism achieve kar sakta hai. Isliye FastAPI efficiently I/O-bound aur CPU-bound dono tarah ke workloads handle kar sakta hai.

Dependency Injection 
FastAPI mein **Dependency Injection** ek feature hai jo code ko reusable, clean aur maintainable banata hai.

Dependency ka matlab hai ki agar kisi endpoint ko koi common functionality chahiye, jaise database connection, authentication check, current user information, ya validation logic, to us functionality ko baar-baar likhne ki jagah ek alag function mein define kar sakte hain aur jahan zarurat ho wahan use kar sakte hain.

FastAPI mein dependencies ko `Depends()` ki help se inject kiya jata hai. Jab koi request aati hai, FastAPI pehle dependency function ko execute karta hai aur phir uska result endpoint function ko provide karta hai.

Iska fayda ye hai ki code duplication kam hota hai, code zyada reusable banta hai, aur maintenance easy ho jati hai. Agar common logic mein koi change karna ho to sirf dependency function ko update karna padta hai, har endpoint ko alag-alag modify nahi karna padta.

Path operation functions multiple dependencies use kar sakte hain aur ek dependency doosri dependency par bhi depend kar sakti hai. Isse complex applications mein code ko organize karna aur manage karna bahut aasaan ho jata hai.

Exception -- web socket exception and https exception 
these are the exceptions that could be shown to the customer if being required 
there are diffrent ways to show exception to the customer in formats like 
1)status_code
2)details -- it is the json prompt being sent to the customer depending upon the usage 
3)headers -- headers are being sent to client as an response




