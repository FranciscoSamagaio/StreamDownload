from pytube import YouTube


def download_youtube_audio(search_query):
    '''
    Downloads the audio from the highest quality stream of the YouTube video based on the provided url.
    @param search_query: str, The url for the YouTube video.
    @return: 
    Example:
        >> download_youtube_audio("Desired YouTube Video")
    '''
    try:

        yt = YouTube(search_query)

        # Get the highest resolution stream
        audio = yt.streams.filter(only_audio = True).first()
        
        # Download the video to the current directory
        print("Downloading...")
        audio.download()
        print("Download complete.")

        print(f"{yt.title} by {yt.author} has been successfully downloaded.")

    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    # Ask the user to input the YouTube URL or search query
    audio = input("Enter the URL of the audio to download: ")

    download_youtube_audio(audio)

