import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Counter")

# Create and configure the main frame
frame = tk.Frame(window)
frame.pack(padx=20, pady=20)

# Initialize counter variable
counter = tk.IntVar(value=0)

# Create minus button
minus_button = tk.Button(frame, text="-", command=lambda: counter.set(counter.get() - 1), width=3)
minus_button.pack(side=tk.LEFT, padx=5)

# Create counter label
counter_label = tk.Label(frame, textvariable=counter, width=5)
counter_label.pack(side=tk.LEFT, padx=10)

# Create plus button
plus_button = tk.Button(frame, text="+", command=lambda: counter.set(counter.get() + 1), width=3)
plus_button.pack(side=tk.LEFT, padx=5)

# Start the main event loop
window.mainloop()
