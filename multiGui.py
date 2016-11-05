import tkinter as tk   # python3
#import gui
#import Tkinter as tk   # python

TITLE_FONT = ("Helvetica", 18, "bold")

class gui_Frame(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (fileInputFrame, commandSelectFrame, commandOptionsFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("fileInputFrame")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class fileInputFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please enter the file path", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        inputBox = tk.Entry(self)
        inputBox.pack()
        #fslt(parent = controller, controller = self
        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("commandSelectFrame"))
        #button2 = tk.Button(self, text="Go to Page Two",
             #               command=lambda: controller.show_frame("commandOptionsFrame"))
        button1.pack(side = "bottom", padx = 10)
        #button2.pack(side = "right", padx = 20)


class commandSelectFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please select which commands to run from each section:", font = 'Helvetica 12')
        label.pack(side="top", fill="x", pady=10)
        fsltLabel = tk.Label(self, text="File System Layer Tools", font='Helvetica 14 bold')
        fsltLabel.pack(side = "top", fill = "x")

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("fileInputFrame"))
        button.pack(side = "bottom")

        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("commandOptionsFrame"))
        button2.pack(side="right", padx=20)


class commandOptionsFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Options for the commands selected", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("fileInputFrame"))

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("commandSelectFrame"))

        button1.pack(side = 'right')

        button.pack(side = 'bottom')


if __name__ == "__main__":
    app = gui_Frame()
    app.title("SleuthKit Visualizer")
    app.geometry("900x800")
    app.mainloop()