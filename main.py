import tkinter as tk
from tkinter import ttk
import re


class Window:
    variables = {}
    rows = -1
    unparsed_text = '''Hello {HR or Company Name},

I am excited to apply for the {Position Title} role at {Company Name}. With a strong background as a product analyst and manager and extensive experience as a developer, I easily understand the business requirements and offer less time-consuming and more valuable solutions. In my  opinion, Cross-domain expertise greatly improves the ability to make and implement decisions 

I have a deep understanding of the game development pipeline and the collaborative work of different specialists, because of my diverse experience, including game jams. That allows me easily to connect with colleagues across the game development pipeline and contribute to team projects.

I am currently seeking a team where I can face new professional challenges and help create innovative projects like yours. I believe my skills and values ​​align well with your company's mission and look forward to the opportunity to contribute to your success.

Best regards,
Artem'''

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('CL builder')

        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, padx=20, pady=20)

        ttk.Label(self.mainframe, text='Enter your CL template').grid(columnspan=2, row=self.get_rows())
        self.entry = tk.Text(self.mainframe, width=50)
        self.entry.config(wrap=tk.WORD)
        self.entry.insert(tk.END, self.unparsed_text)
        self.entry.grid(columnspan=2, row=self.get_rows())
        self.btn = tk.Button(self.mainframe, height=1, width=10, text="Commit",
                             command=lambda: self.parse_text())
        self.btn.grid(columnspan=2, row=self.get_rows())

        self.root.mainloop()

    def get_rows(self):
        self.rows += 1
        return self.rows

    def add_value(self, match):
        text = match.replace('{', '').replace('}', '')
        row = self.get_rows()
        ttk.Label(self.mainframe, text=text).grid(column=0, row=row)
        var = tk.StringVar()
        tk.Entry(self.mainframe, textvariable=var, width=20).grid(column=1, row=row)
        self.variables[match] = var

    def process_text(self):
        text = self.unparsed_text
        matches = re.findall('{[^{}]*}', text)
        for match in matches:
            text = text.replace(match, self.variables[match].get())
        return text

    def return_text(self):
        text = self.process_text()
        self.entry.delete('1.0', tk.END)
        self.entry.insert(tk.END, text)

    def parse_text(self):
        text = self.get_text()
        matches = re.findall('{[^{}]*}', text)
        for match in matches:
            self.add_value(match)
        tk.Button(self.mainframe, height=1, width=10, text="finish",
                  command=lambda: self.return_text()).grid(column=0, row=self.get_rows())

    def get_text(self) -> str:
        self.unparsed_text = self.entry.get("1.0", tk.END)
        return self.unparsed_text


def main():
    w = Window()

if __name__ == '__main__':
    main()
