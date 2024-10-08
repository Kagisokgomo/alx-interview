def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Start a new row with 1
        row = [1] * (i + 1)  # Create a row of 'i+1' elements initialized to 1

        # Calculate the values for the inner elements of the row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)  # Append the constructed row to the triangle

    return triangle
