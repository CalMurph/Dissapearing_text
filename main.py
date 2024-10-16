from tkinter import *
from PIL import ImageTk, Image


class SpyTextApp:
    def __init__(self):
        self.text_box = None
        self.logo_img = None
        self.timer_id = None
        self.count = 5
        self.font = ("Courier", 24)
        self.img = None
        self.canvas = None
        self.button = None
        self.mission_canvas = None
        self.mission_text = None
        self.message_text = ("Dear Agent, our field agents are in grave peril.\nHostile forces are closing in, and they"
                             "\nare in desperate need of your expertise and\nprecise instructions to navigate through"
                             " the\ncurrent threat. Time is of the essence.\n\nYour mission is to provide critical"
                             " instructions\nto ensure their safe extraction. Due to the highly\nsensitive"
                             " nature of this operation, the message\nyou compose will be top secret and will\n"
                             "SELF_DESTRUCT after five seconds. This precaution\nis necessary to prevent any possibility"
                             " of our\ndirectives falling into the wrong hands.\n\nPlease type your instructions in the"
                             " provided\nprompt. Remember, after five seconds,\nyour message will be deleted permanently.\n\n"
                             "Pay close attention and proceed with caution.\n\nStay vigilant,\n\nM")
        self.timer = False
        self.window = Tk()
        self.window.title("Top Secret")
        self.render_home()
        self.window.bind('<Key>', self.start_timer)
        self.window.mainloop()

    def render_home(self):
        self.window.config(bg="black")

        self.canvas = Canvas(self.window, height=400, width=400, bg="black", highlightbackground="black")
        try:
            self.img = ImageTk.PhotoImage(Image.open('spy_photo.png'))
            self.logo_img = self.canvas.create_image(200, 200, image=self.img)
        except FileNotFoundError:
            print("File does not exist. Download your own image and run again.")

        self.canvas.grid(column=0, row=0, padx=20)

        self.button = Button(self.window, text="Start Mission", font=('Arial', 20), command=self.start_mission)
        self.button.config(bd=0, highlightbackground="white", bg='black', fg='black', pady=5, padx=5)
        self.button.grid(column=0, row=1, pady=(30, 40))

    def start_mission(self):
        self.button.destroy()
        self.canvas.destroy()
        self.window.geometry('750x750')

        self.mission_canvas = Canvas(self.window, height=600, width=740, bg="black", highlightbackground="black")
        self.mission_canvas.grid(column=0, row=0)
        self.mission_text = self.mission_canvas.create_text(10, 10, text=self.message_text, anchor=NW, font=self.font,
                                                            fill="darkgreen")

        self.text_box = Text(self.window, background="black", font=self.font, fg="white", width=40, height=4,
                             highlightbackground="darkgreen")
        self.text_box.grid(column=0, row=1)

    def start_timer(self, event):
        self.reset_timer()
        print(event)

    def reset_timer(self):
        if self.timer_id is not None:
            self.window.after_cancel(self.timer_id)
        self.count = 5
        self.count_down()

    def count_down(self):
        if self.count > 0:
            self.count -= 1
            self.timer_id = self.window.after(1000, self.count_down)
        else:
            self.text_box.config(bg="darkred", fg="black")
            self.window.update()
            self.text_box.delete('1.0', END)
            self.window.after(1000, self.delete_text)

    def delete_text(self):
        self.text_box.delete('1.0', END)
        self.text_box.config(bg="black", fg="white")
        self.window.update()  # Force update to show black background immediately
        self.window.after(500, self.start_mission)


if __name__ == "__main__":
    app = SpyTextApp()
