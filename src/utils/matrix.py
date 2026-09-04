

def blank():

        W = (255,255,255) # white

        return [
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        ]
        
def empty():

    B = (0, 0, 0) # black

    return [
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B,
    ]

def success():

        G = (0,255,0)   # green
        O = (0,0,0)     # off/black

        return [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, G,
        O, O, O, O, O, O, G, O,
        O, O, O, O, O, G, O, O,
        G, O, O, O, G, O, O, O,
        O, G, O, G, O, O, O, O,
        O, O, G, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]


def reject():

        R = (255,0,0)   # red
        O = (0,0,0)     # off/black

        return [
        O, O, O, O, O, O, O, O,
        O, R, O, O, O, O, R, O,
        O, O, R, O, O, R, O, O,
        O, O, O, R, R, O, O, O,
        O, O, O, R, R, O, O, O,
        O, O, R, O, O, R, O, O,
        O, R, O, O, O, O, R, O,
        O, O, O, O, O, O, O, O,
        ]