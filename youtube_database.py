import sqlite3

conn = sqlite3.connect("youtube_videos.db") #returns connection object
curr=conn.cursor()
curr.execute(''' 
    CREATE TABLE if not exists videos(
             id INTEGER PRIMARY KEY,
             name TEST NOT NULL,
             time TEXT NOT NULL
    )
''')
def list_all_videos():
    curr.execute("select * from videos")  #tuple output hoga toh loop use karo to retrive through loop
    for row in curr.fetchall():
        print(row)

def add_videos(name,time):
    curr.execute("insert into videos (name,time)values(?,?)",(name,time))
    conn.commit()

def update_videos(video_id,new_name,new_time):
    curr.execute("update videos set name=?,time=? where id =?",(new_name,new_time,video_id))
    conn.commit()

def delete_videos(video_id):
    curr.execute("delete from videos where id=?",(video_id,))  #comma imp hai tuple ek raha toh comma imp warna error
    conn.commit()

def main():
    while True:
        print("\n Youtube Manager with DB")
        print("\n 1.List all videos")
        print("\n 2.add a new video")
        print("\n 3.update a new video")
        print("\n 4.delete a new video")
        print("\n 5.exit")
        choice = input("\n Enter the choice: ")
        if choice=='1':
            list_all_videos()
        elif choice == '2':
            name=input("enter the video name: ")
            time=input("enter the video time: ")
            add_videos(name,time)
        elif choice=='3':
            video_id=input("enter the video id to update")
            name=input("enter the video name: ")
            time=input("enter the video time: ")
            update_videos(video_id,name,time)
        elif choice=='4':
             video_id=input("enter the video id to delete")
             delete_videos(video_id)
        elif choice =='5':
            break
        else:
            print("enter the valid choice")
    
    conn.close()

if __name__=="__main__":
    main()