
# Import library of functions we will use for filewriting .etc
import lib.backend

def print_menu():
    print("Option 1: Search channels")
    print("Option 2: Check your own channel")

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
    option = input("Select menu option: ")


# Save session information
if new_account == "Y":
    # Update the existing channel file
    lib.backend.update_existing_channel(channel_name, channel_number_of_subscribers, channel_videos)
elif new_account == "N":
    # Create a textfile with the channel information
    lib.backend.create_channel(channel_name, channel_number_of_subscribers, channel_videos)