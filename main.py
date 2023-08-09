from drawing import draw_circle_pattern
from generate_color_matrices import generate_color_matrix
from color_maps import index_to_hex_color


q = 9
d = 6
min_radius = 0.3
max_radius = 2
linewidth = 1
output_filename = 'output.svg'  # Specify the output SVG filename

color_matrices = [
    generate_color_matrix(q, k) for k in range(1, q)
]

draw_circle_pattern(q, d, min_radius, max_radius, color_matrices, linewidth, output_filename, index_to_hex_color)
