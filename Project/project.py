import tkinter as tk
import sqlite3
from tkinter import messagebox, ttk
from tkinter import *



class LIMS(tk.Tk):
        def __init__(self):
            super().__init__()
            self.connect = sqlite3.connect('LIMS.db')
            self.c = self.connect.cursor()
            self.c.execute('''CREATE TABLE IF NOT EXISTS Book (
                                                    Book_ID  INTEGER   PRIMARY KEY
                                                                        UNIQUE,
                                                    Title    VARCHAR (100),
                                                    Author   VARCHAR (100),
                                                    Category VARCHAR (100),
                                                    Edition  INTEGER);''')
            self.c.execute('''CREATE TABLE IF NOT EXISTS Patron (
                                                    Patron_ID INTEGER       UNIQUE,
                                                    Name      VARCHAR (100),
                                                    Phone     INTEGER,
                                                    Email     VARCHAR (100)  );''')
            self.c.execute('''CREATE TABLE IF NOT EXISTS Issue (
                                                                Patron_ID INTEGER       UNIQUE,
                                                                Book_ID   INTEGER,
                                                                Date     VARCHAR (100)  );''')
            self.c.execute('''CREATE TABLE IF NOT EXISTS Login (
                                                                            Username VARCHAR (100),
                                                                            password     VARCHAR (100)  );''')
            self.connect.commit()
            self.title('LIMS')
            self.geometry("1280x720")
            self.configure(bg="#FFFFFF")
            self.canvas = tk.Canvas(
                self,
                bg="#FFFFFF",
                height=720,
                width=1280,
                bd=0,
                highlightthickness=0,
                relief="ridge"
            )
            self.canvas.place(x=0, y=0)
            self.image_image_1 = tk.PhotoImage(file="image_1.png")
            self.image_1 = self.canvas.create_image(
                640.0,
                360.0,
                image=self.image_image_1
            )
            self.canvas.create_rectangle(
                0.0,
                150.0,
                1302.0,
                160.0,
                fill="#7D3021",
                outline="")

            self.tablogin()
            self.resizable(False, False)

        def show_pass(self):
            if self.entry2.cget('show') == '':
                self.entry2.config(show='*')
                self.showbtn.config(text='Show')
            else:
                self.entry2.config(show='')
                self.showbtn.config(text='Hide')


        def tablogin(self):
            self.framelogin = tk.Frame(self, bg='white')
            self.framelogin.place(x=0, y=0, width=1280, height=720)
            self.img = PhotoImage(file="thuvien-removebg-preview.png")
            self.imglabel = Label(self.framelogin, image=self.img, bg='white')
            self.imglabel.place(x=0, y=0, width=670, height=720)
            self.img2 = PhotoImage(file="user.png")
            self.img2label = Label(self.framelogin, image=self.img2, bg='white')
            self.img2label.place(x=863, y=100)
            self.loginlabel = Label(self.framelogin, text="Login", fg='slateblue', bg='white', font=("Arial Bold", 25))
            self.loginlabel.place(x=882, y=230)
            self.labellogin = Label(self.framelogin, text='LIBRARY ', fg='slateblue', bg='white', font=("Arial Bold", 50))
            self.labellogin.pack(side=TOP)
            self.Label1 = Label(self.framelogin, text="Username", fg='slateblue', bg='white', font=('Anton', 15))
            self.Label1.place(x=760, y=300)
            self.label2 = Label(self.framelogin, text="Password", fg='slateblue', bg='white', font=('Anton', 15))
            self.label2.place(x=760, y=360)
            self.entry1 = Entry(self.framelogin, bd=2, font=('Anton', 10))
            self.entry1.place(x=760, y=330, width=350, height=30)
            self.entry2 = Entry(self.framelogin, bd=2, font=('Anton', 10),show="*")
            self.entry2.place(x=760, y=390, width=350, height=30)
            self.signinbtn = Button(self.framelogin, text='Sign in', command=self.login, width=49, height=2, bg='slateblue', bd=1, fg='white')
            self.signinbtn.place(x=760, y=465)
            self.showbtn = Button(self.framelogin, text="show", width=5, bd=0, command=self.show_pass, bg="slateblue", fg='white')
            self.showbtn.place(x=1067, y=390, height=30)
            self.canvas.create_rectangle(
                0.0,
                150.0,
                1302.0,
                160.0,
                fill="#7D3021",
                outline="")

        def login(self):
            self.search_username = self.entry1.get()
            self.c.execute("SELECT * FROM Login WHERE Username  = ?", (self.search_username,))
            self.connect.commit()
            login_username = self.c.fetchone()
            if login_username:
                self.search_password = self.entry2.get()
                self.c.execute("SELECT * FROM Login WHERE password = ?", (self.search_password,))
                self.connect.commit()
                login_password = self.c.fetchone()
                if login_password:
                    self.main_tab()
                    self.framelogin.destroy()
                else:
                    messagebox.showwarning('Warning', 'Input information is incorrect')
                    self.entry1.delete(0, "end")
                    self.entry2.delete(0, "end")
            else:
                messagebox.showwarning('Warning', 'Input information is incorrect')
                self.entry1.delete(0, "end")
                self.entry2.delete(0, "end")

        def tablogout(self):
            self.delete_button()
            self.tablogin()

        def delete_button(self):
            self.add_book_button.destroy()
            self.remove_book_button.destroy()
            self.edit_book_button.destroy()
            self.search_book_button.destroy()
            self.add_patron_button.destroy()
            self.remove_patron_button.destroy()
            self.issue_book_button.destroy()
            self.return_book_button.destroy()
            self.list_book_button.destroy()
            self.logoutbutton.destroy()

        # ---------------------------Add book--------------------
        def tab2_add_book(self):
            self.labelbookid = tk.Label(self, text='Book ID:', relief="solid", font=('Anton', 20), bg='#E6CC91')
            self.labelbooktitle = tk.Label(self, text='Book Title:', relief="solid", font=('Anton', 20), bg='#E6CC91')
            self.labelbookauthor = tk.Label(self, text='Book Author:', relief="solid", font=('Anton', 20), bg='#E6CC91')
            self.labelbookcategory = tk.Label(self, text='Book Category:', relief="solid", font=('Anton', 20), bg='#E6CC91')
            self.labelbookedition = tk.Label(self, text='Book Edition :', relief="solid", font=('Anton', 20), bg='#E6CC91')

            self.labelbookid.place(
                x=80,
                y=180,
                width=250,
                height=60
            )
            self.labelbooktitle.place(
                x=80,
                y=260,
                width=250,
                height=60
            )
            self.labelbookauthor.place(
                x=80,
                y=350,
                width=250,
                height=60
            )
            self.labelbookcategory.place(
                x=80,
                y=440,
                width=250,
                height=60
            )
            self.labelbookedition.place(
                x=80,
                y=520,
                width=250,
                height=60
            )

            self.entry_bookid = tk.Entry(self, bd=7, bg='#E6CC91', font=('Anton', 20))
            self.entry_title = tk.Entry(self, bd=7, bg='#E6CC91', font=('Anton', 20))
            self.entry_author = tk.Entry(self, bd=7, bg='#E6CC91', font=('Anton', 20))
            self.entry_category = tk.Entry(self, bd=7, bg='#E6CC91', font=('Anton', 20))
            self.entry_edition = tk.Entry(self, bd=7, bg='#E6CC91', font=('Anton', 20))
            self.entry_bookid.place(x=350, y=185, width=650)
            self.entry_title.place(x=350, y=265, width=650)
            self.entry_author.place(x=350, y=355, width=650)
            self.entry_category.place(x=350, y=445, width=650)
            self.entry_edition.place(x=350, y=525, width=650)
            self.submit1_button = tk.Button(self, text='Add Book', font=('Anton', 20), bg='#E6CC91', relief="solid",
                                            command=self.submit1)
            self.submit1_button.place(
                x=550,
                y=600,
                width=250,
                height=60
            )

        def submit1(self):
            self.book_id = self.entry_bookid.get()
            self.title_book = self.entry_title.get()
            self.author = self.entry_author.get()
            self.category = self.entry_category.get()
            self.edition = self.entry_edition.get()
            self.c.execute('INSERT INTO Book VALUES (?, ?, ?, ?, ?)',
                           (self.book_id, self.title_book, self.author, self.category, self.edition))
            self.connect.commit()
            self.clear()
            messagebox.showinfo("Success!!!", "Add book is completed")

        def clear(self):
            self.entry_bookid.delete(0, 'end')
            self.entry_title.delete(0, 'end')
            self.entry_author.delete(0, 'end')
            self.entry_category.delete(0, 'end')
            self.entry_edition.delete(0, 'end')

        def tab_add_book(self):
            self.delete_button()
            self.tab2_add_book()

            def back():
                self.labelbookid.destroy()
                self.labelbooktitle.destroy()
                self.labelbookauthor.destroy()
                self.labelbookcategory.destroy()
                self.labelbookedition.destroy()
                self.back_button.destroy()
                self.entry_bookid.destroy()
                self.entry_title.destroy()
                self.entry_author.destroy()
                self.entry_category.destroy()
                self.entry_edition.destroy()
                self.submit1_button.destroy()

                self.main_tab()

            self.back_button = tk.Button(self, text='back', relief="solid", font=('Anton', 20), command=back, bg='#E6CC91')
            self.back_button.place(x=1050, y=180, width=150, height=60)

        # ---------------------------remove book-------------------

        def tab_remove_book(self):
            self.delete_button()
            self.remove_book = tk.Label(self, text='Book ID:', relief="solid", font=('Anton', 20), bg='#E6CC91')
            self.remove_book.place(
                x=80,
                y=280,
                width=250,
                height=60
            )
            self.entry_removebook = tk.Entry(self, bd=7, bg='#E6CC91', font=('Anton', 20))
            self.entry_removebook.place(
                x=350, y=285, width=650
            )
            self.button_remove = tk.Button(self, text='Remove Book', relief="solid", font=('Anton', 20), bg='#E6CC91',
                                           command=self.submit2)
            self.button_remove.place(
                x=540, y=400, width=250
            )

            def back():
                self.remove_book.destroy()
                self.entry_removebook.destroy()
                self.back_button.destroy()
                self.button_remove.destroy()
                self.main_tab()

            self.back_button = tk.Button(self, text='back', relief="solid", font=('Anton', 20), command=back, bg='#E6CC91')
            self.back_button.place(x=1050, y=180, width=150, height=60)

        def submit2(self):
            self.delete_data = self.entry_removebook.get()
            self.c.execute("DELETE FROM Book WHERE Book_ID=?", (self.delete_data,))
            self.connect.commit()
            self.clearremovebook()
            if self.c.rowcount > 0:
                messagebox.showinfo('Library System', 'YOUR DATA IS DELETED !')
            else:
                messagebox.showerror('Library System', 'YOUR DATA IS NOT FOUND !')

        def clearremovebook(self):
            self.entry_removebook.delete(0, 'end')

        # ---------------------------edit book--------------------------------

        def tab_edit_book(self):
            self.delete_button()
            self.label_editbook = tk.Label(self, text='Book ID:', relief="solid", font=('Anton', 20), bg='#E6CC91')
            self.label_editbook.place(
                x=80,
                y=280,
                width=200,
                height=60
            )
            self.entry_editbook = tk.Entry(self, bd=7, bg='#E6CC91', font=('Anton', 20))
            self.entry_editbook.place(
                x=350, y=285, width=650
            )

            def backtab1():
                self.label_editbook.destroy()
                self.entry_editbook.destroy()
                self.back_button.destroy()
                self.search_button.destroy()
                self.main_tab()
            self.back_button = tk.Button(self, text='back', relief="solid", font=('Anton', 20), command=backtab1, bg='#E6CC91')
            self.back_button.place(x=1050, y=180, width=150, height=60)
            self.search_button = tk.Button(self, text='Search', relief="solid", font=('Anton', 20), command=self.editbook_tab,
                                    bg='#E6CC91')
            self.search_button.place(
                x=550,
                y=399,
                width=200,
                height=60
            )

        def editbook_tab(self):
            self.datas = self.entry_editbook.get()
            self.c.execute("SELECT * FROM book WHERE Book_ID='" + self.datas + "'")
            self.connect.commit()
            check = self.c.fetchone()
            if check:
                self.newtab = Toplevel(self)
                self.newtab.title('Edit Book')
                self.newtab.geometry("1000x700")
                self.newtab.configure(bg='#E6CC91')
                self.labelbookid = tk.Label(self.newtab, text='Book ID:', relief="solid", font=('Anton', 20), bg='#E6CC91')
                self.labelbooktitle = tk.Label(self.newtab, text='Book Title:', relief="solid", font=('Anton', 20),
                                               bg='#E6CC91')
                self.labelbookauthor = tk.Label(self.newtab, text='Book Author:', relief="solid", font=('Anton', 20),
                                                bg='#E6CC91')
                self.labelbookcategory = tk.Label(self.newtab, text='Book Category:', relief="solid", font=('Anton', 20),
                                                  bg='#E6CC91')
                self.labelbookedition = tk.Label(self.newtab, text='Book Edition :', relief="solid", font=('Anton', 20),
                                                 bg='#E6CC91')

                self.labelbookid.place(
                    x=50,
                    y=100,
                    width=200,
                    height=60
                )
                self.labelbooktitle.place(
                    x=50,
                    y=180,
                    width=200,
                    height=60
                )
                self.labelbookauthor.place(
                    x=50,
                    y=260,
                    width=200,
                    height=60
                )
                self.labelbookcategory.place(
                    x=50,
                    y=340,
                    width=200,
                    height=60
                )
                self.labelbookedition.place(
                    x=50,
                    y=420,
                    width=200,
                    height=60
                )

                self.entry_bookid = tk.Entry(self.newtab, bd=7, bg='#E6CC91', font=('Anton', 20))
                self.entry_title = tk.Entry(self.newtab, bd=7, bg='#E6CC91', font=('Anton', 20))
                self.entry_author = tk.Entry(self.newtab, bd=7, bg='#E6CC91', font=('Anton', 20))
                self.entry_category = tk.Entry(self.newtab, bd=7, bg='#E6CC91', font=('Anton', 20))
                self.entry_edition = tk.Entry(self.newtab, bd=7, bg='#E6CC91', font=('Anton', 20))
                self.entry_bookid.place(x=300, y=105, width=650)
                self.entry_title.place(x=300, y=185, width=650)
                self.entry_author.place(x=300, y=265, width=650)
                self.entry_category.place(x=300, y=345, width=650)
                self.entry_edition.place(x=300, y=425, width=650)
                self.editbook_button = tk.Button(self.newtab, text='Edit Book', font=('Anton', 20), bg='#E6CC91',
                                                 relief="solid", command=self.edit_book)
                self.editbook_button.place(
                    x=420,
                    y=600,
                    width=250,
                    height=60
                )

            else:
                messagebox.showerror('Library System', 'YOUR DATA IS NOT FOUND !')

        def edit_book(self):
            self.id = self.entry_bookid.get()
            self.ti = self.entry_title.get()
            self.au = self.entry_author.get()
            self.ca = self.entry_category.get()
            self.ed = self.entry_edition.get()
            self.c.execute(
                "UPDATE book SET Book_ID='" + self.id + "', Title='" + self.ti + "',Author='" + self.au + "',Category='" + self.ca + "',Edition='" + self.ed + "' WHERE Book_ID='" + self.datas + "'")
            self.connect.commit()
            messagebox.showinfo('Library System', 'YOUR DATA IS UPDATED!')
        # ------------------ Search book--------------------

        def tab_search_book(self):
            self.delete_button()
            self.search_book = tk.Label(self, text='Book ID:', relief="solid", font=('Anton', 20), bg='#E6CC91')
            self.search_book.place(
                x=80,
                y=280,
                width=250,
                height=60
            )
            self.entry_searchbook = tk.Entry(self, bd=7, bg='#E6CC91', font=('Anton', 20))
            self.entry_searchbook.place(
                x=350, y=285, width=650
            )
            self.button_search = tk.Button(self, text='Search', relief="solid", font=('Anton', 20), bg='#E6CC91',
                                           command=self.search_book1)
            self.button_search.place(
                x=540, y=400, width=250
            )

            def back():
                self.button_search.destroy()
                self.search_book.destroy()
                self.entry_searchbook.destroy()
                self.back_button.destroy()
                self.main_tab()

            self.back_button = tk.Button(self, text='back', relief="solid", font=('Anton', 20), command=back, bg='#E6CC91')
            self.back_button.place(x=1050, y=180, width=150, height=60)

        def search_book1(self):
            self.search_id = self.entry_searchbook.get()
            self.c.execute("SELECT * FROM Book WHERE Book_ID = ?", (self.search_id,))
            self.connect.commit()
            book_info = self.c.fetchone()
            if book_info:
                book_window = tk.Toplevel()
                book_window.title("Book Information")
                book_window.geometry('450x250')
                book_window.configure(bg='#E6CC91')

                book_id_label = tk.Label(book_window, text="Book ID: {}".format(book_info[0]), font=('Anton', 15), bg='#E6CC91')
                book_id_label.pack()

                title_label = tk.Label(book_window, text="Title: {}".format(book_info[1]), font=('Anton', 15), bg='#E6CC91')
                title_label.pack()

                author_label = tk.Label(book_window, text="Author: {}".format(book_info[2]), font=('Anton', 15), bg='#E6CC91')
                author_label.pack()

                category_label = tk.Label(book_window, text="Category: {}".format(book_info[3]), font=('Anton', 15), bg='#E6CC91')
                category_label.pack()

                edition_label = tk.Label(book_window, text="Edition: {}".format(book_info[4]), font=('Anton', 15), bg='#E6CC91')
                edition_label.pack()
            else:
                messagebox.showwarning('Library System', 'YOUR DATA IS NOT AVAILABLE !')

        # ------------------ Add patron----------
        def tab2_add_patron(self):
            self.labelpatronid = tk.Label(self, text='Patron ID:', relief="solid", font=('Anton', 20), bg='#E6CC91')
            self.labelpatronname = tk.Label(self, text='Patron Name:', relief="solid", font=('Anton', 20), bg='#E6CC91')
            self.labelpartonemail = tk.Label(self, text='Patron Email:', relief="solid", font=('Anton', 20), bg='#E6CC91')
            self.labelpatronphone = tk.Label(self, text='Patron Phone:', relief="solid", font=('Anton', 20), bg='#E6CC91')
            self.labelpatronid.place(
                x=80,
                y=180,
                width=250,
                height=60
            )
            self.labelpatronname.place(
                x=80,
                y=260,
                width=250,
                height=60
            )
            self.labelpartonemail.place(
                x=80,
                y=350,
                width=250,
                height=60
            )
            self.labelpatronphone.place(
                x=80,
                y=440,
                width=250,
                height=60
            )
            self.entry_patronid = tk.Entry(self, bd=7, bg='#E6CC91', font=('Anton', 20))
            self.entry_patronname = tk.Entry(self, bd=7, bg='#E6CC91', font=('Anton', 20))
            self.entry_patronemail = tk.Entry(self, bd=7, bg='#E6CC91', font=('Anton', 20))
            self.entry_patronphone = tk.Entry(self, bd=7, bg='#E6CC91', font=('Anton', 20))
            self.entry_patronid.place(x=350, y=185, width=650)
            self.entry_patronname.place(x=350, y=265, width=650)
            self.entry_patronemail.place(x=350, y=445, width=650)
            self.entry_patronphone.place(x=350, y=355, width=650)

            self.submit1_patron = tk.Button(self, text='Add Patron', font=('Anton', 20), bg='#E6CC91', relief="solid",
                                            command=self.submitpatron)
            self.submit1_patron.place(
                x=550,
                y=600,
                width=250,
                height=60
            )

        def submitpatron(self):
            self.patron_id = self.entry_patronid.get()
            self.patron_name = self.entry_patronname.get()
            self.patron_email = self.entry_patronemail.get()
            self.patron_phone = self.entry_patronphone.get()
            self.c.execute('INSERT INTO Patron VALUES ( ?, ?, ?, ?)',
                           (self.patron_id, self.patron_name, self.patron_email, self.patron_phone))
            messagebox.showinfo("Success!!!", "Add Patron is completed")
            self.connect.commit()
            self.clearpatron()

        def clearpatron(self):
            self.entry_patronid.delete(0, 'end')
            self.entry_patronname.delete(0, 'end')
            self.entry_patronemail.delete(0, 'end')
            self.entry_patronphone.delete(0, 'end')

        def tab_add_patron(self):
            self.delete_button()
            self.tab2_add_patron()

            def back():
                self.labelpatronphone.destroy()
                self.labelpartonemail.destroy()
                self.labelpatronname.destroy()
                self.labelpatronid.destroy()
                self.back_button.destroy()
                self.entry_patronid.destroy()
                self.entry_patronname.destroy()
                self.entry_patronphone.destroy()
                self.entry_patronemail.destroy()
                self.submit1_patron.destroy()
                self.main_tab()

            self.back_button = tk.Button(self, text='back', relief="solid", font=('Anton', 20), command=back, bg='#E6CC91')
            self.back_button.place(x=1050, y=180, width=150, height=60)

        # -------------Remove patron ---------------

        def tab_remove_patron(self):
            self.delete_button()
            self.removepatron = tk.Label(self, text='Remove Patron:', relief="solid", font=('Anton', 20), bg='#E6CC91')
            self.removepatron.place(
                x=80,
                y=280,
                width=250,
                height=60
            )
            self.entry_removepatron = tk.Entry(self, bd=7, bg='#E6CC91', font=('Anton', 20))
            self.entry_removepatron.place(
                x=350, y=285, width=650
            )
            self.button_removepatron = tk.Button(self, text='Remove Book', relief="solid", font=('Anton', 20), bg='#E6CC91',
                                                 command=self.submit4)
            self.button_removepatron.place(
                x=540, y=400, width=250
            )

            def back():
                self.entry_removepatron.destroy()
                self.removepatron.destroy()
                self.button_removepatron.destroy()
                self.back_button.destroy()
                self.main_tab()

            self.back_button = tk.Button(self, text='back', relief="solid", font=('Anton', 20), command=back, bg='#E6CC91')
            self.back_button.place(x=1050, y=180, width=150, height=60)

        def submit4(self):
            self.delete_patron = self.entry_removepatron.get()
            self.c.execute("DELETE FROM Patron WHERE Patron_ID=?", (self.delete_patron,))
            self.connect.commit()
            self.clearpatron2()
            if self.c.rowcount > 0:
                messagebox.showinfo('Library System', 'YOUR DATA IS DELETED !')
            else:
                messagebox.showerror('Library System', 'YOUR DATA IS NOT FOUND !')
        def clearpatron2(self):
            self.entry_removepatron.delete(0,'end')

        # --------------Issue book----------------------

        def tab_issue_book(self):
            self.delete_button()
            self.patronidissuelabel = tk.Label(self, text='Patron ID:', relief="solid", font=('Anton', 15),
                                               bg='#E6CC91')
            self.patronidissuelabel.place(
                x=120,
                y=180,
                width=100,
                height=30
            )

            self.entrypatronidissue = tk.Entry(self, bd=2, bg='#E6CC91', font=('Anton', 20))
            self.entrypatronidissue.place(x=230, y=175, width=200)

            self.Ok1 = tk.Button(self, text='OK', font=('Anton', 15), bg='#E6CC91', relief="solid",
                                 command=self.search_patron)
            self.Ok1.place(
                x=255,
                y=230,
                width=50,
                height=30
            )

            def back():
                self.patronidissuelabel.destroy()
                self.entrypatronidissue.destroy()
                self.back_button.destroy()
                self.Ok1.destroy()
                self.frameinforpatron.destroy()
                self.labelframe1.destroy()
                self.idbookissue_label.destroy()
                self.idbookissue_entry.destroy()
                self.patron_id_label.destroy()
                self.namepatron_label.destroy()
                self.phonepatron_label.destroy()
                self.emailpatron_label.destroy()
                self.Ok2.destroy()
                self.main_tab()

            self.back_button = tk.Button(self, text='back', relief="solid", font=('Anton', 20), command=back,
                                         bg='#E6CC91')
            self.back_button.place(x=1050, y=180, width=150, height=60)

        def search_patron(self):
            self.search_id = self.entrypatronidissue.get()
            self.c.execute("SELECT * FROM Patron WHERE Patron_ID = ?", (self.search_id,))
            self.connect.commit()
            patron_info = self.c.fetchone()
            if patron_info:
                self.inputbookID()
                self.frameinforpatron = tk.Frame(self, bg='#C2A87C')
                self.frameinforpatron.place(x=50, y=300, width=500, height=350)
                self.labelframe1 = tk.Label(self.frameinforpatron, text='PATRON INFORMATION:', bg='#C2A87C',
                                            font=('Anton', 18))
                self.labelframe1.pack(side=TOP)
                self.patron_id_label = tk.Label(self.frameinforpatron, text="Patron ID: {}".format(patron_info[0]),
                                                font=('Anton', 18), bg='#C2A87C')
                self.patron_id_label.pack()

                self.namepatron_label = tk.Label(self.frameinforpatron, text="Patron name: {}".format(patron_info[1]),
                                                 font=('Anton', 18), bg='#C2A87C')
                self.namepatron_label.pack()

                self.phonepatron_label = tk.Label(self.frameinforpatron, text="Patron phone: {}".format(patron_info[2]),
                                                  font=('Anton', 18), bg='#C2A87C')
                self.phonepatron_label.pack()

                self.emailpatron_label = tk.Label(self.frameinforpatron, text="Patron email: {}".format(patron_info[3]),
                                                  font=('Anton', 18),
                                                  bg='#C2A87C')
                self.emailpatron_label.pack()
            else:
                messagebox.showwarning('Library System', 'YOUR DATA IS NOT AVAILABLE !')

        def inputbookID(self):
            self.idbookissue_label = tk.Label(self, text='Book ID', bg='#E6CC91', font=('Anton', 18))
            self.idbookissue_label.place(x=500, y=180, width=100, height=30)
            self.idbookissue_entry = tk.Entry(self, font=('Anton', 18), bg='#E6CC91')
            self.idbookissue_entry.place(x=610, y=175, width=200)
            self.Ok2 = tk.Button(self, text='OK', font=('Anton', 15), bg='#E6CC91', relief="solid",
                                 command=self.checkidbbookissue)
            self.Ok2.place(
                x=630,
                y=230,
                width=50,
                height=30
            )

        def checkidbbookissue(self):
            self.search_idbook = self.idbookissue_entry.get()
            self.c.execute("SELECT * FROM Book WHERE Book_ID = ?", (self.search_idbook,))
            self.connect.commit()

            book_info = self.c.fetchone()
            if book_info:
                self.c.execute("SELECT * FROM Issue WHERE Book_ID = ?", (self.search_idbook,))
                self.connect.commit()
                check_issue = self.c.fetchone()
                if check_issue:
                    messagebox.showwarning('Library System', 'THIS BOOK HAS BEEN ISSUED!')
                else:
                    self.newwindownissue()
            else:
                messagebox.showwarning('Library System', 'YOUR DATA IS NOT AVAILABLE !')

        def newwindownissue(self):
            self.issue_window = tk.Toplevel()
            self.issue_window.title("Book issue")
            self.issue_window.geometry('500x450')
            self.issue_window.configure(bg='#E6CC91')

            self.search_idbook = self.idbookissue_entry.get()
            self.c.execute("SELECT * FROM Book WHERE Book_ID = ?", (self.search_idbook,))
            self.connect.commit()
            book_info = self.c.fetchone()
            if book_info:
                self.frameinforbook = tk.Frame(self.issue_window, bg='#E6CC91')
                self.frameinforbook.place(x=100, y=60, width=300, height=350)

                self.labelframe1 = tk.Label(self.frameinforbook, text='BOOK INFORMATION', bg='#E6CC91',
                                            font=('Anton', 18), fg='red')
                self.labelframe1.pack(side=TOP)

                self.book_id_label = tk.Label(self.frameinforbook, text="Book ID: {}".format(book_info[0]),
                                              font=('Anton', 15), bg='#E6CC91')
                self.book_id_label.pack()

                self.title_label = tk.Label(self.frameinforbook, text="Title: {}".format(book_info[1]),
                                            font=('Anton', 15), bg='#E6CC91')
                self.title_label.pack()

                self.author_label = tk.Label(self.frameinforbook, text="Author: {}".format(book_info[2]),
                                             font=('Anton', 15), bg='#E6CC91')
                self.author_label.pack()

                self.category_label = tk.Label(self.frameinforbook, text="Category: {}".format(book_info[3]),
                                               font=('Anton', 15), bg='#E6CC91')
                self.category_label.pack()

                self.edition_label = tk.Label(self.frameinforbook, text="Edition: {}".format(book_info[4]),
                                              font=('Anton', 15), bg='#E6CC91')
                self.edition_label.pack()

            self.label1 = tk.Label(self.issue_window, text=' Patron ID :' + self.entrypatronidissue.get(), bg='#E6CC91',
                                   font=('Anton', 18))
            self.label1.pack(side=TOP)

            self.label3 = tk.Label(self.issue_window, text='Date issue', bg='#E6CC91', font=('Anton', 18))
            self.label3.place(
                x=20,
                y=300,
                width=200,
                height=30
            )
            self.entrylabel3 = tk.Entry(self.issue_window, bd=7, bg='#E6CC91', font=('Anton', 20))
            self.entrylabel3.place(
                x=200,
                y=290,
                width=250,
                height=45
            )

            self.issue = tk.Button(self.issue_window, text="Issue", bg='#E6CC91', font=('Anton', 18),
                                   command=self.submitissue)
            self.issue.pack(side=BOTTOM)

        def submitissue(self):
            self.idpatronissue = self.entrypatronidissue.get()
            self.idbookissue = self.idbookissue_entry.get()
            self.dateissue = self.entrylabel3.get()
            self.c.execute('INSERT INTO Issue VALUES (?, ?, ?)',
                           (self.idpatronissue, self.idbookissue, self.dateissue,))
            self.connect.commit()
            messagebox.showinfo("Warning", "Issue book is completed")

        # ------------Return book ----------------

        def tab_return_book(self):
            self.delete_button()
            self.label_patron_id = tk.Label(self, text='Patron ID:', relief="solid", font=('Anton', 20), bg='#E6CC91')
            self.label_patron_id.place(
                x=100, y=280, width=150, height=50
            )
            self.entrypatronid_return = tk.Entry(self, bd=7, bg='#E6CC91', font=('Anton', 20))
            self.entrypatronid_return.place(x=260, y=280, width=250, height=50)
            self.button_ok = tk.Button(self, text='Ok', font=('Anton', 20), bg='#E6CC91',
                                       command=self.check_patronid_return)
            self.button_ok.place(x=300, y=460, width=100, height=50)

            def back():
                self.label_patron_id.destroy()
                self.back_button.destroy()
                self.button_ok.destroy()
                self.entrypatronid_return.destroy()
                self.main_tab()

            self.back_button = tk.Button(self, text='back', relief="solid", font=('Anton', 20), command=back,
                                         bg='#E6CC91')
            self.back_button.place(x=1050, y=180, width=150, height=60)

        def check_patronid_return(self):
            self.search_patronid_return = self.entrypatronid_return.get()
            self.c.execute("SELECT * FROM Issue WHERE Patron_ID = ?", (self.search_patronid_return,))
            self.connect.commit()
            checkpatronid = self.c.fetchone()
            if checkpatronid:
                self.newreturnwin()
            else:
                messagebox.showerror('PATRON NOT EXIST!')

        def newreturnwin(self):
            self.return_window = tk.Toplevel()
            self.return_window.title("Book Information")
            self.return_window.geometry('350x300')
            self.return_window.configure(bg='#E6CC91')
            self.book_id_return_label = tk.Label(self.return_window, text='Book ID', font=('Anton', 15),
                                                 bg='#E6CC91')
            self.book_id_return_label.place(x=30, y=100)
            self.bookid_new_entry = tk.Entry(self.return_window, bd=3, width=27, bg='#E6CC91')
            self.bookid_new_entry.place(x=130, y=105)
            self.ok_newwindown = tk.Button(self.return_window, text='Return', font=('Anton', 16), bg='#E6CC91',
                                           command=self.check_bookid_return)
            self.ok_newwindown.place(x=150, y=200)

        def check_bookid_return(self):
            self.search_bookid_return = self.bookid_new_entry.get()
            self.c.execute("SELECT * FROM Issue WHERE Book_ID = ?", (self.search_bookid_return,))
            self.connect.commit()
            checkbookid = self.c.fetchone()
            if checkbookid:
                self.delete_data_issue = self.bookid_new_entry.get()
                self.c.execute("DELETE FROM Issue WHERE Book_ID=?", (self.delete_data_issue,))
                self.connect.commit()
                messagebox.showinfo('library System', 'RETURN BOOK COMPLETED !!')
            else:
                messagebox.showerror('Library System', 'YOUR DATA IS NOT FOUND !')

        # ------------list book ----------------
        def tab_list_book(self):
            self.delete_button()
            self.table_frame = tk.Frame(self, bg='#C2A87C', bd=1, relief='flat')
            self.table_frame.place(x=0, y=161, width=996, height=557)

            self.scroll_x = tk.Scrollbar(self.table_frame, orient=tk.HORIZONTAL)
            self.scroll_y = tk.Scrollbar(self.table_frame, orient=tk.VERTICAL)
            self.book_table = ttk.Treeview(self.table_frame,
                                           columns=("Book_ID", "Title", "Author", "Category", "Edition"),
                                           xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
            self.scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
            self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
            self.scroll_x.config(command=self.book_table.xview)
            self.scroll_y.config(command=self.book_table.yview)

            self.book_table.heading("Book_ID", text="Book_ID")
            self.book_table.heading("Title", text="Title")
            self.book_table.heading("Author", text="Author")
            self.book_table.heading("Category", text="Category")
            self.book_table.heading("Edition", text="Edition")

            self.book_table['show'] = 'headings'
            self.book_table.column("Book_ID", width=100)
            self.book_table.column("Title", width=300)
            self.book_table.column("Author", width=200)
            self.book_table.column("Category", width=200)
            self.book_table.column("Edition", width=100)
            self.book_table.pack(fill=tk.BOTH, expand=1)
            self.fetch_data()

            def back():
                self.table_frame.destroy()
                self.book_table.destroy()
                self.back_button.destroy()
                self.main_tab()

            self.back_button = tk.Button(self, text='back', relief="solid", font=('Anton', 20), command=back,
                                         bg='#E6CC91')
            self.back_button.place(x=1050, y=180, width=150, height=60)

        def fetch_data(self):
            self.c.execute("SELECT * FROM Book")
            self.connect.commit()
            self.row = self.c.fetchall()
            for self.row in self.row:
                self.book_table.insert('', 'end', values=self.row)

        def main_tab(self):
            # ----Add book-----

            self.add_book_button = tk.Button(self,
                                             text='1. Add books',
                                             bg='#E6CC91',
                                             font=('Anton', 20),
                                             relief="solid",
                                             command=self.tab_add_book,
                                             highlightthickness=0
                                             )
            self.add_book_button.place(
                x=93.0,
                y=220.0,
                width=252.0,
                height=67.0
            )
            # -------Remove book-------

            self.remove_book_button = tk.Button(self,
                                                text='2. Remove book',
                                                highlightthickness=0,
                                                relief="solid",
                                                bg='#E6CC91',
                                                font=('Anton', 20),
                                                command=self.tab_remove_book
                                                )
            self.remove_book_button.place(
                x=93.0,
                y=315.0,
                width=252.0,
                height=67.0
            )
            # -----Edit book-----------

            self.edit_book_button = tk.Button(self,
                                              text='3. Edit book',
                                              bg='#E6CC91',
                                              highlightthickness=0,
                                              relief="solid",
                                              font=('Anton', 20),
                                              command=self.tab_edit_book
                                              )
            self.edit_book_button.place(
                x=93,
                y=413,
                width=252.0,
                height=67.0
            )

            # ------ search book ---------------
            self.search_book_button = tk.Button(self,
                                                text='4. Search book',
                                                bg='#E6CC91',
                                                highlightthickness=0,
                                                relief="solid",
                                                font=('Anton', 20),
                                                command=self.tab_search_book
                                                )
            self.search_book_button.place(
                x=93.0,
                y=510.0,
                width=252.0,
                height=67.0
            )
            # -------------Add patron------------

            self.add_patron_button = tk.Button(self,
                                               text='5. Add Patron',
                                               bg='#E6CC91',
                                               relief="solid",
                                               font=('Anton', 20),
                                               highlightthickness=0,
                                               command=self.tab_add_patron

                                               )
            self.add_patron_button.place(
                x=420.0,
                y=220.0,
                width=252.0,
                height=67.0
            )

            # ------------ Remove patron---------------
            self.remove_patron_button = tk.Button(self,
                                                  text='6. Remove Patron',
                                                  bg='#E6CC91',
                                                  font=('Anton', 20),
                                                  relief="solid",
                                                  highlightthickness=0,
                                                  command=self.tab_remove_patron
                                                  )
            self.remove_patron_button.place(
                x=420.0,
                y=315.0,
                width=252.0,
                height=67.0
            )
            # ---------Issue book----------
            self.issue_book_button = tk.Button(self,
                                               text='7. Issue book',
                                               relief="solid",
                                               bg='#E6CC91',
                                               font=('Anton', 20),
                                               highlightthickness=0,
                                               command=self.tab_issue_book

                                               )
            self.issue_book_button.place(
                height=67.0,
                x=420.0,
                y=413.0,
                width=252.0
            )
            # -----------------Return books---------------
            self.return_book_button = tk.Button(self,
                                              text='8. Return book',
                                              highlightthickness=0,
                                              relief="solid",
                                              font=('Anton', 20),
                                              bg='#E6CC91',
                                              command=self.tab_return_book
                                              )
            self.return_book_button.place(
                x=420.0,
                y=510.0,
                width=252.0,
                height=67.0
            )
            # -----------------List books---------------
            self.list_book_button = tk.Button(self,
                                              text='9. List book',
                                              highlightthickness=0,
                                              relief="solid",
                                              font=('Anton', 20),
                                              bg='#E6CC91',
                                              command=self.tab_list_book
                                              )
            self.list_book_button.place(
                x=249.0,
                y=600,
                width=252.0,
                height=67.0
            )
            #-----------------log out----------------
            self.logoutbutton = tk.Button(self,
                                          text='Log out',
                                          highlightthickness=0,
                                          relief="solid",
                                          font=('Anton', 20),
                                          bg='#E6CC91',
                                          command=self.tablogout
                                          )
            self.logoutbutton.place(
                x=1040.0,
                y=230,
                width=180.0,
                height=40.0
            )


if __name__ == '__main__':
    app = LIMS()
    app.mainloop()
