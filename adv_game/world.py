_world = {}
starting_position = (0, 0)


def tile_exists(x, y):
    """Returns the tile at the given coordinates or None if there is no tile.
    :param x: the x-coordinate in the world
    :param y: the y-coordinate in the world
    """
    return _world.get((x, y))


def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()            # Place all tiles into a array
    x_max = len(rows[0].split('\t'))    # Find the number of tiles pre-row
    for y in range(len(rows)):
        cols = rows[y].split('\t')      # Sepreate each row into a array
        for x in range(x_max):
            # Replae the newline character in any tile name
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            # Get tile instances and place into the world
            if tile_name == '':
                _world[(x, y)] = None
            else:
                getattr(__import__('tiles'), tile_name)(x, y)
