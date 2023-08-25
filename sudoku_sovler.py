import tkinter as tk

# Initialize an empty 9x9 Sudoku grid
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def solve_sudoku():
    empty_cell = find_empty_cell()
    if not empty_cell:
        return True
    
    row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(row, col, num):
            grid[row][col] = num

            if solve_sudoku():
                return True

            grid[row][col] = 0

    return False

def find_empty_cell():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def is_valid_move(row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

def update_grid():
    for i in range(9):
        for j in range(9):
            entry = entry_grid[i][j]
            value = grid[i][j]
            entry.delete(0, tk.END)
            entry.insert(0, str(value) if value != 0 else "")
            
def reset_grid():
    for i in range(9):
        for j in range(9):
            grid[i][j] = 0
            entry_grid[i][j].delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Sudoku Solver")

entry_grid = []

for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(root, width=2, font=("Helvetica", 20))
        entry.grid(row=i, column=j)
        row_entries.append(entry)
        if (i + 1) % 3 == 0 and i < 8:
            entry.grid(pady=(0, 10))
        if (j + 1) % 3 == 0 and j < 8:
            entry.grid(padx=(0, 10))
    entry_grid.append(row_entries)


solve_button = tk.Button(root, text="Solve", command=lambda: [solve_sudoku(), update_grid()])
solve_button.grid(row=9, columnspan=9)

update_grid_button = tk.Button(root, text="Update Grid", command=update_grid)
update_grid_button.grid(row=10, columnspan=9)
            
reset_button = tk.Button(root, text="Reset", command=reset_grid)
reset_button.grid(row=11, columnspan=9)

# Start the main event loop
root.mainloop()
