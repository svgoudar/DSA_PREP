def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The size of the square.

    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # Your code here
    return ['*'*n for _ in range(n)]

def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The size of the square.

    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    return ["*"*n if x in [n-1,0] else "*"+" "*(n-2) +"*" for x in range(n) ]
    # return ['*'*n] + ['*'+' '*(n-2) + '*' for _ in range(1,n-1)] + ['*'*n] if n !=1 else ['*']


def generate_rectangle(n, m):
    """
    Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.

    Parameters:
    n (int): The number of rows in the rectangle.
    m (int): The number of columns in the rectangle.

    Returns:
    list: A list of strings where each string represents a row of the rectangle pattern.
    """
    # Your code here
    return ['*'*m for _ in range(n)]


def generate_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height and base of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    return ['*'*x for x in range(1,n+1)]

def generate_inverted_triangle(n):
    """
    Function to return an inverted right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height and base of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    return ["*"*x for x in range(n,0,-1)]


def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The number of rows in the pyramid.

    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here
    return [' ' * (n - i - 1) + '*'*(2*i+1)+ ' ' * (n - i - 1) for i in range(n)]


def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The number of rows in the inverted pyramid.

    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    # Your code here
    return [
        ' ' * (n-i) + '*' * (2 * i -1) + ' ' * (n-i)
        for i in range(n,0,-1)
    ]

def generate_number_triangle(n):
    """
    Function to return a right-angled triangle of repeated numbers of side n as a list of strings.

    Parameters:
    n (int): The height of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    return [f'{x}'*x for x in range(1,n+1)]


def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.

    Parameters:
    n (int): The number of rows in the triangle.

    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    # Your code here
    num=1
    pattern = []
    for i in range(1, n + 1):
        # Create each row by joining the numbers
        pattern.append(' '.join(str(num + j) for j in range(i)))
        # Update num for the next row
        num += i
    return pattern



def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The number of rows for the upper part of the diamond.

    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Your code here
    g = []
    fixed = 2 * n -1

    for i in range(n):
        first = 2*i + 1
        g.append(' '*((fixed - first)//2) + '*'*first + ' '*((fixed - first)//2))
        if fixed == first:
            g = g + g[-2::-1]
            break

    return g



def generate_right_angled_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code hereb
    return [' '*(n -x)+'*'*(x) for x in range(1,n+1)]

def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The height of the sandglass.

    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """
    # Your code here
    v = [' '*(n-x) + '*'*(2*x-1) + ' '*(n-x) for x in range(n,0,-1)]
    return v[:-1] + v[::-1]

def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    if n == 1:
        return ["*"]
    return ["*"] + ["*"+" "*(x -2)+"*" for x in range(2,n)] +["*"*n]


def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.

    Parameters:
    n (int): The height of the pyramid.

    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    # Your code here

    v = [' '.join(map(str, range(1, i + 1))) for i in range(1,n+1)]

    return [x.center(2*n -1) for x in v ]
