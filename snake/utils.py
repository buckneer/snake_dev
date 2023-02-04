def generate_letters_width(width = 50):
    return \
        {
            '.': width * 0.1,
            ',': width * 0.1,
            '!': width * 0.1,
            ';': width * 0.1,
            ':': width * 0.1,
            '(': width * 0.2,
            ')': width * 0.2,
            '@': width * 0.2,
            '*': width * 0.4,
            '/': width * 0.5,
            'q': width * 1.6,
            'w': width * 1.7
        }


def get_letter_width(letter):
    if letter in generate_letters_width():
        return generate_letters_width()[letter]
    else:
        return 50
    pass


def generate_letters(x, y, width=50, height=100):

    return \
    { 
        ' ': [],
        '.': [
            {'break': {'x': x + (width * 0.1), 'y': y}},
            {'circle': {'radius': (width * 0.1), 'angle': 360}}
        ],
        '!': [
            {'break': {'x': x + (width * 0.1), 'y': y + height}},
            {'draw': {'x': x + (width * 0.1), 'y': y + (height * 0.2)}},
            {'break': {'x': x + (width * 0.1), 'y': y}},
            {'circle': {'radius': (width * 0.1), 'angle': 360}}
        ],
        '@': [ # znaci navoda "
            {'break': {'x': x, 'y': y + (height * 0.8)}},
            {'draw': {'x': x, 'y': y + (height * 0.7)}},
            {'break': {'x': x + (width * 0.2), 'y': y + (height * 0.8)}},
            {'draw': {'x': x + (width * 0.2), 'y': y + (height * 0.7)}}
        ],
        '#': [
            {'break': {'x': x, 'y': y + (height * 0.33)}},
            {'draw': {'x': x + width, 'y': y + (height * 0.33)}},
            {'break': {'x': x, 'y': y + (height * 0.66)}},
            {'draw': {'x': x + width, 'y': y + (height * 0.66)}},
            {'break': {'x': x + (width * 0.33), 'y': y + height}},
            {'draw': {'x': x + (width * 0.33), 'y': y}},
            {'break': {'x': x + (width * 0.66), 'y': y + height}},
            {'draw': {'x': x + (width * 0.66), 'y': y}}
        ],
        ',': [
            {'break': {'x': x + (width * 0.1), 'y': y}},
            {'circle': {'radius': (width * 0.1), 'angle': 450}},
            {'circle': {'radius': (width * 0.4), 'angle': -45}}
        ],
        '<': [ # tacka zarez ;
            {'break': {'x': x + (width * 0.1), 'y': y + (height * 0.7)}},
            {'circle': {'radius': (width * 0.1), 'angle': 360}},
            {'break': {'x': x + (width * 0.1), 'y': y + (height * 0.3)}},
            {'circle': {'radius': (width * 0.1), 'angle': 450}},
            {'circle': {'radius': (width * 0.4), 'angle': -45}}
        ],
        '>': [ # dve tacke : 
            {'break': {'x': x + (width * 0.1), 'y': y + (height * 0.7)}},
            {'circle': {'radius': (width * 0.1), 'angle': 360}},
            {'break': {'x': x + (width * 0.1), 'y': y + (height * 0.3)}},
            {'circle': {'radius': (width * 0.1), 'angle': 360}},
        ],
        '?': [
            {'break': {'x': x, 'y': y + (height * 0.75)}},
            {'circle': {'radius': -(width / 2), 'angle': 270, 'rotation': 270}},
            {'draw': {'x': x + (width / 2), 'y': y + (height * 0.2)}},
            {'break': {'x': x + (width / 2), 'y': y}},
            {'circle': {'radius': (width * 0.1), 'angle': 360}}
            
        ],
        '-': [
            {'break': {'x': x, 'y': y + (height * 0.5)}},
            {'draw': {'x': x + width, 'y': y + (height * 0.5)}}
        ],
        '+': [
            {'break': {'x': x, 'y': y + (height * 0.5)}},
            {'draw': {'x': x + width, 'y': y + (height * 0.5)}},
            {'break': {'x': x + (width / 2), 'y': y + (height * 0.75)}},
            {'draw': {'x': x + (width / 2), 'y': y + (height * 0.25)}}
        ],
        '/': [
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x + (width / 2), 'y': y + height}},
        ],
        '*': [
            {'break': {'x': x + (width * 0.1), 'y': y + (height * 0.8)}},
            {'draw': {'x': x + (width * 0.3), 'y': y + height}},
            {'break': {'x': x + (width * 0.1), 'y': y + (height)}},
            {'draw': {'x': x + (width * 0.3), 'y': y + (height * 0.8)}},
            {'break': {'x': x, 'y': y + (height * 0.9)}},
            {'draw': {'x': x + (width * 0.4), 'y': y + (height * 0.9)}}
        ],
        '=': [
            {'break': {'x': x, 'y': y + (height * 0.6)}},
            {'draw': {'x': x + width, 'y': y + (height * 0.6)}},
            {'break': {'x': x, 'y': y + (height * 0.4)}},
            {'draw': {'x': x + width, 'y': y + (height * 0.4)}}
        ],
        '_': [
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x + width, 'y': y}}
        ],
        '(': [
            {'break': {'x': x + (width * 0.2), 'y': y}}, 
            {'circle': {'radius': width * 0.2, 'angle': -90}},
            {'draw': {'x': x, 'y': y + (height * 0.9)}},
            {'circle': {'radius': width * 0.2, 'angle': -90}}
        ],
        ')': [
            {'break': {'x': x, 'y': y}},
            {'circle': {'radius': width * 0.2, 'angle': 90}},
            {'draw': {'x': x + (width * 0.2), 'y': y + (height * 0.9)}},
            {'circle': {'radius': width * 0.2, 'angle': 90}}
        ],
        # '[': [
        #     {'break': {'x': x + (width * 0.2), 'y': y}},
        #     {'draw': {'x': x, 'y': y}},
        #     {'draw': {'x': x, 'y': y + height}},
        #     {'draw': {'x': x + (width * 0.2), 'y': y + height}}
        # ],
        '1': [
            {'break': {'x': x, 'y': y + (height * 0.8)}},
            {'draw': {'x': x + (width * 0.8), 'y': y + height}},
            {'draw': {'x': x + (width * 0.8), 'y': y}},
            {'break': {'x': x + (width * 0.6), 'y': y}},
            {'draw': {'x': x + width, 'y': y}},
        ],
        '2': [
            {'break': {'x': x, 'y': y + (height * 0.75)}},
            {'circle': {'radius': -(width / 2), 'angle': 225, 'rotation': 270}},
            {'draw': {'x': x, 'y': y}},
            {'draw': {'x': x + width, 'y': y}}
        ],
        '3': [
            {'break': {'x': x + (width / 2), 'y': y + (height / 2)}},
            {'circle': {'radius': -(height * 0.25), 'angle': 270}},
            {'break': {'x': x + (width / 2), 'y': y + (height / 2)}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'draw': {'x': x, 'y': y + height}},
            {'break': {'x': x, 'y': y + (height * 0.9)}},
            {'draw': {'x': x, 'y': y + height}},
            {'break': {'x': x - (width * 0.1), 'y': y + (height * 0.25)}},
            {'draw': {'x': x + (width * 0.1), 'y': y + (height * 0.25)}}
        ],
        '4': [
            {'break': {'x': x + (width * 0.4), 'y': y}},
            {'draw': {'x': x + (width * 0.8), 'y': y}},
            {'break': {'x': x + (width * 0.6), 'y': y}},
            {'draw': {'x': x + (width * 0.6), 'y': y + height}},
            {'draw': {'x': x, 'y': y + (height * 0.4)}},
            {'draw': {'x': x + width, 'y': y + (height * 0.4)}},
        ],
        '5': [
            {'break': {'x': x + width, 'y': y + height}},
            {'draw': {'x': x, 'y': y + height}},
            {'draw': {'x': x, 'y': y + (height / 2)}},
            {'draw': {'x': x + (width / 2), 'y': y + (height / 2)}},
            {'circle': {'radius': width / 2, 'angle': -180, 'rotation': 180}},
            {'draw': {'x': x, 'y': y}}
        ],
        '6': [
            {'break': {'x': x, 'y': y + (height * 0.25)}},
            {'circle': {'radius': width / 2, 'angle': 360, 'rotation': -90}},
            {'break': {'x': x, 'y': y + (height * 0.25)}},
            {'draw': {'x': x, 'y': y + (height * 0.8)}},
            {'circle': {'radius': height * 0.2, 'angle': -90}},
            {'draw': {'x': x + (width * 0.6), 'y': y + height}},
            {'circle': {'radius': height * 0.2, 'angle': -30}}
        ],
        '7': [
            {'break': {'x': x + (width * 0.4), 'y': y}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'draw': {'x': x, 'y': y + height}},
            {'break': {'x': x + (width * 0.4), 'y': y + (height * 0.5)}},
            {'draw': {'x': x + width, 'y': y + (height * 0.5)}}
        ],
        '8': [
            {'break': {'x': x, 'y': y + (height * 0.75)}},
            {'circle': {'radius': width / 2, 'angle': 360, 'rotation': -90}},
            {'break': {'x': x, 'y': y + (height * 0.25)}},
            {'circle': {'radius': width / 2, 'angle': 360}}
        ],
        '9': [
            {'break': {'x': x, 'y': y + (height * 0.75)}},
            {'circle': {'radius': width / 2, 'angle': 360, 'rotation': -90}},
            {'break': {'x': x + width, 'y': y + (height * 0.75)}},
            {'draw': {'x': x + width, 'y': y + (height * 0.2)}},
            {'circle': {'radius': height * 0.2, 'angle': -90, 'rotation': 180}},
            {'draw': {'x': x + (width * 0.4), 'y': y}},
            {'circle': {'radius': height * 0.2, 'angle': -30}},
        ],
        '0': [
            {'break': {'x': x, 'y': y + (height / 4)}},
            {'circle': {'radius': (width / 2), 'angle': 180, 'rotation': 90}},
            {'draw': {'x': x + width, 'y': y + (height * 0.75)}},
            {'circle': {'radius': (width / 2), 'angle': 180}},
            {'draw': {'x': x, 'y': y + (height * 0.25)}},
            {'draw': {'x': x + width, 'y': y + (height * 0.75)}}
        ],
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
            {'draw': {'x': x - (width * 0.1), 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + (height * 0.9)}},
            {'break': {'x': x, 'y': y + (height / 2)}},
            {'draw': {'x': x + (width / 2), 'y': y + (height / 2)}},
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x + (width / 2), 'y': y}},
            {'circle': {'radius': (width / 2), 'angle': 182}},
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x - (width * 0.1), 'y': y}}
        ],
        'v': [
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x, 'y': y + height}},
            {'draw': {'x': x - (width * 0.1), 'y': y + height}},
            {'draw': {'x': x + (width * 0.2), 'y': y + height}},
            {'circle': {'radius': - (height * 0.2), 'angle': 180}},
            {'draw': {'x': x , 'y': y + (height * 0.6)}},
            {'draw': {'x': x + (width * 0.4), 'y': y + (height * 0.6)}},
            {'circle': {'radius': -(height * 0.3), 'angle': 180, 'rotation': 180}},
            {'draw': {'x': x - (width * 0.1), 'y': y}}
        ],
        'g': [
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x, 'y': y + height}},
            {'draw': {'x': x - (width * 0.1), 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + (height * 0.9)}},
            {'break': {'x': x - (width * 0.1), 'y': y}},
            {'draw': {'x': x + (width * 0.1) , 'y': y}}
        ], 
        'd': [
            {'break': {'x': x, 'y': y }},
            {'draw': {'x': x + width , 'y': y }},
            {'break': {'x': x + (width * 0.1), 'y': y}},
            {'circle': {'radius': (width * 0.05), 'angle': 90}},
            {'draw': {'x': x + (width * 0.15), 'y': y + height}},
            {'draw': {'x': x + (width * 0.85), 'y': y + height}},
            {'draw': {'x': x + (width * 0.85), 'y': y}},    
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x, 'y': y - (height * 0.2)}},
            {'break': {'x': x - (width * 0.1), 'y': y - (height * 0.2)}},
            {'draw': {'x': x + (width * 0.1), 'y': y - (height * 0.2)}},
            {'break': {'x': x + width, 'y': y}},
            {'draw': {'x': x + width, 'y': y - (height * 0.2)}},
            {'break': {'x': x + (width * 0.9), 'y': y - (height * 0.2)}},
            {'draw': {'x': x + (width * 1.1), 'y': y - (height * 0.2)}}
        ],
        ']': [ #slovo Đ
            {'break': {'x': x + (width * 0.2), 'y': y}},
            {'draw': {'x': x + (width * 0.2), 'y': y + height}},
            {'break': {'x': x, 'y': y + (height * 0.9)}},
            {'draw': {'x': x, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + (height * 0.9)}},
            {'break': {'x': x + (width * 0.2), 'y': y + (height * 0.4)}},
            {'circle': {'radius': -(width * 0.4), 'angle': 180, 'rotation': 270}},
            {'draw': {'x': x + width, 'y': y - (height * 0.1)}},
            {'circle': {'radius': -(width * 0.4), 'angle': 90, 'rotation': 0}},
            {'break': {'x': x + (width * 0.1), 'y': y}},
            {'draw': {'x': x + (width * 0.3), 'y': y}},
            {'break': {'x': x + (width * 0.1), 'y': y + (height * 0.8)}},
            {'draw': {'x': x + (width * 0.3), 'y': y + (height * 0.8)}},
            {'break': {'x': x + (width * 0.6), 'y': y - (height * 0.25)}},
            {'draw': {'x': x + (width * 0.6), 'y': y - (height * 0.35)}}
        ], 
        'e': [
            {'break': {'x': x - (width * 0.1), 'y': y}},
            {'draw': {'x': x, 'y': y}},
            {'draw': {'x': x, 'y': y + height}},
            {'draw': {'x': x - (width * 0.1), 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + (height * 0.9)}},
            {'break': {'x': x, 'y': y + (height * 0.5)}},
            {'draw': {'x': x + (width * 0.8), 'y': y + (height * 0.5)}},
            {'draw': {'x': x + (width * 0.8), 'y': y + (height * 0.6)}},
            {'draw': {'x': x + (width * 0.8), 'y': y + (height * 0.4)}},
            {'break': {'x': x, 'y': y}},
            {'draw': {'x': x + width, 'y': y}},
            {'draw': {'x': x + width, 'y': y + (height * 0.1)}}
        ],
        '\\': [ #slovo Ž
            {'break': {'x': x + (width / 2), 'y': y}},
            {'draw': {'x': x + (width / 2), 'y': y + height}},
            {'break': {'x': x, 'y': y + (height /2)}},
            {'draw': {'x': x + width, 'y': y + (height /2)}},
            {'break': {'x': x + (width * 0.2), 'y': y + (height * 0.1)}},
            {'draw': {'x': x + (width * 0.2), 'y': y + (height * 0.9)}},
            {'circle': {'radius': y + (height * 0.1), 'angle': 90, 'rotation': 270}},
            {'draw': {'x': x, 'y': y + (height * 0.9)}},
            {'break': {'x': x, 'y': y + (height * 0.1)}},
            {'draw': {'x': x, 'y': y}},
            {'circle': {'radius': y + (height * 0.1), 'angle': 90, 'rotation': 180}},
            {'break': {'x': x + (width * 0.8), 'y': y + (height * 0.1)}},
            {'draw': {'x': x + (width * 0.8), 'y': y + (height * 0.9)}},
            {'circle': {'radius': -(y + (height * 0.1)), 'angle': 90}},
            {'draw': {'x': x + width, 'y': y + (height * 0.9)}},
            {'break': {'x': x + width, 'y': y + (height * 0.1)}},
            {'draw': {'x': x + width, 'y': y}},
            {'circle': {'radius': -(y + (height * 0.1)), 'angle': 90, 'rotation': 180}},
            {'break': {'x': x + (width * 0.4), 'y': y}},
            {'draw': {'x': x + (width * 0.6), 'y': y}},
            {'break': {'x': x + (width * 0.4), 'y': y + height}},
            {'draw': {'x': x + (width * 0.6), 'y': y + height}}
        ],
        'z': [
            {'break': {'x': x + (width / 2), 'y': y + (height / 2)}},
            {'circle': {'radius': -(height * 0.25), 'angle': 270}},
            {'break': {'x': x + (width / 2), 'y': y + (height / 2)}},
            {'circle': {'radius': (height * 0.25), 'angle': 270, 'rotation': 90}},
            {'break': {'x': x - (width * 0.1), 'y': y + (height * 0.75)}},
            {'draw': {'x': x + (width * 0.1), 'y': y + (height * 0.75)}},
            {'break': {'x': x - (width * 0.1), 'y': y + (height * 0.25)}},
            {'draw': {'x': x + (width * 0.1), 'y': y + (height * 0.25)}}
        ],
        'i': [
            {'break': {'x': x, 'y': y + height}},
            {'draw': {'x': x, 'y': y}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y}},
            {'break': {'x': x - (width * 0.1), 'y': y + height}},
            {'draw': {'x': x + (width * 0.1), 'y': y + height}},
            {'break': {'x': x + (width * 0.9), 'y': y}},
            {'draw': {'x': x + (width * 1.1), 'y': y}}
        ],
        'j': [
            {'break': {'x': x, 'y': y + height}},
            {'draw': {'x': x, 'y': y + (height * 0.8)}},
            {'break': {'x': x, "y": y + height}},
            {'draw': {'x': x + (width * 1.2), "y": y + height}},
            {'break': {'x': x + width, "y": y + height}},
            {'draw': {'x': x + width, "y": y + (height * 0.24)}},
            {'break': {'x': x , "y": y + (height * 0.25)}},
            {'circle': {'radius': width * 0.5, 'angle': 180, "rotation": 90}},
            {'break': {'x': x , "y": y + (height * 0.25)}},
            {'draw': {'x': x , "y": y + (height * 0.3)}},
            {'break': {'x': x - (width * 0.1) , "y": y + (height * 0.3)}},
            {'draw': {'x': x + (width * 0.1) , "y": y + (height * 0.3)}}
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
        'l': [
            {'break': {'x': x + width, 'y': y}}, 
            {'draw': {'x': x + width, 'y': y + height}},
            {'break': {'x': x + (width * 1.1), 'y': y + height}},
            {'draw': {'x': x + (width * 0.3), 'y': y + height}},
            {'draw': {'x': x + (width * 0.4), 'y': y + height}},
            {'draw': {'x': x + (width * 0.4), 'y': y + (height * 0.1)}},
            {'circle': {'radius': -(width * 0.2), 'angle': 180, 'rotation': 90}},
            {'break': {'x': x - (width * 0.1), 'y': y + (height * 0.1)}},
            {'draw': {'x': x + (width * 0.1), 'y': y + (height * 0.1)}},
            {'break': {'x': x + (width * 0.9), 'y': y}},
            {'draw': {'x': x + (width * 1.1), 'y': y}}
        ],
        'q': [ #slovo Lj
        
            ### WIDTH = 1.6W ###
            {'break': {'x': x + width, 'y': y}}, 
            {'draw': {'x': x + width , 'y': y + height}},
            {'break': {'x': x + (width * 1.1), 'y': y + height}},
            {'draw': {'x': x + (width * 0.3), 'y': y + height}},
            {'draw': {'x': x + (width * 0.4), 'y': y + height}},
            {'draw': {'x': x + (width * 0.4), 'y': y + (height * 0.1)}},
            {'circle': {'radius': -(width * 0.2), 'angle': 180, 'rotation': 90}},
            {'break': {'x': x + (width * 0.9), 'y': y}},
            {'draw': {'x': x + (width * 1.1), 'y': y}},
            {'circle': {'radius': (width / 2), 'angle': 182, 'rotation': -90}},
            {'draw': {'x': x + width, 'y': y + (height / 2)}},
            {'break': {'x': x - (width * 0.1), 'y': y + (height * 0.1)}},
            {'draw': {'x': x + (width * 0.1), 'y': y + (height * 0.1)}}

            ### WIDTH = 1W ###
            # {'break': {'x': x + (width * 0.6), 'y': y}}, 
            # {'draw': {'x': x + (width * 0.6) , 'y': y + height}},
            # {'break': {'x': x + (width * 0.7), 'y': y + height}},
            # {'draw': {'x': x + (width * 0.1), 'y': y + height}},
            # {'draw': {'x': x + (width * 0.2), 'y': y + height}},
            # {'draw': {'x': x + (width * 0.2), 'y': y + (height * 0.05)}},
            # {'circle': {'radius': -(width * 0.1), 'angle': 180, 'rotation': 90}},
            # {'break': {'x': x + (width * 0.5), 'y': y}},
            # {'draw': {'x': x + (width * 0.65), 'y': y}},
            # {'circle': {'radius': width * 0.35, 'angle': 182, 'rotation': -90}},
            # {'draw': {'x': x + (width * 0.6), 'y': y + (height * 0.35)}},
            # {'break': {'x': x - (width * 0.1), 'y': y + (height * 0.05)}},
            # {'draw': {'x': x + (width * 0.1), 'y': y + (height * 0.05)}}
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
            {'break': {'x': x - (width * 0.1),'y': y + height}},
            {'draw': {'x': x + (width * 0.1),'y': y + height}},
            {'break': {'x': x + (width * 0.9) , 'y': y}},
            {'draw': {'x': x + (width * 1.1) , 'y': y}},        
            {'break': {'x': x + (width * 0.9), 'y': y + height}},
            {'draw': {'x': x + (width * 1.1),'y': y + height}},
            {'break': {'x': x - (width * 0.1) , 'y': y}},
            {'draw': {'x': x + (width * 0.1),'y': y}}
        ],
        'w': [ #slovo Nj
            {'break': {'x': x, 'y': y}},
            {'draw': {'x' : x, 'y': y + height}},
            {'break': {'x': x, 'y': y + (height / 2)}},

            ### WIDTH = 1.7W?? ###
            {'draw': {'x': x + (width * 1.2), 'y': y + (height / 2)}},
            {'break': {'x': x + width, 'y': y + height}},
            {'draw': {'x': x + width,'y': y}},
            {'break': {'x': x + (width * 0.9) , 'y': y}},
            {'draw': {'x': x + (width * 1.2) , 'y': y}},
            {'circle': {'radius': (width / 2), 'angle': 182}},
            {'break': {'x': x - (width * 0.1),'y': y + height}},
            {'draw': {'x': x + (width * 0.1),'y': y + height}},      
            {'break': {'x': x + (width * 0.9), 'y': y + height}},
            {'draw': {'x': x + (width * 1.1),'y': y + height}},
            {'break': {'x': x - (width * 0.1) , 'y': y}},
            {'draw': {'x': x + (width * 0.1),'y': y}}

            ### WIDTH = 1W ###
            # {'draw': {'x': x + (width * 0.5), 'y': y + (height / 2)}},
            # {'break': {'x': x + (width * 0.4), 'y': y + height}},
            # {'draw': {'x': x + (width * 0.4),'y': y}},
            # {'break': {'x': x + (width * 0.3) , 'y': y}},
            # {'draw': {'x': x + (width * 0.5) , 'y': y}},
            # {'circle': {'radius': (width / 2), 'angle': 182}},
            # {'break': {'x': x - (width * 0.1),'y': y + height}},
            # {'draw': {'x': x + (width * 0.1),'y': y + height}},      
            # {'break': {'x': x + (width * 0.3), 'y': y + height}},
            # {'draw': {'x': x + (width * 0.5),'y': y + height}},
            # {'break': {'x': x - (width * 0.1) , 'y': y}},
            # {'draw': {'x': x + (width * 0.1),'y': y}}
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
            {'draw': {'x': x - (width * 0.1), 'y': y + height}},
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
        '\'': [ #slovo Ć
            {'break': {'x': x + (width * 0.2), 'y': y}},
            {'draw': {'x': x + (width * 0.2), 'y': y + height}},
            {'break': {'x': x, 'y': y + (height * 0.9)}},
            {'draw': {'x': x, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y + (height * 0.9)}},
            {'break': {'x': x + (width * 0.2), 'y': y + (height * 0.4)}},
            {'circle': {'radius': -(width * 0.4), 'angle': 180, 'rotation': 270}},
            {'draw': {'x': x + width, 'y': y}},
            {'break': {'x': x + (width * 0.1), 'y': y}},
            {'draw': {'x': x + (width * 0.3), 'y': y}},
            {'break': {'x': x + (width * 0.1), 'y': y + (height * 0.8)}},
            {'draw': {'x': x + (width * 0.3), 'y': y + (height * 0.8)}},
            {'break': {'x': x + (width * 0.9), 'y': y}},
            {'draw': {'x': x + (width * 1.1), 'y': y}}
        ],
        'u': [
            {'break': {'x': x, 'y': y + (height * 0.15)}},
            {'circle': {'radius': (width * 0.3), 'angle': 160, 'rotation': 90}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'break': {'x': x + (width * 0.73), 'y': y + (height * 0.45)}},
            {'draw': {'x': x, 'y': y + height}},
            {'break': {'x': x - (width * 0.1), 'y': y + height}},
            {'draw': {'x': x + (width * 0.1), 'y': y + height}},
            {'break': {'x': x + (width * 0.9), 'y': y + height}},
            {'draw': {'x': x + (width * 1.1), 'y': y + height}},
            {'break': {'x': x - (width * 0.1), 'y': y + (height * 0.15)}},
            {'draw': {'x': x + (width * 0.1), 'y': y + (height * 0.15)}}
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
        ],
        'h': [
            {'break': {'x': x , 'y': y}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'break': {'x': x, 'y': y + height}},
            {'draw': {'x': x + width, 'y': y}},
            {'break': {'x': x - (width * 0.1) , 'y': y}},
            {'draw': {'x': x + (width * 0.1) , 'y': y}},
            {'break': {'x': x - (width * 0.1) , 'y': y + height}},
            {'draw': {'x': x + (width * 0.1) , 'y': y + height}},
            {'break': {'x': x + (width * 0.9) , 'y': y}},
            {'draw': {'x': x + (width * 1.1) , 'y': y}},
            {'break': {'x': x + (width * 0.9) , 'y': y + height}},
            {'draw': {'x': x + (width * 1.1) , 'y': y + height}}
        ], 
        'c': [
            {'break': {'x': x - (width * 0.1) , 'y': y + height}},
            {'draw': {'x': x + (width * 0.1) , 'y': y + height}},
            {'break': {'x': x , 'y': y + height}},
            {'draw': {'x': x , 'y': y}},
            {'draw': {'x': x + width , 'y': y}},
            {'break': {'x': x + (width * 0.7) , 'y': y + height}},
            {'draw': {'x': x + (width * 0.9) , 'y': y + height}},
            {'break': {'x': x + (width * 0.8), 'y': y + height}},
            {'draw': {'x': x + (width * 0.8), 'y': y}},
            {'break': {'x': x + width, 'y': y}},
            {'draw': {'x': x + width, 'y': y - (height * 0.2)}},
            {'break': {'x': x + (width * 0.9), 'y': y - (height * 0.2)}},
            {'draw': {'x': x + (width * 1.1), 'y': y - (height * 0.2)}}
        ],
        ';': [ #slovo Č
            {'break': {'x': x + width, 'y': y}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'break': {'x': x + width, 'y': y + (height * 0.6)}},
            {'circle': {'radius': -(height * 0.1), 'angle': 90, 'rotation': 90}},
            {'draw': {'x': x + (width * 0.2), 'y': y + (height / 2)}},
            {'circle': {'radius': -(height * 0.1), 'angle': 90}},
            {'draw': {'x': x, 'y': y + height}},
            {'break': {'x': x - (width * 0.1), 'y': y + height}},
            {'draw': {'x': x + (width * 0.1), 'y': y + height}},
            {'break': {'x': x + (width * 0.9), 'y': y + height}},
            {'draw': {'x': x + (width * 1.1), 'y': y + height}},
            {'break': {'x': x + (width * 0.9), 'y': y}},
            {'draw': {'x': x + (width * 1.1), 'y': y}}
        ],
        'x': [ #slovo Dž
            {'break': {'x': x, "y": y}},
            {'draw': {'x': x, "y": y + height}},
            {'break': {'x': x - (width * 0.1), "y": y + height}},
            {'draw': {'x': x + (width * 0.1), "y": y + height}},
            {'break': {'x': x + (width * 0.5), "y": y}},
            {'draw': {'x': x + (width * 0.5), "y": y - (height * 0.2)}},
            {'break': {'x': x + (width * 0.4), "y": y - (height * 0.2)}},
            {'draw': {'x': x + (width * 0.6), "y": y - (height * 0.2)}},
            {'break': {'x': x, "y": y}},
            {'draw': {'x': x + width, "y": y}},
            {'draw': {'x': x + width, "y": y + height}},
            {'break': {'x': x + (width * 0.9), "y": y + height}},
            {'draw': {'x': x + (width * 1.1), "y": y + height}}
        ], 
        '[': [ #slovo Š
            {'break': {'x': x , 'y': y}},
            {'draw': {'x': x , 'y': y + height}},
            {'break': {'x': x - (width * 0.1) , 'y': y + height}},
            {'draw': {'x': x + (width * 0.1) , 'y': y + height}},
            {'break': {'x': x , 'y': y}},
            {'draw': {'x': x + width, 'y': y}},
            {'break': {'x': x + (width * 0.5) , 'y': y}},
            {'draw': {'x': x + (width * 0.5), 'y': y + height}},
            {'break': {'x': x + (width * 0.4) , 'y': y + height}},
            {'draw': {'x': x + (width * 0.6) , 'y': y + height}},
            {'break': {'x': x + width, 'y': y}},
            {'draw': {'x': x + width, 'y': y + height}},
            {'break': {'x': x + (width * 0.9) , 'y': y + height}},
            {'draw': {'x': x + (width * 1.1) , 'y': y + height}}

        ],
    }