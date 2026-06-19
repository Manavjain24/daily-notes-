1) I would be talking about type hints in python this allows the devlopers to annotate their code with various 
types of variables and function arguments .
2) this also helps in checking the readability of the code .
3) in this we woukd be giving hint to how the code should look like if the output type is being specified 
example -- age: int = 23
def greet(name :str) -> str 
return f"hello ,{name} !"
in this as you have seen the function return a string in this 
also example 2 -- def adding(x: int , y : int ) -> int 
return x+y

aslo example 3 -- def substract (z:int , m:int)->int
return z-m'

also example 4 -- def intrest(principle : int , rate : float , time : int )-> float
return principle * rate * time / 100

in the second part we would be talking about dataclasses in this the reduction of the size of the class is being
done in such a way that the repetative action that are taken again and again those sizes are being reduced 
as an example -- from dataclasses import dataclass 
@dataclass
class Product:
name : str 
price : float
quantity : int = 0 