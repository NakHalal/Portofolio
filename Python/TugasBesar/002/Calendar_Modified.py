import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from tkinter.scrolledtext import ScrolledText
from time import strftime
import locale

todos = {}

def detailTodo(cb=None):
    tanggal = str(cal.get_date())
    try:
        selectedItem = treev.focus()
        selectedIndex = treev.item(selectedItem)['text']
        selectedTodo = todos[tanggal][selectedIndex]
        ListTodo()
    except Exception:
        pass
    else:
        win = tk.Toplevel(bg='grey', cursor='hand1')
        '''
        Make Windows UnResizeable for Clearly Visible Title
        '''
        win.resizable(width=False, height=False)
        win.wm_title("Detail ToDo")
        '''
        Change Windows Size and Center the Position PopUp
        '''
        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        positionRight = int(root.winfo_screenwidth()/2)
        positionDown = int(root.winfo_screenheight()/2)
        win.geometry("230x125+{}+{}".format(positionRight, positionDown))
        judul = tk.StringVar(value=selectedTodo['judul'])
        '''
        Stick to West
        '''
        tk.Label(win, text="Tanggal: ", bg='grey', fg='white').grid(row=0, column=0, sticky='W')
        '''
        Stick to West
        '''
        tk.Label(win, text="{} | {}".format(tanggal, selectedTodo['waktu']), bg='grey', fg='white').grid(row=0 ,column=1, sticky="W")
        '''
        Stick to West
        '''
        tk.Label(win, text="Judul: ", bg='grey', fg='white').grid(row=1, column=0, sticky='W')
        tk.Entry(win, state="disabled", textvariable=judul, disabledbackground='grey', disabledforeground='white', width=24).grid(row=1, column=1, sticky="W")
        '''
        Stick to NorthWest
        '''
        tk.Label(win, text="Keterangan: ", bg='grey', fg='white').grid(row=2, column=0, sticky="NW")
        keterangan = ScrolledText(win, width=21, height=5, bg='grey', fg='white', font='Calibri 8')
        keterangan.grid(row=2, column=1, sticky="W")
        keterangan.insert(tk.INSERT, selectedTodo['keterangan'])
        keterangan.configure(state="disabled")
    
def LoadTodos():
    tanggal = str(cal.get_date())
    global todos
    f = open('backup.bin', 'r')
    data = f.read()
    f.close()
    todos = eval(data)
    ListTodo()

def SaveTodos():
    tanggal = str(cal.get_date())
    f = open('backup.bin', 'w')
    f.write(str(todos))
    f.close()

def delTodo():
    tanggal = str(cal.get_date())
    selectedItem = treev.focus()
    try:
        todos[tanggal].pop(treev.item(selectedItem)['text'])
    except Exception:
        pass
    else:
        ListTodo()

def ListTodo(cb=None):
    tanggal = str(cal.get_date())
    for i in treev.get_children():
        treev.delete(i)
    if tanggal in todos:
        for i in range(len(todos[tanggal])):
            treev.insert("","end", text=i, values=(todos[tanggal][i]['waktu'], todos[tanggal][i]['judul']), tags=('fg', 'bg'))
            treev.tag_configure('bg', background='yellow')
            treev.tag_configure('fg', foreground='red')

def addTodo(win, key, jam, menit, judul, keterangan):
    tanggal = str(cal.get_date())
    if jam.get() < 10:
        newTodo = {
            'waktu':'0{}:{}'.format(jam.get(), menit.get()),
            'judul': judul.get(),
            'keterangan': keterangan.get('1.0', tk.END)
        }
    if menit.get() < 10:
        newTodo = {
            'waktu':'{}:0{}'.format(jam.get(), menit.get()),
            'judul': judul.get(),
            'keterangan': keterangan.get('1.0', tk.END)
        }
    if jam.get() < 10 and menit.get() < 10:
        newTodo = {
            'waktu':'0{}:0{}'.format(jam.get(), menit.get()),
            'judul': judul.get(),
            'keterangan': keterangan.get('1.0', tk.END)
        }
    else:
        newTodo = {
            'waktu':'{}:{}'.format(jam.get(), menit.get()),
            'judul': judul.get(),
            'keterangan': keterangan.get('1.0', tk.END)
        }
    if key in todos:
        todos[key].append(newTodo)
    else:
        todos[key] = [newTodo]
    win.destroy()
    ListTodo()

def AddForm():
    tanggal = str(cal.get_date())
    win = tk.Toplevel(bg='grey')
    '''
    Change Windows Size and Center the Position PopUp
    '''
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/2)
    positionDown = int(root.winfo_screenheight()/2)
    win.geometry("220x135+{}+{}".format(positionRight, positionDown))
    '''
    Make Windows UnResizeable for Clearly Visible Title
    '''
    win.resizable(width=False, height=False)
    win.wm_title("Tambah")
    jam = tk.IntVar(value=10)
    menit = tk.IntVar(value=30)
    judul = tk.StringVar(value="")
    '''
    Stick to West
    '''
    tk.Label(win, text="Waktu: ", bg='grey', fg='white').grid(row=0, column=0, sticky='W')
    '''
    Change Spinbox Width
    '''
    tk.Spinbox(win, from_=0, to=23, textvariable=jam, width=8, bg='white', fg='black').grid(row=0, column=1)
    tk.Spinbox(win, from_=0, to=59, textvariable=menit, width=8, bg='white', fg='black').grid(row=0, column=2)
    '''
    Stick to West
    '''
    tk.Label(win, text="Judul: ", bg='grey', fg='white').grid(row=1, column=0, sticky='W')
    tk.Entry(win, textvariable=judul).grid(row=1, column=1, columnspan=4)
    '''
    Stick to North West
    '''
    tk.Label(win, text="Keterangan: ", bg='grey', fg='white').grid(row=2, column=0, sticky='NW')
    '''
    Change ScrolledText Width
    '''
    keterangan = ScrolledText(win, width=13, height=5)
    '''
    Change Columnspan
    '''
    keterangan.grid(row=2, column=1, columnspan=4, rowspan=4)
    tk.Button(win, text="Tambah", activebackground="grey", bd=3, relief="raised", background='white', fg='black', command=lambda: addTodo(win, tanggal, jam, menit, judul, keterangan)).grid(row=5, column=0)

def title():
    locale.setlocale(locale.LC_ALL, 'id_ID')
#    tanggal = str(cal.get_date())
#    waktu = strftime('%I:%M %p')
    tanggal = strftime("%d")
    hari = strftime("%A")
    waktu = strftime('%H:%M:%S')
    bulan = strftime('%B')
    tahun = strftime("%Y")
    root.title(hari + ', ' + tanggal + ' ' + bulan + ' ' + tahun + " | " + waktu)
    root.after(1000, title)

#def donothing():
#   filewin = Toplevel(root)
#   button = Button(filewin, text="Do nothing button")
#   button.pack()

root = tk.Tk()
root.resizable(height = 0, width = 0)

#menubar = Menu(root)
#filemenu = Menu(menubar, tearoff = 0)
#filemenu.add_command(label = "Load", command = LoadTodos, activeforeground='white', activebackground='#4A6984')
#filemenu.add_command(label = "Save", command = SaveTodos, activeforeground='white', activebackground='#4A6984')
#filemenu.add_separator()
#filemenu.add_command(label = "Exit", command = root.quit, activeforeground='white', activebackground='#4A6984')
#menubar.add_cascade(label = "File", menu = filemenu, activeforeground='white', activebackground='#4A6984')
#root.config(menu = menubar)
'''
Center the Calendar Position PopUp
'''
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth)
positionDown = int(root.winfo_screenheight()/2 - windowHeight)
root.geometry("+{}+{}".format(positionRight, positionDown))
s = ttk.Style()
'''
Change Appearance
'''
s.theme_use('clam')
s.configure("Treeview",
            rowheight=16,
            fieldbackground='grey',
            background='grey',
            foreground='grey',
            arrowcolor='grey',
            bg='grey',
            fg='grey',)
#root.title("Calendar")

'''
Change Font and Date Format to %dd-%mm-%yyyy
'''
cal = Calendar(root, font="Calibri 14 bold", selectmode="day", locale="id_ID", cursor="target", date_pattern='dd-mm-y', foreground='white', background='grey', firstweekday='sunday', disabledbackground='black', disabledforeground='black', bordercolor='black', normalbackground='grey', headersbackground='grey', headersforeground='white', selectbackground='black', selectforeground='white', weekendbackground='red', weekendforeground='black', othermonthforeground='black', othermonthbackground='white', othermonthweforeground='black', othermonthwebackground='white', borderwidth=22, showweeknumbers=True)
#print(cal.get_date())
cal.grid(row=0, column=0, sticky="N", rowspan=1)
cal.bind("<<CalendarSelected>>", ListTodo)

tanggal = str(cal.get_date())

treev = ttk.Treeview(root)
treev.grid(row=1, column=0, sticky="WSE")

scrollBar = tk.Scrollbar(root, orient="vertical", command=treev.yview, bg='black')
scrollBar.grid(row=1, column=0, sticky="ENS", rowspan=4)

treev.configure(yscrollcommand=scrollBar.set)
treev.bind("<Double-1>", detailTodo)

treev['columns'] = ("1", "2")
treev['show'] = 'headings'
treev.column("1", width=100)
treev.heading('1', text="Jam")
treev.heading('2', text="Judul")

btnAdd = tk.Button(root, text="Tambah", width=25, command=AddForm, activebackground="#4A6984", bd=3, bg='grey', fg='white', relief="raised")
btnAdd.grid(row=5, column=0, sticky="W", pady=3, padx=2)

btnDel = tk.Button(root, text="Hapus", width=25, command=delTodo, activebackground="#4A6984", bd=3, bg='grey', fg='white', relief="raised")
btnDel.grid(row=5, column=0, sticky="E", pady=3, padx=2)

btnLoad = tk.Button(root, text="Load", width=25, command=LoadTodos, activebackground="#4A6984", bd=3, bg='grey', fg='white', relief="raised")
btnLoad.grid(row=6, column=0, sticky="W", pady=3, padx=2)

btnSave = tk.Button(root, text="Save", width=25, command=SaveTodos, activebackground="#4A6984", bd=3, bg='grey', fg='white', relief="raised")
btnSave.grid(row=6, column=0, sticky="E", pady=3, padx=2)

title()
root.mainloop()