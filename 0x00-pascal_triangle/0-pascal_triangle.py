def pascal_triangle(n):
    """Generate Pascal's triangle with n rows."""
    if n <= 0:
        return []
    
    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1] + [prev[j] + prev[j+1] for j in range(len(prev)-1)] + [1]
        triangle.append(row)
    return triangle

def print_pyramid(triangle):
    """Print Pascal's triangle in a nicely centered pyramid format."""
    if not triangle:
        print("[]")
        return
    max_width = len("   ".join(map(str, triangle[-1])))
    for row in triangle:
        row_str = "   ".join(map(str, row))
        print(row_str.center(max_width))

# Example usage
n = 5  # change this to generate more rows
triangle = pascal_triangle(n)
print_pyramid(triangle)
