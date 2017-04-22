import os


class OutletHandler:
    def __init__(self):
        self.gpio_dict = {1: [16, 26], 2: [12, 20], 3: [21, 19], 4: [13, 6]}
        for key in self.gpio_dict:
            os.system("sudo sh outlet_setup.sh " + str(self.gpio_dict[key][0]) + " " + str(self.gpio_dict[key][1])) #setup all outlets

    def turn_on(self, outlet_num):
        if outlet_num in range(1, len(self.gpio_dict) + 1):
            os.system("sudo sh outlet_trigger.sh " + str(self.gpio_dict[outlet_num][0]))
        else:
            print("INVALID OUTLET")

    def turn_off(self, outlet_num):
        if outlet_num in range(1, len(self.gpio_dict) + 1):
            os.system("sudo sh outlet_trigger.sh " + str(self.gpio_dict[outlet_num][1]))
        else:
            print("INVALID OUTLET")