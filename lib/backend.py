
'''
    Channel file:
        Line 0: Channel name
        Line 1: Number of subscribers
        Lines 2 - N: List of videos
'''

'''
    This function will allow you to open a file and read its contents line by line
        returns a list of strings, each string is a line in the file
'''
def read_file_as_list(filename):

    # Open the file
    file = open("filename", "r")
    # Retrieve contents of file as lines; note that each line will end with a newline character, will strip later
    lines_from_file = file.readlines()

    lines = []
    for line in lines_from_file:
        lines.append(line.strip())

    return lines

'''
    This function takes in a channel name
        returns the channel information: name, subscribers, videos
'''
def get_channel_from_file(channel):

    # Name of the file containing the channel data
    filename = channel + ".txt"
    channel_list = read_file_as_list(filename)

    channel_name = channel_list[0]
    channel_subscribers = int(channel_list[1])
    channel_videos = []

    # Videos exist
    if len(channel_list) > 2:
        channel_videos = channel_list[2:]
    
    return channel_name, channel_subscribers, channel_videos

def get_channel_name(channel):

    channel_name, channel_subscribers, channel_videos = get_channel_from_file(channel)
    return channel_name

def get_channel_subscriber_number(channel):

    channel_name, channel_subscribers, channel_videos = get_channel_from_file(channel)
    return channel_subscribers

def get_channel_videos(channel):
    
    channel_name, channel_subscribers, channel_videos = get_channel_from_file(channel)
    return channel_videos

'''
    This function creates a new text file from a channel's data
        nothing is returned
'''
def create_channel(channel_name):

    # Create a new text file for the channel
    filename = channel_name + ".txt"
    file = open(filename, "x")

    # Write the channel name and the number of subscribers into the file
    file.write(channel_name)
    file.write(0)
    file.close()

def create_channel(channel_name, channel_subscribers):

    # Create a new text file for the channel
    filename = channel_name + ".txt"
    file = open(filename, "x")

    # Write the channel name and the number of subscribers into the file
    file.write(channel_name)
    file.write(channel_subscribers)
    file.close()

def create_channel(channel_name, channel_subscribers, channel_videos):

    # Create a new text file for the channel
    filename = channel_name + ".txt"
    file = open(filename, "x")

    # Write the channel name and the number of subscribers into the file
    file.write(channel_name)
    file.write(channel_subscribers)

    for video in channel_videos:
        file.write(video)

    file.close()

'''
    This function updates an existing channel file
        nothing is returned

'''