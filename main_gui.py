import tkinter as tk
from tkinter import messagebox
from red_black_tree import RedBlackTree, Node

class RedBlackTreeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Red-Black Tree Simulator")
        
        # Initialize the Red-Black Tree
        self.rbtree = RedBlackTree()
        
        # Canvas settings
        self.canvas_width = 1200
        self.canvas_height = 600
        self.node_radius = 20
        self.vertical_gap = 60
        
        # Create GUI elements
        self.create_gui_elements()
        
    def create_gui_elements(self):
        # Top frame for input
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        # Input field
        tk.Label(input_frame, text="Enter value:").pack(side=tk.LEFT, padx=5)
        self.value_entry = tk.Entry(input_frame, width=10)
        self.value_entry.pack(side=tk.LEFT, padx=5)
        
        # Insert button
        tk.Button(input_frame, text="Insert", command=self.insert_value).pack(side=tk.LEFT, padx=5)
        
        # Delete button
        tk.Button(input_frame, text="Delete", command=self.delete_value).pack(side=tk.LEFT, padx=5)
        
        # Find button
        tk.Button(input_frame, text="Find", command=self.find_value).pack(side=tk.LEFT, padx=5)
        
        # Clear button
        tk.Button(input_frame, text="Clear Tree", command=self.clear_tree).pack(side=tk.LEFT, padx=5)
        
        # Canvas for tree visualization
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack(pady=10)
        
    def insert_value(self):
        try:
            value = int(self.value_entry.get())
            self.rbtree.insert(value)
            self.value_entry.delete(0, tk.END)
            self.draw_tree()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer")
            
    def delete_value(self):
        try:
            value = int(self.value_entry.get())
            self.rbtree.delete(value)
            self.value_entry.delete(0, tk.END)
            self.draw_tree()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer")
            
    def find_value(self):
        try:
            value = int(self.value_entry.get())
            node = self.rbtree.find(value)
            if node:
                messagebox.showinfo("Found", f"Node {value} found!")
            else:
                messagebox.showinfo("Not Found", f"Node {value} not found.")
            self.value_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer")
        
    def clear_tree(self):
        self.rbtree = RedBlackTree()
        self.canvas.delete("all")
        
    def draw_tree(self):
        self.canvas.delete("all")
        if self.rbtree.root != self.rbtree.TNULL:
            self._draw_node(self.rbtree.root, self.canvas_width//2, 50, self.canvas_width//4)
            
    def _draw_node(self, node, x, y, offset):
        if node == self.rbtree.TNULL:
            return
            
        # Draw node circle
        color = node.color.lower()
        self.canvas.create_oval(x-self.node_radius, y-self.node_radius,
                              x+self.node_radius, y+self.node_radius,
                              fill=color)
        
        # Draw node value
        self.canvas.create_text(x, y, text=str(node.key), fill='white' if color == 'black' else 'black')
        
        # Draw left child
        if node.left != self.rbtree.TNULL:
            child_x = x - offset
            child_y = y + self.vertical_gap
            self.canvas.create_line(x, y+self.node_radius,
                                  child_x, child_y-self.node_radius,
                                  fill='black')
            self._draw_node(node.left, child_x, child_y, offset/2)
            
        # Draw right child
        if node.right != self.rbtree.TNULL:
            child_x = x + offset
            child_y = y + self.vertical_gap
            self.canvas.create_line(x, y+self.node_radius,
                                  child_x, child_y-self.node_radius,
                                  fill='black')
            self._draw_node(node.right, child_x, child_y, offset/2)

def main():
    root = tk.Tk()
    app = RedBlackTreeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
