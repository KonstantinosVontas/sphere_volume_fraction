from asyncore import write
import overlap
import numpy as np
import csv




def random_points_generator():

    number_of_points = 10000
    maximum_coordinate_value = 0.995

    points = (np.random.rand(number_of_points, 3) * (2 * maximum_coordinate_value)) - maximum_coordinate_value

    return points


def generate_cube_from_center(point):

    h = 0.01

    cube_vertices = np.array((
        (point[0] - h / 2, point[1] - h / 2, point[2] - h / 2),
        (point[0] + h / 2, point[1] - h / 2, point[2] - h / 2),
        (point[0] + h / 2, point[1] + h / 2, point[2] - h / 2),
        (point[0] - h / 2, point[1] + h / 2, point[2] - h / 2),
        (point[0] - h / 2, point[1] - h / 2, point[2] + h / 2),
        (point[0] + h / 2, point[1] - h / 2, point[2] + h / 2),
        (point[0] + h / 2, point[1] + h / 2, point[2] + h / 2),
        (point[0] - h / 2, point[1] + h / 2, point[2] + h / 2),
    ))
    return cube_vertices


def find_volume_fraction(cubicle_overlap):
    maximum_volume = 1e-6

    volume_fraction = cubicle_overlap / maximum_volume

    if volume_fraction > 1:
        volume_fraction = 1

    return volume_fraction


sphere = overlap.Sphere((0, 0, 0), 1)

points = random_points_generator()

with open('cube_centers_overlap.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)

    for point in points:

        cubicle_overlap = overlap.overlap(sphere, overlap.Hexahedron(generate_cube_from_center(point)))

        # each row will have x,y,z,alpha
        row = [point[0], point[1], point[2], find_volume_fraction(cubicle_overlap)]

        writer.writerow(row)


