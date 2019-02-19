# Python3 urlparse lib
import urllib.parse as urlparse, os

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

# Build a filename-count dictionary
countList = dict()
for url in urls:
    # Get filename safety
    path = urlparse.urlparse(url).path
    filename = os.path.basename(path)
    # Count
    countList[filename] = countList[filename] + 1 if filename in countList else 1

# Sort DESC
sortList = [(k, countList[k]) for k in sorted(countList, key=countList.get, reverse=True)]
# Sort filename name with equal count
sortList.sort()

# Output format
# Top limit number
topLimit = 3
topCounter = 0
for filename, count in sortList:
    # top list limit
    topCounter = topCounter + 1
    if topCounter > topLimit:
        break
    print(filename + ' ' + str(count))
