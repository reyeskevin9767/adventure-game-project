_world = {}
starting_position = (0, 0)


def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('./resources/map.txt', 'r') as f:
        rows = f.readlines()
    # Assumes all rows contain the same number of tabs
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            # Windows users may need to replace '\r\n'
            tile_name = cols[x].replace('\r\n', '')
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            if tile_name == '':
                _world[(x, y)] = None
            else:
                getattr(__import__('tiles'), tile_name)(x, y)


def tile_exists(x, y):
    return _world.get((x, y))
