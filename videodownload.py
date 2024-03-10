from pytube import YouTube


def download_youtube_video(search_query):
    '''
    Downloads the highest resolution video from YouTube based on the provided url.
    @param search_query: str, The url for the YouTube video.
    @return: 
    Example:
        >> download_youtube_video("Desired YouTube Video")
    '''
    try:

        yt = YouTube(search_query)
        
        # Get the highest resolution stream
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() 
        
        # Download the audio to the current directory
        print("Downloading...")
        video.download()
        print("Download complete.")

        print(f"{yt.title} by {yt.author} has been successfully downloaded.")

    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    # Ask the user to input the YouTube URL or search query
    video = input("Enter the URL of the video to download: ")

    download_youtube_video(video)
