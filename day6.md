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


