from random import choice

Emoticons = [
    [':', ';', 'x'], # Eyes
    ['-',], # Nose (optional)
    [')', 'D', '>', '<', 'P', 'I', 'C', 'V', ']', '[', '|', 'O', '}', '{', '(']  # Mouth
]

EnableNose = False # Enable Nose

def RandomEmoticon() -> str:
    for Build in Emoticons:
        if Build is Emoticons[1] and not EnableNose:
            yield ' '
        else:
            yield choice(Build)

print(''.join(RandomEmoticon()))
