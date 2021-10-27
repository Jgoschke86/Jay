    #!/usr/bin/python3
    
    import tkinter as tk
    
    def solong(): main.destroy()
    
    main = tk.Tk()
    
    for i in range(3):
        r = tk.Radiobutton(main,text="R" + str(i))
        r.pack()
    
    for i in range(3):
        r = tk.Radiobutton(main,text="R" + str(i))
        r.pack(anchor='w')
    
    b1 = tk.Button(main,text="Button 1",command=solong)
    b1.pack()
    
    b2 = tk.Button(main,text="Button 2",command=solong)
    b2.pack(fill=tk.X)
    
    b3 = tk.Button(main,text="Button 3",command=solong)
    b3.pack(fill=tk.Y)
    
    b4 = tk.Button(main,text="Button 4",command=solong)
    b4.pack(fill=tk.BOTH)
    
    b5 = tk.Button(main,text="Button 5",command=solong)
    b5.pack(fill=tk.X,expand=True)
    
    b6 = tk.Button(main,text="Button 6",command=solong)
    b6.pack(fill=tk.BOTH,expand=True)
    
    b7 = tk.Button(main,text="Button 7",command=solong)
    b7.pack(padx=10,pady=10)
    
    b8 = tk.Button(main,text="Button 8",command=solong)
    b8.pack(pady=20)
    
    b9 = tk.Button(main,text="Button 9",command=solong)
    b9.pack(ipadx=10,ipady=10)
    
    b10 = tk.Button(main,text="Button 10",command=solong)
    b10.pack(ipady=20)
    
    tk.mainloop()