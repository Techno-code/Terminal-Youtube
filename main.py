# Import library of functions we will use for filewriting .etc
import lib.backend

def print_menu():
    print("Option 1: Search channels")
    print("Option 2: Check your own channel")
    print("Option 3: Create New Video")
    print("Option 4: Edit channel")
    print("To exit, type 'QUIT'")

def print_edit_channel():
    print("Option 1: Delete Video")
    print("Option 2: Change Video Name")
    print("Option 3: Change channel name")
    print("Option 4: YOU CAN BUY SUBSCRIBER BOTS NO CAP NOT SCAM!!!s")
    print("Option 5: Delete Channel")
    print("To exit this portion, type 'QUIT'")

# Global variables to use to store current channel information
channel_name = ""
channel_number_of_subscribers = 0
channel_videos = []

# User login/signup
new_account = input("Do you have a channel: (Y for yes, N for no) ")

if new_account == "Y":
    channel_name = input("Enter your channel name: ")
    channel_number_of_subscribers = lib.backend.get_channel_subscriber_number(channel_name)
    channel_videos = lib.backend.get_channel_videos(channel_name)

elif new_account == "N":
    channel_name = input("Enter your new channel name: ")

# Main event loop
while True:
    print_menu()
    option_1 = input("Select menu option: ")
    if option_1 == "2":
        print("Channel Name: " + channel_name)
        print("Subscribers: " + str(channel_number_of_subscribers))
        print("Your Videos: " + str(channel_videos))
    elif option_1 == "1":
        # Make input to search videos and channels, then asks which ones it should view
        pass
    elif option_1 == "3":
        vid_title = input("Name your video: ")
        channel_videos.append(vid_title)
    elif option_1 == "4":
        while True:
            print_edit_channel()
            option_2 = input("Choose an option to edit channel: ")
            if option_2 == "QUIT":
                break
            elif option_2 == "1":
                # Make a list of the videos and use number inputs to choose video to delete
                print("Choose a video to delete")
                i = 0
                for i in range(len(channel_videos)):
                    print(f"{i+1}: {channel_videos[i]}")
                    i += 1
                delete_vid_option = input("Which vid do you want to delete? ")

            elif option_2 == "2":
                # Make a list of videos and use number inputs to choose video to change, then make an input for a new video name
                pass
            elif option_2 == "3":
                # Display current channel name and then input to change the name
                pass
            elif option_2 == "4":
                # Print that u got scammed, then delete channel
                pass
            elif option_2 == "5":
                delete_channel_option = input(("Are you sure you want to permanently delete your channel? (Y or N): "))
                if delete_channel_option == "Y":
                    print("Alright then...")
                    # Delete Channel


    elif option_1 == "QUIT":
        break

# Save session information
if new_account == "Y":
    # Update the existing channel file
    lib.backend.update_existing_channel(channel_name, channel_number_of_subscribers, channel_videos)
elif new_account == "N":
    # Create a textfile with the channel information
    lib.backend.create_channel(channel_name, channel_number_of_subscribers, channel_videos) 