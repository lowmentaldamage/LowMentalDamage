# Theatre Square:
# Pave an n × m meter rectangle with a × a square flagstones.
# - Cannot break flagstones → must use whole ones.
# - Must fully cover the rectangle (overhang is allowed).
# - Stones must be axis-aligned (no rotation needed — just grid placement).

#   lenght of rectangle
#   Width of rectangle
#   The Flag stone size
n, m, a = map(int, input().split())

#   Calculating the size of theatre square
theatre_size = n * m 
# m is length
# n is width

#   Calculating the size of a tile
tile = a * a

# Number of flagstones along the n side (ceiling division)
tiles_n = (n + a - 1) // a

# Number of flagstones along the m side (ceiling division)
tiles_m = (m + a - 1) // a

# Print total flagstones required (product of counts along each side)
print(tiles_n * tiles_m)
