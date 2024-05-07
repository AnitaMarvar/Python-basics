import json
def load_data():
    try:
        with open('youtube.txt','r') as file:
           return json.load(file)  #converts (string)whatever is in youtube.txt to json
    #mujhe output json jaise hi chahiye
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    #saves all the videos 
    with open('youtube.txt','w') as file:
        file = json.dump(videos,file)  #json to string

def list_all_videos(videos):
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']},Duration: {video['time']}")

def add_video(videos):
    name=input("enter video name : ")
    time=input("enter the video time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index=int(input("enter the number you want to update"))
    if 1<= index <= len(videos):
        name=input("enter the new video name: ")
        time=input("enter the new time : ")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("invalid index")


def del_video(videos):
     list_all_videos(videos)
     index=int(input("enter the number you want to delete"))
     if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
     else:
         print("invalid index")

def main():   #starting point of the app
    videos=load_data()
    #saare data aayega pahele
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. delete a youtube video")
        print("5. Exit the app")
        choice = input("enter the choice: ")
        match choice:
            case '1':  
                list_all_videos(videos) 
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                del_video(videos)
            case '5':
                break
            case _:
                print("invalid choice")


if __name__=="__main__":  #if function name is main()
    main()  #calling main function