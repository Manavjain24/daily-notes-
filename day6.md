#so today we are going to talk about path and parameters according to which the journey for fastapi has been 
started and lets see how it goes this week this week i am focusing on completing all the targets and reaching my goals 
1) so path parameters are being used to opena specific folder or a specific folder location so it can be used 
to return the required item 
example -- 
from fastapi import fastAPI
app = FastAPI()
@app.get("/items/{item_id}")
async def read_item(item_id):
return{"item_id":item_id}
// in this the only instruction is being given of a specific folder 
// the path parameters are being used to insure that the things come in path of the link 
// or the url 
2) query parameter when we declare a function and in that we have things that are not meant to be mentioned in the path of the  url then it is being called query parameters 
from fastapi import FastAPI
app = FastAPI()
fake_items_db = [{"item_name" : "Foo"},{"item_name":"Bar"}]
@app.get("/items/")
async def read_item(skip:int = 0 , limit :int = 10 ):
return fake_items_db [skip: skip + limit ]
so the url for this would be http://127.0.0.1:8000/items/?skip=0&limit=10
