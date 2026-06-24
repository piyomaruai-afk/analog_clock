
class ThemeManager:
    def __init__(self,root):
        self.root=root
        self.dark=True

    def toggle(self):
        self.dark=not self.dark

        self.root.configure(
            bg="#111" if self.dark else "white"
        )
