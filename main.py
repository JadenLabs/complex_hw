"""Hello world.
"""
from rich.console import Console
from rich.theme import Theme

my_theme = Theme(
    {
        "h_1": "#2a3a58",
        "e_1": "#214b6d",
        "l_1": "#005c80",
        "l_2": "#006e8f",
        "o_1": "#00819a",
        "c_1": "#00939f",
        "s_1": "#00a5a0",
        "w_1": "#00b69b",
        "o_2": "#38c793",
        "r_1": "#6cd688",
        "l_3": "#9ae47d",
        "d_1": "#c9f073",
        "ex_1": "#fafa6e",
    }
)
console = Console(theme=my_theme)


class PrintChars:
    """Chars the prints"""

    def __init__(self) -> None:
        # String
        self.world_the_hello = "Hello, world!"

        # Chars
        self.chars = {
            "H": self.print_h,
            "e": self.print_e,
            "l": self.print_l,
            "l_2": self.print_l_2,
            "o": self.print_o,
            ",": self.print_c,
            " ": self.print_s,
            "w": self.print_w,
            "o_2": self.print_o_2,
            "r": self.print_r,
            "l_3": self.print_l_3,
            "d": self.print_d,
            "!": self.print_ex,
        }

    def print_it(self):
        """Hellos the world"""
        for value in self.chars.items():
            value[1]()
        print("\n")

    def print_h(self):
        """Print h - Chad moves."""
        console.print("H", style="h_1", end="")

    def print_e(self):
        """Print e - Boss moves."""
        console.print("e", style="e_1", end="")

    def print_l(self):
        """Print l - God moves."""
        console.print("l", style="l_1", end="")

    def print_l_2(self):
        """Print l - Alpha moves."""
        console.print("l", style="l_2", end="")

    def print_o(self):
        """Print o - Beta moves."""
        console.print("o", style="o_1", end="")

    def print_c(self):
        """Print comma - Gamma moves."""
        console.print(",", style="c_1", end="")

    def print_s(self):
        """Print space - EA moves."""
        console.print(" ", style="s_1", end="")

    def print_w(self):
        """Print w - idk moves."""
        console.print("w", style="w_1", end="")

    def print_o_2(self):
        """Print o - Help moves."""
        console.print("o", style="o_2", end="")

    def print_r(self):
        """Print r - Omega moves."""
        console.print("r", style="r_1", end="")

    def print_l_3(self):
        """Print l - Rad moves."""
        console.print("l", style="l_3", end="")

    def print_d(self):
        """Print d - Dork moves."""
        console.print("d", style="d_1", end="")

    def print_ex(self):
        """Print exlaimation - Crazy moves."""
        console.print("!", style="ex_1", end="")


if __name__ == "__main__":
    # World helloer class
    PrintChars().print_it()
