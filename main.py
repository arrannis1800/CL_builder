import tkinter as tk
from tkinter import ttk
import re


class Window:
    variables = {}
    rows = -1
    unparsed_text = '''Hello {HR or Company Name},

I am excited to apply for the {Position Title} role at {Company Name}. I am an experienced C++/Unreal Engine developer with a strong background in gameplay systems, UI/UX, performance optimization, and tool development. For example, at Social Quantum, I improved developer efficiency by 30% through custom QA tools and refactored legacy code to reduce maintenance time by 25%.

I am particularly impressed by {Company Name}'s work on {specific project or type of game}, and I am eager to contribute my expertise to {specific aspect: gameplay systems, UI, performance, tools, etc.}. My cross-domain experience allows me to collaborate effectively with designers, QA, and backend teams to deliver polished game features.

I am looking for a team where I can tackle new challenges and help create engaging and high-quality projects. I would welcome the opportunity to bring my skills and passion for game development to your team.

Best regards,
Artem'''

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('CL builder')

        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, padx=20, pady=20)

        ttk.Label(self.mainframe, text='Enter your CL template').grid(columnspan=2, row=self.get_rows(), sticky='w')
        self.entry = tk.Text(self.mainframe, width=50, wrap=tk.WORD, pady=10, padx=20)
        self.entry.insert(tk.END, self.unparsed_text)
        self.entry.grid(columnspan=2, row=self.get_rows())
        self.btn = tk.Button(self.mainframe, height=1, width=10, text="Parse",
                             command=lambda: self.parse_text())
        self.btn.grid(columnspan=2, row=self.get_rows(), pady=10)

        self.root.mainloop()

    def get_rows(self):
        self.rows += 1
        return self.rows

    def add_inputs(self, match):
        if match not in self.variables:
            text = match.replace('{', '').replace('}', '')
            row = self.get_rows()
            label = ttk.Label(self.mainframe, text=text, justify='center')
            label.grid(column=0, row=row, sticky="e")
            var = tk.StringVar()
            tk.Entry(self.mainframe, textvariable=var).grid(column=1, row=row, sticky="wesn", padx=10)
            self.variables[match] = var

    def process_text(self):
        text = self.unparsed_text
        for placeholder, var in self.variables.items():
            text = text.replace(placeholder, var.get())
        return text

    def return_text(self):
        text = self.process_text()
        self.entry.delete('1.0', tk.END)
        self.entry.insert(tk.END, text)

    def parse_text(self):
        text = self.get_text()
        matches = set(re.findall(r'{[^{}]*}', text))
        for match in matches:
            self.add_inputs(match)
        tk.Button(self.mainframe, height=1, width=10, text="Replace",
                  command=self.return_text).grid(columnspan=2, row=self.get_rows(), pady=10)

    def get_text(self) -> str:
        self.unparsed_text = self.entry.get("1.0", tk.END)
        return self.unparsed_text


def main():
    w = Window()

if __name__ == '__main__':
    main()
