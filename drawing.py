import numpy as np
from matplotlib import pyplot as plt


def draw_circle(ax, center, radius, color, linewidth):
    circle = plt.Circle(center, radius, fill=False, color=color, linewidth=linewidth)
    ax.add_artist(circle)


def draw_circle_pattern(q, d, min_radius, max_radius, color_matrices, linewidth, output_filename,
                        index_to_hex_color_function):
    fig, ax = plt.subplots(figsize=(8, 8))

    for i in range(q):
        for j in range(q):
            center = np.array([i * d, j * d])
            for k in range(q - 1):
                color_matrix = color_matrices[k]
                color_index = color_matrix[i, j]
                color = index_to_hex_color_function(color_index)
                draw_circle(ax, center, (k + 1) * min_radius, color, linewidth)

    set_plot_properties(ax, d, max_radius, q)

    plt.savefig(output_filename, format='svg')  # Save the plot as an SVG file


def set_plot_properties(ax, d, max_radius, q):
    max_group_radius = max_radius * (q - 1)
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlim(-max_group_radius, q * d + max_group_radius)
    ax.set_ylim(-max_group_radius, q * d + max_group_radius)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'{q}*{q} Groups of Circles with Gradually Increasing Radii and Custom Colors')
