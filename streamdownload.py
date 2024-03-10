from pytube import YouTube, Search

def download_youtube(search_query, download_type):
    '''
    Downloads either the highest resolution video or audio from YouTube based on the provided search query.
    @param search_query: str, The search query for the YouTube video.
    @param download_type: str, The type of content to download, either 'audio' or 'video'.
    @return: 
    Example:
        >> download_youtube("Desired YouTube Video", "audio")
    '''
    try:
        # Perform a YouTube search
        search_results = Search(search_query).results
        if not search_results:
            raise ValueError("No search results found.")

        # Get the first video's URL
        url = search_results[0].watch_url

        # Get YouTube video details
        yt = YouTube(url)

        if download_type == 'audio':
            # Get the highest resolution audio stream
            stream = yt.streams.filter(only_audio=True).first()
        elif download_type == 'video':
            # Get the highest resolution video stream
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        else:
            raise ValueError("Invalid download type. Please choose 'audio' or 'video'.")

        # Download the audio or video to the current directory
        print("Downloading...")
        out_file = stream.download()
        print("Download complete.")

        print(f"{yt.title} by {yt.author} has been successfully downloaded.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Ask the user to input the search query
    search_query = input("Enter the Music to download: ")

    while True:
        # Ask the user what type to download
        download_type = input("Do you want to download 'audio' or 'video': ").lower()
        if download_type in ['audio', 'video']:
            break
        else:
            print("Invalid input. Please enter 'audio' or 'video'.")

    download_youtube(search_query, download_type)
