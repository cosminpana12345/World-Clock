import requests
from tkinter import *
from tkinter import ttk

timezones_api = requests.get('http://worldtimeapi.org/api/timezone')

timezones = timezones_api.text
mytable = timezones.maketrans("", "", '[]"')
timezones_copy = timezones.translate(mytable)
timezones_split = timezones_copy.split(",")

area = []
locations = {}
argentina = []
indiana = []
kentucky = []
north_dakota = []

for x in timezones_split:
    lista = x.split("/")
    is_in_area = 0
    for y in area:
        if y == lista[0]:
            is_in_area = is_in_area+1
            break
    if is_in_area == 0:
        area.insert(len(area), lista[0])

for x in area:
    locations[x] = []

for x in area:
    for y in timezones_split:
        lista = y.split("/")
        if len(lista) > 1:
            if lista[0] == x:
                is_in_loc1 = 1
                for z in locations[x]:
                    if lista[1] == z:
                        is_in_loc1 = 0
                        break
                if is_in_loc1 == 1:
                    locations[x].insert(len(locations[x]), lista[1])
        if len(lista) > 2:
            if lista[1] == "Argentina":
                is_in_loc2 = 1
                for z in argentina:
                    if lista[2] == z:
                        is_in_loc2 = 0
                        break
                if is_in_loc2 == 1:
                    argentina.insert(len(argentina), lista[2])
            elif lista[1] == "Indiana":
                is_in_loc2 = 1
                for z in indiana:
                    if lista[2] == z:
                        is_in_loc2 = 0
                        break
                if is_in_loc2 == 1:
                    indiana.insert(len(indiana), lista[2])
            elif lista[1] == "Kentucky":
                is_in_loc2 = 1
                for z in kentucky:
                    if lista[2] == z:
                        is_in_loc2 = 0
                        break
                if is_in_loc2 == 1:
                    kentucky.insert(len(kentucky), lista[2])
            else:
                is_in_loc2 = 1
                for z in north_dakota:
                    if lista[2] == z:
                        is_in_loc2 = 0
                        break
                if is_in_loc2 == 1:
                    north_dakota.insert(len(north_dakota), lista[2])

for x in locations:
    if len(locations[x]) == 0:
        locations[x].insert(len(locations[x]), "-")

class Application(Frame):

    def __init__(self, master=None, Frame=None):
        Frame.__init__(self, master)
        super(Application,self).__init__()
        self.grid(column = 1,row = 20,padx = 160,pady = 16)
        self.createWidgets()

    def getUpdateData(self,  event):
        self.LocationCombo.config(state = "readonly")
        self.LocationCombo['values'] = locations[self.AreaCombo.get()]

    def getUpdateData2(self, event):
        if self.LocationCombo.get() == "Argentina":
            self.ExactLocationCombo['values'] = argentina
            self.ExactLocationCombo.config(state = "readonly")
            return
        elif self.LocationCombo.get() == "Indiana":
            self.ExactLocationCombo['values'] = indiana
            self.ExactLocationCombo.config(state="readonly")
            return
        elif self.ExactLocationCombo.get() == "Kentucky":
            self.ExactLocationCombo.config(state="readonly")
            self.ExactLocationCombo['values'] = kentucky
            return
        elif self.ExactLocationCombo.get() == "North_Dakota":
            self.ExactLocationCombo.config(state="readonly")
            self.ExactLocationCombo['values'] = north_dakota
            return
        else:
            self.ExactLocationCombo.config(state="readonly")
            self.ExactLocationCombo['values'] = '-'

    def checkButton(self, event):
        if self.AreaCombo.get() != "":
            if self.LocationCombo.get() != "":
                if self.LocationCombo.get() != "Argentina" and self.LocationCombo.get() != "Indiana" and self.LocationCombo.get() != "Kentucky" and self.LocationCombo != "North_Dakota":
                    self.button.config(state="normal")
                elif self.ExactLocationCombo.get() != "":
                    self.button.config(state="normal")

    def callback(self):
        areaStr = self.AreaCombo.get()
        locationStr = self.LocationCombo.get()
        exactLocationStr = self.ExactLocationCombo.get()

        if locationStr == "-":
            outputTimezone = 'http://worldtimeapi.org/api/timezone' + "/" + areaStr
            outputTimezone_api = requests.get(outputTimezone)
            outputText = outputTimezone_api.text
            mytable2 = outputText.maketrans("", "", '{}"')
            outputText = outputText.translate(mytable2)

            outputText_split = outputText.split(",")
            for x in outputText_split:
                y = x.split(":")
                douapct = 0
                pct = 0
                T = 0;
                if y[0] == "datetime":
                    for i in range(0, len(x) - 1):
                        if x[i] == ":":
                            douapct = i
                            break
                    for i in range(douapct, len(x) - 1):
                        if x[i] == "T":
                            T = i
                            break
                    for i in range(T, len(x) - 1):
                        if x[i] == ".":
                            pct = i
                            break
                    date = x[douapct + 1:T]
                    time = x[T + 1:pct]
                    finalOutput = "date: " + date + " time: " + " " + time
                    self.OutputLabel.config(text=finalOutput)
        else:
            outputTimezone = 'http://worldtimeapi.org/api/timezone' + "/" + areaStr + "/" + locationStr
            if (exactLocationStr != "-"):
                outputTimezone = outputTimezone + "/" + exactLocationStr
            outputTimezone_api = requests.get(outputTimezone)
            outputText = outputTimezone_api.text
            mytable2 = outputText.maketrans("", "", '{}"')
            outputText = outputText.translate(mytable2)

            outputText_split = outputText.split(",")
            for x in outputText_split:
                y = x.split(":")
                douapct = 0
                pct = 0
                T = 0;
                if y[0] == "datetime":
                    for i in range(0, len(x) - 1):
                        if x[i] == ":":
                            douapct = i
                            break
                    for i in range(douapct, len(x) - 1):
                        if x[i] == "T":
                            T = i
                            break
                    for i in range(T, len(x) - 1):
                        if x[i] == ".":
                            pct = i
                            break
                    date = x[douapct + 1:T]
                    time = x[T + 1:pct]
                    finalOutput = "date: " + date + " time: " + " " + time
                    self.OutputLabel.config(text=finalOutput)

    def createWidgets(self):
        Label(text = 'Select area').grid(row = 2,column = 1,padx = 10)
        Label(text = 'Select location').grid(row = 4,column = 1,padx = 10)
        Label(text = 'Select exact location').grid(row = 6, column = 1, padx = 10)
        self.ExactLocationCombo = ttk.Combobox(width = 15, state = "disabled")
        self.ExactLocationCombo.bind('<<ComboboxSelected>>', self.checkButton)
        self.ExactLocationCombo.grid(row = 7, column = 1, pady = 5, padx = 10)

        self.LocationCombo = ttk.Combobox(width = 15, state = "disabled")
        self.LocationCombo.bind('<<ComboboxSelected>>', self.getUpdateData2)
        self.LocationCombo.grid(row = 5,column = 1,pady = 5,padx = 10)

        self.AreaCombo = ttk.Combobox(width = 15, state = "readonly", values = list(locations.keys()))
        self.AreaCombo.bind('<<ComboboxSelected>>', self.getUpdateData)
        self.AreaCombo.grid(row = 3,column = 1,padx = 10,pady = 5)

        self.button = ttk.Button(text = 'Show time', state = "disabled",  command = self.callback)
        self.button.grid(row = 8, column = 1, padx = 10, pady = 5)

        self.OutputLabel = ttk.Label(text = 'Time: ')
        self.OutputLabel.config(width = 50)
        self.OutputLabel.grid(row = 9, column = 1, padx = 10, pady = 5)

app = Application()
app.master.title('Timezones')
app.master.resizable(False, False)
app.mainloop()