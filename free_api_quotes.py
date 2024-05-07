import requests


def quotes_free_api():
    url = "https://api.freeapi.app/api/v1/public/quotes?page=1&limit=10&query=human"
    response = requests.get(url)
    data = response.json()
    if data["success"] and data["data"]:
        Data = data["data"]
        currentPage = Data["currentPageItems"]
        current_data = Data["data"][0]
        datas = Data["data"]
        author=current_data["author"]
        for each_data in datas:
            print(each_data["content"])
        return currentPage,current_data,author
    else:
        raise Exception("failed to process")
    

def main():
    try:
        currentPage,current_data,author = quotes_free_api()
        print("\n Current Page: ",currentPage)
        print("\n Current data: ",current_data)
        print("\n Author: ",author)
    except Exception as e:
        print(str(e))



if __name__=="__main__":
    main()


