import customtkinter as ctk
from Temp import format_temp, get_colour

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class TemperatureApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Temperature")
        self.geometry("360x320")
        self.resizable(False, False)

        self.celsius = 20.0
        self.unit = "C"

        # Title
        ctk.CTkLabel(self, text="Current Temperature",
                     font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(25, 5))

        # Big temperature display
        self.temp_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=56, weight="bold"))
        self.temp_label.pack(pady=10)

        # Slider to change the temperature (in Celsius)
        self.slider = ctk.CTkSlider(self, from_=-20, to=50, number_of_steps=70,
                                    command=self.on_slide)
        self.slider.set(self.celsius)
        self.slider.pack(pady=10, padx=30, fill="x")

        # Toggle between °C and °F
        self.unit_switch = ctk.CTkSegmentedButton(self, values=["°C", "°F"],
                                                  command=self.on_unit_change)
        self.unit_switch.set("°C")
        self.unit_switch.pack(pady=15)

        self.update_display()

    def on_slide(self, value):
        self.celsius = float(value)
        self.update_display()

    def on_unit_change(self, value):
        self.unit = "C" if value == "°C" else "F"
        self.update_display()

    def update_display(self):
        self.temp_label.configure(text=format_temp(self.celsius, self.unit),
                                  text_color=get_colour(self.celsius))


if __name__ == "__main__":
    app = TemperatureApp()
    app.mainloop()