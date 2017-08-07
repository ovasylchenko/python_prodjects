import sys
import os
from tkinter import *
from tkinter.messagebox import *
import tkinter
from tkinter.filedialog import *
import csv
import collections


class Molecule:
    def __init__(self, structure1, filds1):
        self.structure1 = []
        self.filds1 = collections.OrderedDict()


class RedirectText(object):
    def __init__(self, text_ctrl):
        self.output = text_ctrl
        self.output.config(state=DISABLED)

    def write(self, string):
        self.output.config(state="normal")
        self.output.insert(tkinter.END, string)
        self.output.see(END)
        self.output.config(state=DISABLED)

    def flush(self):
        sys.__stdout__.flush()


class RedyaGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.file_name = 0
        self.csv_file_name = 0
        self.filds = []
        self.id_var1 = ''
        self.id_var0 = ''
        self.idnumber0 = 0
        self.idnumber2 = 0
        self.field_processing0 = 0
        self.procesing_id0 = 0
        self.sorted_move0 = 0
        self.sorted_fild0 = 0
        self.sdf_all = collections.OrderedDict()
        self.xraniliwe = collections.OrderedDict()
        # self.counter1 = 0
        # self.counter2 = 0
        self.id_var3 = ''
        self.id_var4 = ''
        self.id_var5 = ''
        self.id_var6 = ''
        self.id_var7 = ''
        self.id_var8 = ''
        self.ent_text = ''
        self.ent_text1 = ''
        self.ent_text2 = ''
        self.list_saver = ''
        self.list_saver_act = ''
        self.idnumber4 = 0
        self.idnumber6 = ''
        self.idnumber7 = ''
        self.adding_field = 0
        self.adding_field_val = 0
        self.file_name_save = 0
        self.list_name = 0
        self.list_xran = []
        self.list_nd_xran = []
        self.list_list = []
        self.dict0 = 0
        self.dict2 = 0
        self.sorted_move2 = 0
        self.sorted_move3 = 0
        self.listid2 = []
        self.list4 = []
        self.sortmovelist2 = ['yes', 'no']
        self.csvlist = ['sdf', 'csv']
        self.sortmovelist = ['small', 'big', 'add']
        self.pack(expand=NO, fill=BOTH)
        self.makeWidgets()
        self.master.title("SDF MAKER FROM REDYA")
        self.master.geometry('800x500')
        self.master.minsize(width=300, height=150)
        self.rtext = Text(bg='white', wrap='word')
        self.tbar = Scrollbar(self.rtext)
        self.tbar.config(command=self.rtext.yview)
        self.rtext.config(yscrollcommand=self.tbar.set)
        self.tbar.pack(side=RIGHT, fill=Y)
        self.rtext.pack(side=BOTTOM, expand=YES, fill=BOTH)
        self.input_sdf_count = 0
        self.csf_count = 0

        redir = RedirectText(self.rtext)
        sys.stdout = redir

    def makeWidgets(self):
        self.makeRmenu()
        fr1 = Frame(self)
        fr1.grid(column=0, row=0, sticky=(N, W))
        lab = Label(self, bg='white', text='system text out')
        but1 = Button(fr1,  bg='white', fg="black", text='remove dublicates from sdf', command=self.dub_remover1)
        but2 = Button(fr1,  bg='black', fg="white", text='clear system text out', command=self.notdone3)
        but3 = Button(fr1,  bg='white', fg="black", text='load sdf file in memory', command=self.load_sdf)
        but4 = Button(fr1, bg='white', fg="red", text='clear cash', command=self.clear_cash)
        but5 = Button(fr1, bg='white', fg="black", text='remove dublicates from list', command=self.rem_dub_list)
        but6 = Button(fr1, bg='white', fg="black", text='save sdf from list', command=self.sdf_writer_from_list)
        but7 = Button(fr1, bg='white', fg="black", text='add field to sdf', command=self.field_adder)
        but8 = Button(fr1, bg='white', fg="black", text='save list from sdf', command=self.lst_writer)
        but9 = Button(fr1, bg='white', fg="black", text='add rows from csv in to sdf', command=self.csv_read3)
        but3.grid(row=2, column=0, sticky=(N, W))
        but1.grid(row=0, column=0, sticky="W")
        but5.grid(row=0, column=1)
        but7.grid(row=0, column=3)
        but9.grid(row=1, column=3)
        but8.grid(row=1, column=2)
        but4.grid(row=2, column=5)
        but2.grid(row=2, column=3)
        but6.grid(row=0, column=2)
        lab.grid(column=0, row=2, sticky=(E, W))

    def makeRmenu(self):
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        self.fileMenu()
        self.selectMethod()
        self.helpwindow()

    def fileMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_separator()
        pulldown.add_command(label='Open sdf file', command=self.on_open_sdf_file)
        pulldown.add_separator()
        pulldown.add_command(label='Open csv file', command=self.on_open_csv_file)
        pulldown.add_separator()
        pulldown.add_command(label='Open list file', command=self.lst_reader)
        pulldown.add_separator()
        pulldown.add_command(label='Save full sdf file', command=self.loader)
        pulldown.add_separator()
        pulldown.add_command(label='Save maked sdf file', command=self.loader1)
        pulldown.add_separator()
        pulldown.add_command(label='Save list', command=self.list_saver4)
        pulldown.add_separator()
        pulldown.add_command(label='Quit', command=self.quit)
        self.menubar.add_cascade(label='File', menu=pulldown)

    def selectMethod(self):
        pulldown = Menu(self.menubar)
        pulldown.add_separator()
        pulldown.add_command(label='Save list of selected field', command=self.notdone)
        pulldown.add_separator()
        pulldown.add_command(label='save sdf from list', command=self.notdone)
        pulldown.add_separator()
        pulldown.add_command(label='print available sdf fields', command=self.field_reader1)
        pulldown.add_separator()
        pulldown.add_command(label='print available csf fields', command=self.csv_read)
        pulldown.add_separator()
        self.menubar.add_cascade(label='Methods', menu=pulldown)
        nfm = Menu(pulldown)
        pulldown.add_cascade(label="remove dublicates", menu=nfm)
        pulldown.add_separator()
        nfm.add_command(label='remove dublicates by values of selected field', command=self.sel_idnumber)
        nfm.add_separator()
        nfm.add_command(label='remove dublicates and sort/add', command=self.sel_idnumber1)
        nfm.add_separator()
        nfm.add_command(label='remove dublicates and field values and sort/add', command=self.sel_idnumber2)
        nfm.add_separator()

    def helpwindow(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='help', command=self.redyahelp)
        self.menubar.add_cascade(label='Help', menu=pulldown)
        pulldown.add_separator()

    def notdone(self):
        print('\n' + '=' * 45)
        print('\nhere must be some function')

    def on_open_sdf_file(self):
        self.file_name = askopenfilename(parent=self, filetypes=[("sdf files", "*.sdf")])
        if self.file_name:
            print('\n' + '=' * 45)
            self.field_reader()
            print('\n' + str(self.file_name) + ' successfully opened')
        else:
            print('\n!!! opening sdf file canceled')

    def redyahelp(self):
        helper = Toplevel(self)
        helper.minsize(width=900, height=600)
        helper.maxsize(width=900, height=600)
        helper.title("Help")
        sbar = Scrollbar(helper)
        msg = Text(helper, bg='white', wrap=WORD)
        sbar.config(command=msg.yview)
        msg.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        msg.pack(side=TOP, expand=YES, fill=BOTH)
        helptext = open('MAKER_SDF_HELP.txt', 'r').read()
        msg.insert('1.0', helptext)
        msg.config(state=DISABLED)

    def notdone3(self):
        self.rtext.config(state="normal")
        self.rtext.delete(1.0, END)
        self.rtext.config(state=DISABLED)

    def quit(self):
        sys.exit()

    def field_reader(self):
        if self.file_name:
            openfile1 = open(self.file_name, "r")
            counter1 = 0
            counter2 = 0
            structure = []
            self.filds = []
            fields_value = []
            field_value = []
            cheker101 = 25000
            for line in openfile1:
                if counter1 == 0:
                    structure.append(line)
                    if line[:-1] == 'M  END':
                        counter1 = 1
                        counter2 = 0
                        continue
                else:
                    if counter2 == 1 and line[0] == '>':
                        fields_value.append(field_value)
                        field_value = []
                        counter2 = 0
                    if line[:-1] == '$$$$':
                        break
                    if line[:4] == '>  <':
                        counter2 = 1
                        self.filds.append(line[4:-2])
                        continue
                    elif line[:3] == '> <':
                        counter2 = 1
                        self.filds.append(line[3:-2])
                        continue
                    else:
                        if line[:-1] == '':
                            pass
                        else:
                            field_value.append(line[:-1])
            openfile1.close()
            openfile1 = open(self.file_name, "r")
            for line2 in openfile1:
                if line2[:-1] == '$$$$':
                    self.input_sdf_count += 1
                    if self.input_sdf_count > cheker101:
                        print('\nread ' + str(cheker101) + ' sdf_rows')
                        RedyaGui.update(self)
                        cheker101 += 25000
            print('\ntotal sdf rows in ' + str(self.file_name) + '= ' + str(self.input_sdf_count))
            openfile1.close()

    def field_reader1(self):
        print('\n' + '=' * 45)
        if self.file_name:
            print('\navailable sdf fields:')
            for ele in self.filds:
                print('\n' + str(ele))
        else:
            print('\nno opened sdf file')

    def on_open_csv_file(self):
        self.csv_file_name = askopenfilename(parent=self, filetypes=[("csv files", "*.csv"), ("tsv files", "*.tsv")])
        if self.csv_file_name:
            print('\n' + '=' * 45)
            self.csv_read1()
            print('\n' + str(self.csv_file_name) + ' successfully opened')
        else:
            print('\n!!! opening csv file canceled')

    def csv_read1(self):
        csv_count = 25000
        n = 0
        if self.csv_file_name:
            openfile_csv = open(self.csv_file_name, "r")
            if self.csv_file_name[-4:] == '.csv':
                for row in csv.reader(openfile_csv):
                    self.csf_count += 1
                    if n == 0:
                        for i in row:
                            self.listid2.append(i)
                        n += 1
                        continue
                    if n == 1:
                        if self.csf_count > csv_count:
                            print('\nread ' + str(csv_count) + ' csv_rows')
                            csv_count += 25000
                            RedyaGui.update(self)
                print('\ntotal sdf rows in ' + str(self.csv_file_name) + '= ' + str(self.csf_count))
                openfile_csv.close()
            if self.csv_file_name[-4:] == '.tsv':
                for row in csv.reader(openfile_csv, delimiter="\t"):
                    self.csf_count += 1
                    if n == 0:
                        for i in row:
                            self.listid2.append(i)
                        n += 1
                        continue
                    if n == 1:
                        if self.csf_count > csv_count:
                            print('\nread ' + str(csv_count) + ' csv_rows')
                            csv_count += 25000
                            RedyaGui.update(self)
                print('\ntotal sdf rows in ' + str(self.csv_file_name) + '= ' + str(self.csf_count))
                openfile_csv.close()
    def csv_read(self):
        print('\n' + '=' * 45)
        if self.csv_file_name:
            print('\navailable fields in ' + str(self.csv_file_name) + ' file')
            for ele in self.listid2:
                print('\n' + ele)
        else:
            print('\nno opened csv file')

    def sel_idnumber(self):
        def idnumber_select_destroy():
            idnumber_select.destroy()
        nrow = 0
        mcoll = 0
        if self.filds:
            idnumber_select = Toplevel(self)
            idnumber_select.minsize(width=350, height=300)
            idnumber_select.title("select dublicate removing field")
            self.id_var0 = StringVar()
            lab2 = Label(idnumber_select, bg='white', text='select dublicate removing field')
            lab2.grid(row=nrow, column=2)
            nrow += 1
            for ele2 in self.filds:
                rb1 = Radiobutton(idnumber_select, text=str(ele2), variable=self.id_var0, value=str(ele2))
                rb1.grid(row=nrow, column=mcoll)
                mcoll += 1
                if mcoll == 5:
                    mcoll = 0
                    nrow += 1
            nrow += 1
            but5 = Button(idnumber_select, text="set dublicate removing field", command=self.makemove)
            but6 = Button(idnumber_select, text="close", command=idnumber_select_destroy)
            but5.grid(row=nrow, column=2)
            nrow += 1
            but20 = Button(idnumber_select, text="remove dublicates", command=self.dub_remover)
            but20.grid(row=nrow, column=2)
            nrow += 1
            but6.grid(row=nrow, column=2)
        else:
            print('\n' + '=' * 45)
            print('\n!!! no opened sdf file')

    def sel_idnumber1(self):
        def idnumber_select1_destroy():
            idnumber_select1.destroy()
        nrow = 0
        mcoll = 0
        if self.filds:
            idnumber_select1 = Toplevel(self)
            idnumber_select1.minsize(width=350, height=300)
            idnumber_select1.title("select sorting/add field")
            self.id_var1 = StringVar()
            lab3 = Label(idnumber_select1, bg='white', text='select sorted/add field')
            lab3.grid(row=nrow, column=2)
            nrow += 1
            for ele3 in self.filds:
                rb2 = Radiobutton(idnumber_select1, text=str(ele3), variable=self.id_var1, value=str(ele3))
                rb2.grid(row=nrow, column=mcoll)
                mcoll += 1
                if mcoll == 5:
                    mcoll = 0
                    nrow += 1
            nrow += 1
            mcoll = 1
            lab4 = Label(idnumber_select1, bg='white', text='select action move')
            lab4.grid(row=nrow, column=2)
            nrow += 1
            but8 = Button(idnumber_select1, text="close", command=idnumber_select1_destroy)
            self.id_var3 = StringVar()
            for sort in self.sortmovelist:
                rb3 = Radiobutton(idnumber_select1, text=str(sort), variable=self.id_var3, value=str(sort))
                rb3.grid(row=nrow, column=mcoll)
                mcoll += 1
                if mcoll == 5:
                    mcoll = 0
                    nrow += 1
            nrow += 1
            but9 = Button(idnumber_select1, text="set parameters", command=self.makemove1)
            but9.grid(row=nrow, column=2)
            nrow += 1
            but8.grid(row=nrow, column=2)
            nrow += 1
        self.sel_idnumber()

    def sel_idnumber2(self):
        def idnumber_select2_destroy():
            idnumber_select2.destroy()
        nrow = 0
        mcoll = 0
        if self.filds:
            idnumber_select2 = Toplevel(self)
            idnumber_select2.minsize(width=350, height=300)
            idnumber_select2.title("select sorted/add field2!!!")
            self.id_var4 = StringVar()
            lab5 = Label(idnumber_select2, bg='white', text='select sorted/add field2!!!')
            lab5.grid(row=nrow, column=2)
            nrow += 1
            for ele5 in self.filds:
                rb4 = Radiobutton(idnumber_select2, text=str(ele5), variable=self.id_var4, value=str(ele5))
                rb4.grid(row=nrow, column=mcoll)
                mcoll += 1
                if mcoll == 5:
                    mcoll = 0
                    nrow += 1
            nrow += 1
            mcoll = 1
            but12 = Button(idnumber_select2, text="close", command=idnumber_select2_destroy)
            lab4 = Label(idnumber_select2, bg='white', text='select action move')
            lab4.grid(row=nrow, column=2)
            nrow += 1
            self.id_var5 = StringVar()
            for sort1 in self.sortmovelist:
                rb4 = Radiobutton(idnumber_select2, text=str(sort1), variable=self.id_var5, value=str(sort1))
                rb4.grid(row=nrow, column=mcoll)
                mcoll += 1
                if mcoll == 5:
                    mcoll = 0
                    nrow += 1
            nrow += 1
            but13 = Button(idnumber_select2, text="set parameters", command=self.makemove2)
            but13.grid(row=nrow, column=2)
            nrow += 1
            but12.grid(row=nrow, column=2)
        self.sel_idnumber1()

    def makemove(self):
        print('\n' + '=' * 45)
        if self.id_var0.get() != '':
            self.idnumber0 = self.id_var0.get()
            print('\n"' + str(self.idnumber0) + '" field set as dublicate removing field')
        else:
            print('\n!!! please select  dublicate removing field')

    def makemove1(self):
        print('\n' + '=' * 45)
        if self.id_var1.get() != '':
            self.field_processing0 = self.id_var1.get()
            print('\n"' + str(self.field_processing0) + '" field set as sorting/add field')
            if self.idnumber0 == self.field_processing0:
                print('\n!!! "' + str(self.idnumber0) + '" field has been already selected')
            if self.id_var3.get() != '':
                self.procesing_id0 = self.id_var3.get()
                print('\n"' + self.procesing_id0 + '" set as action for "' + str(self.field_processing0) + '" field')
            else:
                print('\n!!! please select action move for sorting/add field')
        else:
            if self.id_var1.get() == '':
                print('\n!!! please select sorting/add field')
            if self.id_var3.get() == '':
                print('\n!!! please select action move for sorting/add field')

    def makemove2(self):
        print('\n' + '=' * 45)
        if self.id_var4.get() != '':
            self.sorted_fild0 = self.id_var4.get()
            print('\n"' + str(self.sorted_fild0) + '" field set as sorting/add field2!!!')
            if self.sorted_fild0 == self.field_processing0 or self.sorted_fild0 == self.idnumber0:
                print('\n!!! "' + str(self.sorted_fild0) + '" field has been already selected')
            if self.id_var5.get() != '':
                self.sorted_move0 = self.id_var5.get()
                print('\n"' + self.sorted_move0 + '" set as action for "' + str(self.sorted_fild0) + '" field')
        else:
            if self.id_var4.get() == '':
                print('\n!!! please select sorting/add field2!!!')
            if self.id_var5.get() == '':
                print('\n!!! please select action move for sorting/add field2!!!')

    def dub_remover1(self):
        if self.file_name:
            if self.sdf_all:
                if self.idnumber0:
                    self.dub_remover()
                else:
                    # self.counter1 = 1
                    self.sel_idnumber()
            else:
                print('\nLOAD SDF IN MEMORY FIRST')
        else:
            print('\n!!! no opened sdf file')
            self.load_sdf()

    def dub_remover(self):
        print('\n' + '=' * 45)
        # self.counter1 = 0
        input_sdf_count = 0
        x = 0
        self.xraniliwe = collections.OrderedDict()
        if self.idnumber0:
            a = []
            b = collections.OrderedDict()
            no_id_fild = 0
            dub_number = 0
            other_error_count = 0
            empty_list0 = []
            empty_list1 = []
            empty_list = []
            if self.field_processing0:
                file_name_error2 = self.file_name[0:-4] + '_remove_dub_error.txt'
                openfile5 = open(file_name_error2, "w")
            for sdf in self.sdf_all:
                input_sdf_count += 1
                if input_sdf_count >= int(self.input_sdf_count/5):
                    x += 20
                    print('\ndublicate removing done ' + str(x) + '%')
                    input_sdf_count = 0
                    RedyaGui.update(self)
                if self.sdf_all.get(sdf).filds1.get(self.idnumber0) != empty_list:
                    try:
                        tmpid = str(self.sdf_all.get(sdf).filds1.get(self.idnumber0)[0])
                    except TypeError:
                        no_id_fild += 1
                        continue
                    if tmpid not in self.xraniliwe:
                        z12 = Molecule(a, b)
                        for line3 in self.sdf_all.get(sdf).structure1:
                            z12.structure1.append(line3)
                        for key3 in self.sdf_all.get(sdf).filds1:
                            xraniliwe9 = {key3: self.sdf_all.get(sdf).filds1.get(key3)}
                            z12.filds1.update(xraniliwe9)
                        xraniliwe7 = {tmpid: z12}
                        self.xraniliwe.update(xraniliwe7)
                    else:
                        dub_number += 1
                        if self.field_processing0:
                            if str(self.field_processing0) in self.xraniliwe.get(tmpid).filds1:
                                pass
                            else:
                                xraniliwe5 = {str(self.field_processing0): empty_list0}
                                self.xraniliwe.get(tmpid).filds1.update(xraniliwe5)
                                empty_list0 = []
                                openfile5.write(tmpid + ' - no (' + str(self.field_processing0) + ') field in sdf\n')
                                other_error_count += 1
                                if self.sorted_fild0:
                                    if str(self.sorted_fild0) in self.xraniliwe.get(tmpid).filds1:
                                        pass
                                    else:
                                        xraniliwe13 = {str(self.sorted_fild0): empty_list1}
                                        self.xraniliwe.get(tmpid).filds1.update(xraniliwe13)
                                        empty_list1 = []
                                        openfile5.write(tmpid + ' - no (' + str(self.sorted_fild0) + ') field in sdf\n')
                                        other_error_count += 1
                            if str(self.field_processing0) in self.sdf_all.get(sdf).filds1:
                                if self.procesing_id0 == 'small':
                                    if self.xraniliwe.get(tmpid).filds1.get(str(self.field_processing0)) == empty_list:
                                        if self.sdf_all.get(sdf).filds1.get(str(self.field_processing0)) != empty_list:
                                            self.xraniliwe.get(tmpid).filds1.update(self.sdf_all.get(sdf).filds1)
                                    else:
                                        if self.sdf_all.get(sdf).filds1.get(str(self.field_processing0)) != empty_list:
                                            if float(self.xraniliwe.get(tmpid).filds1.get(str(self.field_processing0))[
                                                         0]) > float(
                                                    self.sdf_all.get(sdf).filds1.get(str(self.field_processing0))[0]):
                                                self.xraniliwe.get(tmpid).filds1.update(self.sdf_all.get(sdf).filds1)
                                elif self.procesing_id0 == 'big':
                                    if self.xraniliwe.get(tmpid).filds1.get(str(self.field_processing0)) == empty_list:
                                        if self.sdf_all.get(sdf).filds1.get(str(self.field_processing0)) != empty_list:
                                            self.xraniliwe.get(tmpid).filds1.update(self.sdf_all.get(sdf).filds1)
                                    else:
                                        if self.sdf_all.get(sdf).filds1.get(str(self.field_processing0)) != empty_list:
                                            if float(self.xraniliwe.get(tmpid).filds1.get(str(self.field_processing0))[
                                                         0]) < float(
                                                    self.sdf_all.get(sdf).filds1.get(str(self.field_processing0))[0]):
                                                self.xraniliwe.get(tmpid).filds1.update(self.sdf_all.get(sdf).filds1)
                                elif self.procesing_id0 == 'add':
                                    for ele in self.sdf_all.get(sdf).filds1.get(str(self.field_processing0)):
                                        if ele not in self.xraniliwe.get(tmpid).filds1.get(str(self.field_processing0)):
                                            add_filds = self.xraniliwe.get(tmpid).filds1.get(
                                                str(self.field_processing0))
                                            add_filds.insert(0, ele)
                                            xraniliwe6 = {str(self.field_processing0): add_filds}
                                            self.xraniliwe.get(tmpid).filds1.update(xraniliwe6)
                                    if self.sorted_fild0:
                                        if str(self.sorted_fild0) in self.sdf_all.get(sdf).filds1:
                                            if self.sorted_move0 == 'small':
                                                if self.xraniliwe.get(tmpid).filds1.get(
                                                        str(self.sorted_fild0)) == empty_list:
                                                    if self.sdf_all.get(sdf).filds1.get(
                                                            str(self.sorted_fild0)) != empty_list:
                                                        xraniliwe8 = {
                                                            str(self.sorted_fild0): self.sdf_all.get(sdf).filds1.get(
                                                                str(self.sorted_fild0))}
                                                        self.xraniliwe.get(tmpid).filds1.update(xraniliwe8)
                                                else:
                                                    if self.sdf_all.get(sdf).filds1.get(
                                                            str(self.sorted_fild0)) != empty_list:
                                                        if float(self.xraniliwe.get(tmpid).filds1.get(
                                                                str(self.sorted_fild0))[0]) > float(
                                                                self.sdf_all.get(sdf).filds1.get(
                                                                        str(self.sorted_fild0))[0]):
                                                            xraniliwe9 = {str(self.sorted_fild0): self.sdf_all.get(
                                                                sdf).filds1.get(str(self.sorted_fild0))}
                                                            self.xraniliwe.get(tmpid).filds1.update(xraniliwe9)
                                            elif self.sorted_move0 == 'big':
                                                if self.xraniliwe.get(tmpid).filds1.get(
                                                        str(self.sorted_fild0)) == empty_list:
                                                    if self.sdf_all.get(sdf).filds1.get(
                                                            str(self.sorted_fild0)) != empty_list:
                                                        xraniliwe8 = {
                                                            str(self.sorted_fild0): self.sdf_all.get(sdf).filds1.get(
                                                                str(self.sorted_fild0))}
                                                        self.xraniliwe.get(tmpid).filds1.update(xraniliwe8)
                                                else:
                                                    if self.sdf_all.get(sdf).filds1.get(
                                                            str(self.sorted_fild0)) != empty_list:
                                                        if float(self.xraniliwe.get(tmpid).filds1.get(
                                                                str(self.sorted_fild0))[0]) < float(
                                                                self.sdf_all.get(sdf).filds1.get(
                                                                        str(self.sorted_fild0))[0]):
                                                            xraniliwe9 = {str(self.sorted_fild0): self.sdf_all.get(
                                                                sdf).filds1.get(str(self.sorted_fild0))}
                                                            self.xraniliwe.get(tmpid).filds1.update(xraniliwe9)
                                            elif self.sorted_move0 == 'add':
                                                for ele2 in self.sdf_all.get(sdf).filds1.get(str(self.sorted_fild0)):
                                                    if ele2 not in self.xraniliwe.get(tmpid).filds1.get(
                                                            str(self.sorted_fild0)):
                                                        add_filds2 = self.xraniliwe.get(tmpid).filds1.get(
                                                            str(self.sorted_fild0))
                                                        add_filds2.insert(0, ele2)
                                                        xraniliwe14 = {str(self.sorted_fild0): add_filds2}
                                                        self.xraniliwe.get(tmpid).filds1.update(xraniliwe14)
                                        else:
                                            openfile5.write(
                                                tmpid + ' - no (' + str(self.sorted_fild0) + ') field in sdf\n')
                                            other_error_count += 1
                            else:
                                openfile5.write(tmpid + ' - no (' + str(self.field_processing0) + ') field in sdf\n')
                                other_error_count += 1
                    for tei in self.sdf_all.get(sdf).filds1:
                        if tei not in self.xraniliwe.get(tmpid).filds1:
                            xraniliwe10 = {tei: self.sdf_all.get(sdf).filds1.get(tei)}
                            self.xraniliwe.get(tmpid).filds1.update(xraniliwe10)
                else:
                    no_id_fild += 1
            if self.sdf_all == collections.OrderedDict():
                print('\nLOAD SDF IN MEMORY FIRST')
            if self.field_processing0:
                openfile5.close()
            if self.sdf_all != collections.OrderedDict():
                print('\nstructures with ' + str(self.idnumber0) + ' field in sdf = ' + str(
                    (len(self.sdf_all) - no_id_fild)))
                print('\nstructures with no ' + str(self.idnumber0) + ' field in sdf = ' + str(no_id_fild))
                print('\ntotal number of dublicates in sdf = ' + str(dub_number))
                if self.field_processing0:
                    print('\nnumber of sorting/adding errors = ' + str(other_error_count))
                    print('\n' + str(file_name_error2) + '  saved')
        else:
            print('\n!!!set removing dublicate field first')

    def load_sdf(self):
        print('\n' + '=' * 45)
        linex = ''
        if self.file_name:
            a = []
            b = collections.OrderedDict()
            openfile1 = open(self.file_name, "r")
            counter1 = 0
            counter2 = 0
            my_id = 0
            x = 0
            sdf_counter = 0
            structure = []
            filds = []
            fields_value = []
            field_value = []
            for line in openfile1:
                if counter1 == 0:
                    structure.append(line[:-1])
                    if line[:-1] == 'M  END':
                        counter1 = 1
                        counter2 = 0
                        continue
                else:
                    if counter2 == 1 and line[0] == '>':
                        fields_value.append(field_value)
                        field_value = []
                        counter2 = 0
                    if line[:-1] == '$$$$':
                        sdf_counter += 1
                        if sdf_counter >= int(self.input_sdf_count/10):
                            x += 10
                            print('\n loaded another ' + str(sdf_counter) + ' molecules, ' + str(x) + '%')
                            sdf_counter = 0
                            RedyaGui.update(self)
                        my_id += 1
                        fields_value.append(field_value)
                        z11 = Molecule(a, b)
                        xraniliwe4 = collections.OrderedDict()
                        for i in range(len(filds)):
                            xraniliwe3 = {filds[i]: fields_value[i]}
                            xraniliwe4.update(xraniliwe3)
                        for struc in structure:
                            z11.structure1.append(struc)
                        z11.filds1.update(xraniliwe4)
                        xraniliwe2 = {str(my_id): z11}
                        self.sdf_all.update(xraniliwe2)
                        filds = []
                        field_value = []
                        fields_value = []
                        structure = []
                        counter1 = 0
                        continue
                    if line[:4] == '>  <':
                        counter2 = 1
                        line = line[4:-1]
                        for z in line:
                            if z != '>':
                                linex = linex + str(z)
                        filds.append(linex)
                        linex = ''
                        continue
                    elif line[:3] == '> <':
                        counter2 = 1
                        line = line[3:-1]
                        for z in line:
                            if z != '>':
                                linex = linex + str(z)
                        filds.append(linex)
                        linex = ''
                        continue
                    else:
                        if line[:-1] == '':
                            pass
                        else:
                            field_value.append(line[:-1])
            openfile1.close()
            print('\ntotal sdf rows loaded in memory = ' + str(len(self.sdf_all)))
        else:
            print('\nno selected sdf file')
            self.on_open_sdf_file()

    def loader(self):
        print('\n' + '=' * 45)
        if self.sdf_all:
            self.dict0 = self.sdf_all
            self.sdf_writer()
        else:
            print('\n!!! no sdf file in memory')

    def loader1(self):
        print('\n' + '=' * 45)
        if self.xraniliwe:
            self.dict0 = self.xraniliwe
            self.sdf_writer()
        else:
            print('\n!!! please do some operations with sdf first or save full sdf file')

    def sdf_writer(self):
            writefile1 = asksaveasfile(mode='w', defaultextension='.sdf', filetypes=[("sdf files", "*.sdf")])
            if writefile1:
                upload_struture = 0
                empty_list = []
                for key in self.dict0:
                    for line3 in self.dict0.get(str(key)).structure1:
                        writefile1.write((str(line3)) + '\n')
                    for bubl in self.dict0.get(str(key)).filds1:
                        writefile1.write('>  <' + str(bubl) + '>' + '\n')
                        if self.dict0.get(str(key)).filds1.get(str(bubl)) == empty_list:
                            writefile1.write('\n')
                        else:
                            for krom in self.dict0.get(str(key)).filds1.get(str(bubl)):
                                writefile1.write(str(krom))
                            writefile1.write('\n\n')
                    writefile1.write('$$$$\n')
                    upload_struture += 1
                writefile1.close()
                print('\nstructures saved ' + str(upload_struture) + '\n')
                print('\nsdf successfully saved')
            else:
                print('\n!!! saving sdf file canceled')

    def lst_reader(self):
        print('\n' + '=' * 45)
        self.list_name = askopenfilename(parent=self,
                                         filetypes=[("txt files", "*.txt"), ("lst files", "*.lst"), ("any", "*.*")])
        if self.list_name:
            openfile2 = open(self.list_name, "r")
            for line2 in openfile2:
                if line2 == '\n' or line2 == ' ':
                    continue
                while line2[-1] == ' ' or line2[-1] == '\n':
                    line2 = line2[:-1]
                self.list_xran.append(line2)
            print('\ntotal id in list = ' + str(len(self.list_xran)))
            print('\n' + str(self.list_name) + ' successfully opened')
        else:
            print('\n!!! opening list file canceled')

    def rem_dub_list(self):
        print('\n' + '=' * 45)
        if len(self.list_xran) > 0:
            for lst in self.list_xran:
                if lst not in self.list_nd_xran:
                    self.list_nd_xran.append(lst)
            print('\ntotal id in list = ' + str(len(self.list_xran)))
            print('\ntotal uniq id in list = ' + str((len(self.list_nd_xran))))
        else:
            print('\n!!! no opened list file')
            self.lst_reader()

    def sdf_writer_from_list(self):
        print('\n' + '=' * 45)
        if self.sdf_all:
            if self.list_xran:
                def idnumber_select4_destroy():
                    idnumber_select4.destroy()
                nrow = 0
                mcoll = 0
                idnumber_select4 = Toplevel(self)
                idnumber_select4.minsize(width=350, height=300)
                idnumber_select4.title("select field for sdf saving")
                self.id_var6 = StringVar()
                lab3 = Label(idnumber_select4, bg='white', text='select field for sdf saving')
                lab3.grid(row=nrow, column=2)
                nrow += 1
                for ele3 in self.filds:
                    rb2 = Radiobutton(idnumber_select4, text=str(ele3), variable=self.id_var6, value=str(ele3))
                    rb2.grid(row=nrow, column=mcoll)
                    mcoll += 1
                    if mcoll == 5:
                        mcoll = 0
                        nrow += 1
                nrow += 1
                mcoll = 2
                lab4 = Label(idnumber_select4, bg='white', text='left dublitates in sdf?')
                lab4.grid(row=nrow, column=2)
                nrow += 1
                but8 = Button(idnumber_select4, text="close", command=idnumber_select4_destroy)
                self.id_var7 = StringVar()
                for sort in self.sortmovelist2:
                    rb3 = Radiobutton(idnumber_select4, text=str(sort), variable=self.id_var7, value=str(sort))
                    rb3.grid(row=nrow, column=mcoll)
                    mcoll += 1
                nrow += 1
                mcoll = 2
                lab5 = Label(idnumber_select4, bg='white', text='left dublitates in list?')
                lab5.grid(row=nrow, column=2)
                nrow += 1
                but9 = Button(idnumber_select4, text="set parameters", command=self.makemove3)
                self.id_var8 = StringVar()
                for sort in self.sortmovelist2:
                    rb4 = Radiobutton(idnumber_select4, text=str(sort), variable=self.id_var8, value=str(sort))
                    rb4.grid(row=nrow, column=mcoll)
                    mcoll += 1
                nrow += 1
                but10 = Button(idnumber_select4, text="save sdf", command=self.write_list_sdf)
                but9.grid(row=nrow, column=2)
                nrow += 1
                but10.grid(row=nrow, column=2)
                nrow += 1
                but8.grid(row=nrow, column=2)
            else:
                print('\n!!! no opened list file')
                self.lst_reader()
        else:
            print('\nLOAD SDF IN MEMORY FIRST')

    def makemove3(self):
        print('\n' + '=' * 45)
        if self.id_var6.get() != '':
            self.idnumber0 = self.id_var6.get()
            print('\n"' + str(self.idnumber0) + '" field set for sdf loading')
            if self.id_var7.get() != '':
                self.sorted_move2 = self.id_var7.get()
                print('\n"' + self.sorted_move2 + '" set for remaining dublicates in sdf')
                if self.sorted_move2 == 'no':
                    if self.id_var8.get() != '':
                        self.sorted_move3 = self.id_var8.get()
                        print('\n"' + self.sorted_move3 + '" set for remaining dublicates in list')
                    else:
                        print('\n!!! please set action for remain dublicates in list')
            else:
                print('\n!!! please set action for remain dublicates in sdf')
        else:
            if self.id_var6.get() == '':
                print('\n!!! please select field for sdf loading')
            if self.id_var7.get() == '':
                print('\n!!! please set action for remain dublicates in sdf')
            if self.id_var8.get() == '':
                print('\n!!! please set action for remain dublicates in list')

    def write_list_sdf(self):
        if self.idnumber0:
            if self.sorted_move2:
                if self.sorted_move2 == 'yes':
                    self.dict0 = self.sdf_all
                    self.list_list = self.list_xran
                    self.write_list_sdf1()
                if self.sorted_move2 == 'no':
                    if self.sorted_move3 == 'no':
                        self.dub_remover()
                        self.dict0 = self.xraniliwe
                        self.rem_dub_list()
                        self.list_list = self.list_nd_xran
                        self.write_list_sdf1()
                    if self.sorted_move3:
                        if self.sorted_move3 == 'yes':
                            self.dub_remover()
                            self.dict0 = self.xraniliwe
                            self.list_list = self.list_xran
                            self.write_list_sdf2()
                    else:
                        print('\n!!! please set action for remain dublicates in list')
            else:
                print('\n!!! please set action for remain dublicates in sdf')
        else:
            print('\n!!! please select field for sdf loading')

    def write_list_sdf1(self):
        writefile1 = asksaveasfile(mode='w', defaultextension='.sdf', filetypes=[("sdf files", "*.sdf")])
        if writefile1:
            print('\n' + '=' * 45)
            upload_struture = 0
            error_number = 0
            list3 = []
            empty_list = []
            file_name_error = self.file_name[0:-4] + '_write_sdf_error.txt'
            writefile2 = open(file_name_error, "w")
            for key2 in self.dict0:
                try:
                    tmpid2 = str(self.dict0.get(key2).filds1.get(self.idnumber0)[0])
                except TypeError:
                    continue
                if tmpid2 in self.list_list:
                    list3.append(tmpid2)
                    for line4 in self.dict0.get(str(key2)).structure1:
                        writefile1.write((str(line4)) + '\n')
                    for bubl in self.dict0.get(str(key2)).filds1:
                        writefile1.write('>  <' + str(bubl) + '>' + '\n')
                        if self.dict0.get(str(key2)).filds1.get(str(bubl)) == empty_list:
                            writefile1.write('\n')
                        else:
                            for krom in self.dict0.get(str(key2)).filds1.get(str(bubl)):
                                writefile1.write(str(krom))
                            writefile1.write('\n\n')
                    writefile1.write('$$$$\n')
                    upload_struture += 1
            for sss in self.list_list:
                if sss not in list3:
                    writefile2.write(str(sss) + ' - No such value of "' + str(self.idnumber0) + '" field in sdf\n')
                    error_number += 1
                    print('\n' + str(sss) + ' - No such value of "' + str(self.idnumber0) + '" field in sdf')
            print('\nstructures saved ' + str(upload_struture))
            print('\nnumber errors sdf writing = ' + str(error_number))
            print('\n' + str(file_name_error) + '  recorded')
            writefile1.close()
            writefile2.close()
        else:
            print('\n!!! saving sdf file canceled')

    def write_list_sdf2(self):
        writefile1 = asksaveasfile(mode='w', filetypes=[("sdf files", "*.sdf")], defaultextension='.sdf')
        if writefile1:
            print('\n' + '=' * 45)
            file_name_error = self.file_name[0:-4] + '_write_sdf_error.txt'
            writefile2 = open(file_name_error, "w")
            upload_struture = 0
            error_number = 0
            empty_list = []
            for key in self.list_list:
                try:
                    for line5 in self.xraniliwe.get(str(key)).structure1:
                        writefile1.write((str(line5)) + '\n')
                    for bubl in self.xraniliwe.get(str(key)).filds1:
                        writefile1.write('>  <' + str(bubl) + '>' + '\n')
                        if self.xraniliwe.get(str(key)).filds1.get(str(bubl)) == empty_list:
                            writefile1.write('\n')
                        else:
                            for krom in self.xraniliwe.get(str(key)).filds1.get(str(bubl)):
                                writefile1.write(str(krom))
                            writefile1.write('\n\n')
                    writefile1.write('$$$$\n')
                    upload_struture += 1
                except(KeyError, AttributeError):
                    error_number += 1
                    writefile2.write(str(key) + ' - No such value of "' + str(self.idnumber0) + '" field in sdf\n')
                    print('\n' + str(key) + ' - No such value of "' + str(self.idnumber0) + '" field in sdf')
                    continue
            writefile1.close()
            writefile2.close()
            print('\nstructures saved ' + str(upload_struture))
            print('\nnumber errors sdf writing = ' + str(error_number))
            print('\n' + str(file_name_error) + '  saved')
        else:
            print('\n!!! saving sdf file canceled')

    def field_adder(self):
        if self.sdf_all:
            def idnumber_select4_destroy():
                idnumber_select4.destroy()
            idnumber_select4 = Toplevel(self)
            idnumber_select4.minsize(width=350, height=300)
            idnumber_select4.title("input field name and default value")
            self.ent_text = StringVar()
            self.ent_text1 = StringVar()
            lab4 = Label(idnumber_select4, bg='white', text='Input name field')
            lab4.pack()
            ent1 = Entry(idnumber_select4, textvariable=self.ent_text)
            ent1.pack()
            but10 = Button(idnumber_select4, text="add field to sdf", command=self.field_adder1)
            but8 = Button(idnumber_select4, text="close", command=idnumber_select4_destroy)
            lab5 = Label(idnumber_select4, bg='white', text='Input default field value')
            lab5.pack()
            ent2 = Entry(idnumber_select4, textvariable=self.ent_text1)
            ent2.pack()
            lab6 = Label(idnumber_select4, bg='white', text='left bublicates in sdf?')
            lab6.pack()
            self.ent_text2 = StringVar()
            for sort in self.sortmovelist2:
                rb4 = Radiobutton(idnumber_select4, text=str(sort), variable=self.ent_text2, value=str(sort))
                rb4.pack()
            but10.pack()
            but8.pack()
        else:
            self.load_sdf()

    def field_adder1(self):
        print('\n' + '=' * 45)
        counter12 = 0
        counter11 = 0
        if self.ent_text2.get() != '':
            if self.ent_text.get() != '':
                if self.ent_text2.get() == 'yes':
                    self.adding_field = self.ent_text.get()
                    self.adding_field_val = self.ent_text1.get()
                    xraniliwe10 = {str(self.adding_field): str(self.adding_field_val)}
                    for sdf1 in self.sdf_all:
                        self.sdf_all.get(sdf1).filds1.update(xraniliwe10)
                        counter12 += 1
                    print(
                        '\n"' + self.adding_field + '" field successfully added in to ' + str(counter12) + ' sdf rows')
                if self.ent_text2.get() == 'no':
                    self.adding_field = self.ent_text.get()
                    self.adding_field_val = self.ent_text1.get()
                    if self.xraniliwe:
                        xraniliwe10 = {str(self.adding_field): str(self.adding_field_val)}
                        for sdf1 in self.xraniliwe:
                            self.xraniliwe.get(sdf1).filds1.update(xraniliwe10)
                            counter11 += 1
                        print('\n"' + self.adding_field + '" field successfully added in to ' + str(
                            counter11) + ' sdf rows')
                    else:
                        print('\n!!! remove dublicates first')
                        self.dub_remover1()
            else:
                print('\n!!! input field name')
        else:
            if self.ent_text.get() == '':
                print('\n!!! input field name')
            print('\n!!! please select action for dublicate removing')

    def lst_writer(self):
        if self.sdf_all:
            print('\n' + '=' * 45)
            def idnumber_select4_destroy():
                idnumber_select4.destroy()
            nrow = 0
            mcoll = 0
            idnumber_select4 = Toplevel(self)
            idnumber_select4.minsize(width=350, height=300)
            idnumber_select4.title("select field to save list")
            self.list_saver = StringVar()
            lab4 = Label(idnumber_select4, bg='white', text='select field to save list')
            lab4.grid(row=nrow, column=2)
            nrow += 1
            for ele2 in self.filds:
                rb1 = Radiobutton(idnumber_select4, text=str(ele2), variable=self.list_saver, value=str(ele2))
                rb1.grid(row=nrow, column=mcoll)
                mcoll += 1
                if mcoll == 5:
                    mcoll = 0
                    nrow += 1
            nrow += 1
            mcoll = 2
            lab5 = Label(idnumber_select4, bg='white', text='left dublicates in list?')
            lab5.grid(row=nrow, column=2)
            nrow += 1
            self.list_saver_act = StringVar()
            for sort1 in self.sortmovelist2:
                rb4 = Radiobutton(idnumber_select4, text=str(sort1), variable=self.list_saver_act, value=str(sort1))
                rb4.grid(row=nrow, column=mcoll)
                mcoll += 1
            nrow += 1
            but13 = Button(idnumber_select4, text="set parameters", command=self.makemove4)
            but13.grid(row=nrow, column=2)
            nrow += 1
            but10 = Button(idnumber_select4, text="save list", command=self.lst_writer1)
            but8 = Button(idnumber_select4, text="close", command=idnumber_select4_destroy)
            but10.grid(row=nrow, column=2)
            nrow += 1
            but8.grid(row=nrow, column=2)
        else:
            self.load_sdf()

    def makemove4(self):
        if self.list_saver.get() != '':
            self.idnumber2 = self.list_saver.get()
            print('\n"' + str(self.idnumber2) + '" field set list saving field')
            if self.list_saver_act.get() != '':
                if self.list_saver_act.get() == 'yes':
                    self.dict2 = self.sdf_all
                if self.list_saver_act.get() == 'no':
                    if self.xraniliwe:
                        self.dict2 = self.xraniliwe
                    else:
                        print('\n!!! remove dublicates first')
                        self.dub_remover1()
            else:
                print('\n!!! please select action for dublicate removing')
        else:
            print('\n!!! please select field for saving list')
            if self.list_saver_act.get() == '':
                print('\n!!! please select action for dublicate removing')

    def lst_writer1(self):
        if self.idnumber2:
            if self.list_saver_act.get() != '':
                if self.list_saver_act.get() == 'no':
                    if self.xraniliwe:
                        self.dict2 = self.xraniliwe
                        self.lst_writer2()
                    else:
                        self.dub_remover1()
                else:
                    self.lst_writer2()
            else:
                self.makemove4()
        else:
            self.makemove4()

    def lst_writer2(self):
        writefile1 = asksaveasfile(mode='w', filetypes=[("lst files", "*.lst"), ("txt files", "*.txt"), ("any", "*.*")], defaultextension='.txt')
        if writefile1:
            print('\n' + '=' * 45)
            error_number = 0
            upload_struture = 0
            for key2 in self.dict2:
                try:
                    tmpid2 = str(self.dict2.get(key2).filds1.get(self.idnumber2)[0])
                    writefile1.write(tmpid2 + '\n')
                    upload_struture += 1
                except (TypeError, AttributeError):
                    error_number += 1
                    continue
            print('\nstructures with no "' + str(self.idnumber2) + '" field in sdf = ' + str(error_number))
            print('\nnumber of "' + str(self.idnumber2) + '" field values saved = ' + str(upload_struture))
            writefile1.close()
        else:
            print('\n!!! saving list file canceled')

    def csv_read3(self):
        if self.sdf_all:
            pass
        else:
            self.load_sdf()
        if self.csv_file_name:
            pass
        else:
            self.on_open_csv_file()
        if self.sdf_all:
            if self.csv_file_name:
                self.csv_read2()

    def csv_read2(self):
        print('\n' + '=' * 45)
        def idnumber_select4_destroy():
            idnumber_select4.destroy()
        nrow = 0
        mcoll = 0
        idnumber_select4 = Toplevel(self)
        idnumber_select4.minsize(width=350, height=300)
        idnumber_select4.title("add scv data to sdf rows")
        self.idnumber6 = StringVar()
        lab4 = Label(idnumber_select4, bg='white', text='select ID field in sdf')
        lab4.grid(row=nrow, column=2)
        nrow += 1
        for ele2 in self.filds:
            rb1 = Radiobutton(idnumber_select4, text=str(ele2), variable=self.idnumber6, value=str(ele2))
            rb1.grid(row=nrow, column=mcoll)
            mcoll += 1
            if mcoll == 5:
                mcoll = 0
                nrow += 1
        nrow += 1
        mcoll = 0
        lab5 = Label(idnumber_select4, bg='white', text='select ID field in csv')
        lab5.grid(row=nrow, column=2)
        nrow += 1
        self.idnumber7 = StringVar()
        for sort1 in self.listid2:
            rb4 = Radiobutton(idnumber_select4, text=str(sort1), variable=self.idnumber7, value=str(sort1))
            rb4.grid(row=nrow, column=mcoll)
            mcoll += 1
            if mcoll == 5:
                mcoll = 0
                nrow += 1
        nrow += 1
        but13 = Button(idnumber_select4, text="set parameters", command=self.makemove5)
        but13.grid(row=nrow, column=2)
        nrow += 1
        but10 = Button(idnumber_select4, text="add csv data to sdf", command=self.csv_reader1)
        but11 = Button(idnumber_select4, text="save full sdf", command=self.csv_saver1)
        but12 = Button(idnumber_select4, text="save sdf only from csv id", command=self.csv_saver2)
        but8 = Button(idnumber_select4, text="close", command=idnumber_select4_destroy)
        nrow += 1
        but10.grid(row=nrow, column=2)
        nrow += 1
        but11.grid(row=nrow, column=1)
        but12.grid(row=nrow, column=3)
        nrow += 1
        but8.grid(row=nrow, column=2)

    def makemove5(self):
        if self.idnumber6.get() == '':
            print('\n!!! please select ID field in sdf file')
        else:
            print('\n"' + str(self.idnumber6.get()) + '" set as ID field in sdf')
            self.idnumber0 = self.idnumber6.get()
        if self.idnumber7.get() == '':
            print('\n!!! please select ID field in csv file')
        else:
            print('\n"' + str(self.idnumber7.get()) + '" set as ID field in csv')
            self.idnumber4 = self.idnumber7.get()
        if self.idnumber6.get() != '':
            if self.idnumber7.get() != '':
                self.dub_remover()

    def csv_reader1(self):
        if self.idnumber0 == 0:
            print('\n!!! please set ID field in sdf file')
        elif self.idnumber4 == 0:
            print('\n!!! please set ID field in csv file')
        else:
            self.csv_reader()

    def csv_reader(self):
        print('\n' + '=' * 45)
        dub_in_csv = 0
        no_id_from_csv = 0
        csv_added = 0
        list_id_values = []
        csv_number_input = 0
        empty_number = 0
        total_scv_data_rows = 0
        n = 0
        x = 0
        csv_counter = 0
        listid2 = []
        list5 = []
        empty_list = []
        openfile2 = open(self.csv_file_name, "r")
        if self.csv_file_name[-4:] == '.csv':
            for row in csv.reader(openfile2):
                csv_counter += 1
                if n == 0:
                    for i in row:
                        listid2.append(i)
                    n += 1
                    positionid2 = listid2.index(self.idnumber4)
                    continue
                if n == 1:
                    for i in row:
                        if i == '':
                            list_id_values.append(empty_list)
                        else:
                            list_id_values.append(i)
                    if csv_counter >= int(self.csf_count/10):
                        x += 10
                        print('\n loaded another ' + str(csv_counter) + ' csv_rows, ' + str(x) + '%')
                        csv_counter = 0
                        RedyaGui.update(self)
                if list_id_values[(int(positionid2))] != empty_list:
                    if list_id_values[(int(positionid2))] not in self.list4:
                        self.list4.append(list_id_values[(int(positionid2))])
                        csv_number_input += 1
                    else:
                        dub_in_csv += 1
                    for i in range(len(listid2)):
                        try:
                            if listid2[i] in self.xraniliwe.get(str(list_id_values[(int(positionid2))])).filds1:
                                xraniliwe5 = {listid2[i] + '_new': list_id_values[i]}
                                self.xraniliwe.get(str(list_id_values[(int(positionid2))])).filds1.update(xraniliwe5)
                                csv_added += 1
                            else:
                                xraniliwe5 = {listid2[i]: list_id_values[i]}
                                self.xraniliwe.get(str(list_id_values[(int(positionid2))])).filds1.update(xraniliwe5)
                                csv_added += 1
                        except (KeyError, AttributeError):
                            no_id_from_csv += 1
                            break
                else:
                    empty_number += 1
                total_scv_data_rows += 1
                list_id_values = []
            openfile2.close()
        if self.csv_file_name[-4:] == '.tsv':
            for row in csv.reader(openfile2, delimiter="\t"):
                csv_counter += 1
                if n == 0:
                    for i in row:
                        listid2.append(i)
                    n += 1
                    positionid2 = listid2.index(self.idnumber4)
                    continue
                if n == 1:
                    for i in row:
                        if i == '':
                            list_id_values.append(empty_list)
                        else:
                            list_id_values.append(i)
                    if csv_counter >= int(self.csf_count/10):
                        x += 10
                        print('\n loaded another ' + str(csv_counter) + ' tsv_rows, ' + str(x) + '%')
                        csv_counter = 0
                        RedyaGui.update(self)
                if list_id_values[(int(positionid2))] != empty_list:
                    if list_id_values[(int(positionid2))] not in self.list4:
                        self.list4.append(list_id_values[(int(positionid2))])
                        csv_number_input += 1
                    else:
                        dub_in_csv += 1
                    for i in range(len(listid2)):
                        try:
                            if listid2[i] in self.xraniliwe.get(str(list_id_values[(int(positionid2))])).filds1:
                                xraniliwe5 = {listid2[i] + '_new': list_id_values[i]}
                                self.xraniliwe.get(str(list_id_values[(int(positionid2))])).filds1.update(xraniliwe5)
                                csv_added += 1
                            else:
                                xraniliwe5 = {listid2[i]: list_id_values[i]}
                                self.xraniliwe.get(str(list_id_values[(int(positionid2))])).filds1.update(xraniliwe5)
                                csv_added += 1
                        except (KeyError, AttributeError):
                            no_id_from_csv += 1
                            break
                else:
                    empty_number += 1
                total_scv_data_rows += 1
                list_id_values = []
            openfile2.close()
        for structur in self.list4:
            if structur not in self.xraniliwe:
                list5.append(structur)
        if list5:
            csv_error = self.file_name[0:-4] + '_write_sdf_error.txt'
            writefile3 = open(csv_error, "w")
            for base in list5:
                writefile3.write(str(base) + ' - No such "' + str(self.idnumber0) + '" in sdf' + '\n')
                # print('\n' + str(base) + ' - No such value of "' + str(self.idnumber0) + '" field in sdf')
            print('\n' + str(csv_error) + '  saved')
        print('\nno id from csv in sdf = ' + str(no_id_from_csv))
        print('\ndublicates in csv = ' + str(dub_in_csv))
        print('\ncsv rows with id = ' + str(csv_number_input))
        print('\ncsv rows added to sdf = ' + str(int(csv_added/len(listid2))))
        print('\nno id in csv row = ' + str(empty_number))
        print('\ntotal scv data rows = ' + str(total_scv_data_rows))

    def list_saver4(self):
        print('\n' + '=' * 45)
        if self.list_xran:
            if self.list_nd_xran:
                writefile1 = asksaveasfile(mode='w', defaultextension='.txt', filetypes=[("lst files", "*.lst"), ("txt files", "*.txt"), ("any", "*.*")])
                if writefile1:
                    upload_struture = 0
                    for key2 in self.list_nd_xran:
                        writefile1.write(key2 + '\n')
                        upload_struture += 1
                    writefile1.close()
                    print('\n number of list records saved = ' + str(upload_struture))
                else:
                    print('\n!!! saving list file canceled')
            else:
                print('\n !!! do some operation with list first')
        else:
            print('\n!!! No opened list file')

    def csv_saver1(self):
        print('\n' + '=' * 45)
        self.dict0 = self.xraniliwe
        self.sdf_writer()

    def csv_saver2(self):
        self.list_list = self.list4
        self.write_list_sdf2()

    def clear_cash(self):
        print('\n!!!cash cleaned!!!')
        self.file_name = 0
        self.csv_file_name = 0
        self.filds = []
        self.id_var1 = ''
        self.id_var0 = ''
        self.idnumber0 = 0
        self.idnumber2 = 0
        self.field_processing0 = 0
        self.procesing_id0 = 0
        self.sorted_move0 = 0
        self.sorted_fild0 = 0
        self.sdf_all = collections.OrderedDict()
        self.xraniliwe = collections.OrderedDict()
        # self.counter1 = 0
        # self.counter2 = 0
        self.id_var3 = ''
        self.id_var4 = ''
        self.id_var5 = ''
        self.id_var6 = ''
        self.id_var7 = ''
        self.id_var8 = ''
        self.ent_text = ''
        self.ent_text1 = ''
        self.ent_text2 = ''
        self.list_saver = ''
        self.list_saver_act = ''
        self.idnumber4 = 0
        self.idnumber6 = ''
        self.idnumber7 = ''
        self.adding_field = 0
        self.adding_field_val = 0
        self.file_name_save = 0
        self.list_name = 0
        self.list_xran = []
        self.list_nd_xran = []
        self.list_list = []
        self.dict0 = 0
        self.dict2 = 0
        self.sorted_move2 = 0
        self.sorted_move3 = 0
        self.listid2 = []
        self.list4 = []
        self.input_sdf_count = 0
        self.csf_count = 0

if __name__ == "__main__":
    RedyaGui()
    mainloop()
