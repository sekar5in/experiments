import pafy
import re

url = "https://www.youtube.com/watch?v=1q9kw8ijZIQ"
videometa = pafy.new(url, basic=True, gdata=True, size=True)



print(videometa)