def radius_sum(r1, r2):
    return r1 + r2


def has_intersection(x1, y1, r1, x2, y2, r2):
    distance_sq = (x1 - x2)**2 + (y1 - y2)**2
    radius_sum_sq = (r1 + r2)**2
    return distance_sq <= radius_sum_sq
