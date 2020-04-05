import tkinter as tk
import pickle
import pygame

class Controller():
    def __init__(self, screen):
        self.surface = screen
        self.drawing = False
        self.interval = None
        self.placingStart = False
        self.placingEnd = False
        self.leftMouseDown = False
        self.rightMouseDown = False
        self.running = False
        self.grid = None
        self.fileName = ''


        self.startingNode = None
        self.targetNode = None

    def save(self):
        file = self.fileName
        configFile = open(file, "wb")
        pickle.dump(self.grid, configFile)

    def openFile(self):
        name = self.fileName
        configFile = open(name, "rb")
        savedGrid = pickle.load(configFile)
        self.grid = savedGrid
        self.refreshGrid()

    def saveInfo(self):
        self.win = tk.Toplevel()
        self.win.wm_title("FileName")
        label_1 = tk.Label(self.win, text="FileName:")
        self.entryBox1 = tk.Entry(self.win)
        saveButt = tk.Button(self.win,text='Save', command=self.closeSavePopup)
        openButt = tk.Button(self.win, text = 'Open', command=self.closeOpenPopup)
        label_1.grid(row=0, sticky=tk.E)  # if no column num is specified it will assume 0, the first
        self.entryBox1.grid(row=0, column=1)
        saveButt.grid(row=1, sticky=tk.E)


    def openInfo(self):
        self.win = tk.Toplevel()
        self.win.wm_title("FileName")
        label_1 = tk.Label(self.win, text="FileName:")
        self.entryBox1 = tk.Entry(self.win)
        openButt = tk.Button(self.win,text='Open', command=self.closeOpenPopup)
        label_1.grid(row=0, sticky=tk.E)  # if no column num is specified it will assume 0, the first
        self.entryBox1.grid(row=0, column=1)
        openButt.grid(row=1, sticky=tk.E)


    def closeOpenPopup(self):
        self.fileName = self.entryBox1.get() + '.pickle'
        self.win.destroy()
        self.openFile()

    def closeSavePopup(self):
        self.fileName = self.entryBox1.get() + '.pickle'
        self.win.destroy()
        self.save()

    def refreshGrid(self):
        for node in self.grid:
            node.draw(self.surface)
            pygame.display.update()