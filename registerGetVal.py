from tkinter import messagebox
import validateRegisterData

def getVal(nameBox, userBox, emailBox, passBox, repassBox, c, o):
    # Strip gets rid of whitespace at the beginning or the end of the string
    # 1.0 and end-1c is where the indexing starts and ends
    name = nameBox.get("1.0", "end-1c")
    username = userBox.get("1.0", "end-1c").strip()
    email = emailBox.get("1.0", "end-1c").strip()
    password = passBox.get().strip()
    repassword = repassBox.get().strip()
    school = c.get()
    level = o.get()
    if (len(name) < 1 or len(username) < 1 or len(email) < 1 or len(password) < 1 or school == "School name" or
            level == "Level"):
        messagebox.showwarning("Empty Field", "Please fill out all fields")
    else:
        # Capitalises the first letter of the first name and surname for the database
        space = 0
        for i in range(len(name)):
            if name[i].isspace():
                space = i
        name = name[0].capitalize() + name[1:space] + " " + name[space + 1].capitalize() + name[space + 2:]

        # PUTS ACCOUNT IN THE DATABASE STUDENT OR TEACHER
        if school == "School not listed":
            messagebox.showwarning("School not listed", "You can't create an account because your school "
                                                        "isn't registered to PROGRAM NAME. Please talk to a teacher if "
                                                        "you want to register with us")
            # ADD PROGRAM NAME
        else:
            if password != repassword:
                messagebox.showwarning("Passwords don't match", "Passwords don't match. Please try again")
            else:
                validateRegisterData.checkVal(username, email, password)
