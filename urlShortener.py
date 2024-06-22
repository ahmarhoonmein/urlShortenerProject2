import pyshorteners

def shortenUrl(url):
    sh = pyshorteners.Shortener()
    return sh.tinyurl.short(url)


url = input("Enter a URL: ")
shortUrl = shortenUrl(url)

print("Shortened URL:", shortUrl)

print("Developed by Ahmar.")
