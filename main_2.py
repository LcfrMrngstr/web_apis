
heroku buildpacks:set heroku/python
cat runtime.txt
python-3.10.2

from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

# Creating a new path operand
@app.get('/get/info')
async def get_info():
    return {
        "username": "username",
        "password": "password"
    }


# Will be using insomnia to send requests from now on.

#Creating a post request.
@app.post('/post/create')
async def post_create(information: dict = Body(...)):
    print(information)
    print('Success')
    return {
        "message": "Successfully created post"
    }



# Sending and using information that is received.
'''
The following message will be received:
{ 
    username: ...
    description: ....
    date: ....
}

To extract the information received, we can add a parameter to the app. The variable name could be anything, but
I used 'information'. The body function, appears to parse the information.
'''
