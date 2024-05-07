import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url) # response in string
    data=response.json()  #converts to json

    if data["success"] and "data" in data:
        user_data=data["data"]
        user_name=user_data["login"]["username"]  # userdata ke andar joh login hai aur login ke andar joh username hai woh
        user_country = user_data["location"]["country"]
        return user_name,user_country
    else:
        raise Exception("Failed to fetch user data")   #jaanbujkar hum raise karege error
    

def main():
    try:
        username,country=fetch_random_user_freeapi()
        print("Username: ",username)
        print("Country: ",country)
    except Exception as e:
        print(str(e))  #kuch bhi error ka format ho sakta hai

if __name__=='__main__':
    main()