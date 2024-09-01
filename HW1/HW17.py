# The author is Cody Brown, HW17.py

# Create a function that displays a line from your cherished lyric once. Then, leveraging this function, 
# design another that showcases that beloved line four times.

def lyric():
    return "Life\'s a dance you learn as you go"

print(lyric())

def x4_lyric():
    print(lyric())
    print(lyric())
    print(lyric())
    print(lyric())
    
x4_lyric()
