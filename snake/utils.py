

def generate_letters(x, y, width=50, height=100):

    return \
    {
        'a': [
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x + (width / 2), 'y': y + height}},
            {'draw': {'x': x + width, 'y': y}},
            {'break': {'x': x + (width * 0.8), 'y': y + (height * 0.4)}},
            {'draw': {'x': x + (width * 0.2), 'y': y + (height * 0.4)}},
            {'break': {'x': x + (width * 1.1),  'y': y}},
            {'draw': {'x': x + (width * 0.9), 'y': y}},
            {'break': {'x': x - (width * 0.1), 'y': y}},
            {'draw': {'x': x + (width * 0.1), 'y': y}}
        ],
        'b': [
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + (height * 0.9)}},
            {'break': {'x': x, 'y': y + (height / 2)}},
            {'draw': {'x': x + (width / 2), 'y': y + (height / 2)}},
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x + (width / 2), 'y': y}},
            {'circle': {'radius': (width / 2), 'angle': 182}}
        ],
        'v': [
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x, 'y': y + height}},
            {'draw': {'x': x + (width * 0.2), 'y': y + height}},
            {'circle': {'radius': -(height * 0.2), 'angle': 180}},
            {'draw': {'x': x , 'y': y + (height * 0.6)}},
            {'draw': {'x': x + (width * 0.4), 'y': y + (height * 0.6)}},
            {'circle': {'radius': -(height * 0.3), 'angle': 180, 'rotation': 180}},
            {'draw': {'x': x, 'y': y}}
        ],
        'g': [
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + (height * 0.9)}},
            {'break': {'x': x - (width * 0.1), 'y': y}},
            {'draw': {'x': x + (width * 0.1) , 'y': y}}
        ],
        'k': [
          {'break': {'x': x, 'y': y}},
          {'draw': {'x': x, 'y': y + height}},
          {'break': {'x': x, 'y': y + (height * 0.5)}},
          {'draw': {'x': x + width, 'y': y + height}},
          {'break': {'x': x, 'y': y + (height * 0.5)}},
          {'draw': {'x': x + width, 'y': y}},
          {'break': {'x': x - (width * 0.1), 'y': y}},
          {'draw': {'x': x + (width * 0.1), 'y': y}},
          {'break': {'x': x - (width * 0.1), 'y': y + height}},
          {'draw': {'x': x + (width * 0.1), 'y': y + height}},
          {'break': {'x': x + (width * 0.9), 'y': y + height}},
          {'draw': {'x': x + (width * 1.1), 'y': y + height}},
          {'break': {'x': x + (width * 0.9), 'y': y }},
          {'draw': {'x': x + (width * 1.1), 'y': y }}
        ],
        'm': [
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x, 'y': y + height}},
            {'draw': {'x': x + (width / 2), 'y': y}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y}},
            {'break': {'x': x + (width * 0.9), 'y': y}},
            {'draw': {'x': x + (width * 1.1), 'y': y}},
            {'break': {'x': x + (width * 0.1), 'y': y}},
            {'draw': {'x': x - (width * 0.1), 'y': y}}
        ],
        'n': [
          {'break': {'x': x, 'y': y}},
          {'draw': {'x' : x, 'y': y + height}},
          {'break': {'x': x, 'y': y + (height / 2)}},
          {'draw': {'x': x + width, 'y': y + (height / 2)}},
          {'break': {'x': x + width, 'y': y + height}},
          {'draw': {'x': x + width,'y': y}},
          {'break': {'x': x, 'y': y + height}},
          {'draw': {'x': x - (width * 0.1),'y': y + height}},
          {'draw': {'x': x + (width * 0.1),'y': y + height}},
          {'break': {'x': x + width, 'y': y}},
          {'draw': {'x': x + (width * 0.9) , 'y': y}},
          {'draw': {'x': x + (width * 1.1) , 'y': y}},        
          {'break': {'x': x + width, 'y': y + height}},
          {'draw': {'x': x + (width * 0.9),'y': y + height}},
          {'draw': {'x': x + (width * 1.1),'y': y + height}},
          {'break': {'x': x , 'y': y}},
          {'draw': {'x': x - (width * 0.1),'y': y}},
          {'draw': {'x': x + (width * 0.1),'y': y}}
        ],
        'o': [
            {'break': {'x': x, 'y': y + (height / 4)}},
            {'circle': {'radius': (width / 2), 'angle': 180, 'rotation': 90}},
            {'draw': {'x': x + width, 'y': y + (height * 0.75)}},
            {'circle': {'radius': (width / 2), 'angle': 180}},
            {'draw': {'x': x, 'y': y + (height * 0.25)}}
        ],
        'p': [
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x, 'y': y + height}},
            {'draw': {'x': x - (width * 0.1), 'y': y + height}},
            {'draw': {'x': x + (width * 1.1), 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y}},
            {'draw': {'x': x + (width * 1.1), 'y': y}},
            {'draw': {'x': x + (width * 0.9), 'y': y}},
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x - (width * 0.1), 'y': y}},
            {'draw': {'x': x + (width * 0.1), 'y': y}}
        ],
        'r': [
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x, 'y': y + height}},
            {'draw': {'x': x + (width / 2), 'y': y + height}},
            {'break': {'x': x, 'y': y + (height / 2)}},
            {'draw': {'x': x + (width / 2), 'y': y + (height / 2)}},
            {'circle': {'radius': height / 4, 'angle': 182}},
            {'break': {'x': x - (width * 0.1), 'y': y}},
            {'draw': {'x': x + (width * 0.1), 'y': y}}
        ],
        's': [
            {'break': {'x': x + width, 'y': y}},
            {'draw': {'x': x + width, 'y': y + (height * 0.1)}},
            {'break': {'x': x + width, 'y': y + (height * 0.9)}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'circle': {'radius': width, 'angle': 180, 'rotation': 180}}
        ],
        't': [
            {'break': {'x': x + (width * 0.5), 'y': y}},
            {'draw': {'x': x + (width * 0.5), 'y': y + height}},
            {'break': {'x': x , 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + (height * 0.9)}},
            {'break': {'x': x, 'y': y + height}},
            {'draw': {'x': x, 'y': y + (height * 0.9)}},
            {'break': {'x': x + (width * 0.4), 'y': y}},
            {'draw': {'x': x + (width * 0.6), 'y': y}}
        ],
        'f': [
            {'break': {'x': x + (width / 2), 'y': y}},
            {'draw': {'x': x + (width / 2), 'y': y + height}},
            {'break': {'x': x + (width / 2), 'y': y + (height / 4)}},
            {'circle': {'radius': (width / 2), 'angle': 360}},
            {'break': {'x': x + (width / 2) + (width * 0.1), 'y': y + height}},
            {'draw': {'x': x + (width / 2) - (width * 0.1), 'y': y + height}},
            {'break': {'x': x + (width / 2), 'y': y}},
            {'draw': {'x': x + (width / 2) + (width * 0.1), 'y': y}},
            {'draw': {'x': x + (width / 2) - (width * 0.1), 'y': y}}
        ]
    }