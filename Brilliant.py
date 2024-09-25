def draw_diagram(rows):
    for i in range(rows):
        # Print spaces
        for j in range(i):
            print(" ", end=" ")
        
        # Print asterisks
        for k in range(rows - i):
            print("*", end=" ")
        
        print()  # Move to the next line

# Adjust the value of 'rows' to change the size of the diagram
draw_diagram(5)
