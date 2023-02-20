import colour, pyperclip # Install with < pip install colour pyperclip >

with open('Colors.txt', 'r') as File: # All the available colors that can be used to convert the message.
    Colors = File.read().splitlines()
    for Color in Colors:
        print(Color)

try:
    while True:
        print('\nEnter a message to convert to Xonotic colors.')
        Message = input(' > ')
        Red = colour.Color('DarkRed')
        Green = colour.Color('DarkViolet')
        Ranges = list(Red.range_to(Green, len(Message)))
        RangeList = []
        print('Say ', end='')
        for Letter in Message:
            Range = Ranges.pop(0)
            Range = list(Range.hex_l)[1:]
            Range = Range[0:1], Range[2:3], Range[4:5]
            Range = ''.join((''.join(Range[0]), ''.join(Range[1]), ''.join(Range[2])))
            Range = '^x'+Range+Letter
            RangeList.append(Range)
            print(Range, end='')
        pyperclip.copy('Say '+''.join(RangeList))
        print('Copied to clipboard.\n')

except KeyboardInterrupt:
    print('\nExiting...')
    exit()