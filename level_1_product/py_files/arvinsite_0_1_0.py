import pymongo
from bson.objectid import ObjectId


class Contact:
    name = None
    phone = None
    mobile = None
    whatsapp = None
    telegram = None
    instagram = None
    email = None
    web = None


while True:
    print("1.add a contact")
    print("2.show contact list")
    print("3.search")
    print("4.delete a contact")
    print("5.edit a contact")
    print("6.exit")
    print("please enter something between 1 to 6")
    ask = int(input("what are you want to do? "))
    my_client = pymongo.MongoClient("mongodb://localhost:27017")
    db_name = my_client["contact_saver"]
    contact_col = db_name["contacts"]
    match ask:
        case 1:
            c = Contact()
            c_name = input("name: ")
            c_phone = input("phone: ")
            c_mobile = input("mobile number: ")
            c_whatsapp = input("whatsapp id: ")
            c_tlegram = input("telegram id: ")
            c_instagram = input("instagram id: ")
            c_email = input("email: ")
            c_web = input("website: ")
            c.name = c_name
            c.phone = c_phone
            c.mobile = c_mobile
            c.whatsapp = c_whatsapp
            c.telegram = c_tlegram
            c.instagram = c_instagram
            c.email = c_email
            c.web = c_web
            con_dict = c.__dict__
            print(con_dict)
            print(list(con_dict))
            for principal in list(con_dict):
                if principal != "_id" and con_dict[principal] == "":
                    del con_dict[principal]
            contact_col.insert_one(con_dict)
        case 2:
            for contact in contact_col.find():
                print("_________")
                for clean in list(contact):
                    if clean != "_id":
                        print(f"{clean}: {contact[clean]}")
                print("_________")
                
        case 3:
            counter = 0
            search = input("enter something to search: ")
            for dic in contact_col.find():
                for find in dic:
                    if search == dic[find]:
                        counter += 1
                        print(f"I found a {find} for your search...")
                        print("here is hole information of contact...")
                        print("_________")
                        for tell in dic:
                            print(f"{tell}: {dic[tell]}")
                        print("_________")
            if counter == 0:
                print("nothing found...")
        case 4:
            counter = 0
            deleting = input(
                "enter the something about contact you want to delete: ")
            for delete in contact_col.find():
                for finding in delete:
                    if deleting == delete[finding]:
                        counter += 1
                        print("_________")
                        print("contact info:")
                        for show in delete:
                            if show != "_id":
                                print(f"{show}: {delete[show]}")
                        print("_________")
                        sure = input(
                            "you sure you want to delete the contact (1.yes, 2.no)? ")
                        if sure == "1":
                            contact_col.delete_one(delete)
                            print("deleted")
                            break
                        elif sure == "2":
                            print("ok")
                            break
                if counter >= 1:
                    break
            if counter == 0:
                print("not found...")
        case 5:
            counter = 0
            editing = input(
                "enter the something about contact you want to edit: ")
            for edit in contact_col.find():
                for get_find in edit:
                    if editing == edit[get_find]:
                        counter += 1
                        print("_________")
                        print("contact info:")
                        for show in edit:
                            if show != "_id":
                                print(f"{show}: {edit[show]}")
                        print("_________")
                        sure_edit = input(
                            "you sure you want to edit this contact (1.yes, 2.no)? ")
                        if sure_edit == "1":
                            print("1.edit name")
                            print("2.edit phone")
                            print("3.edit mobile")
                            print("4.edit whatsapp")
                            print("5.edit telegram")
                            print("6.edit instagram")
                            print("7.edit email")
                            print("8.edit web")
                            edit_select = int(
                                input("please enter something between 1 to 8: "))
                            match edit_select:
                                case 1:
                                    get_new_name = input("enter new name: ")
                                    new_name = {
                                        "$set": {"name":  get_new_name}}
                                    contact_col.update_one(edit, new_name)
                                    print("name changed...")
                                case 2:
                                    get_new_phone = input("enter new phone: ")
                                    new_phone = {
                                        "$set": {"phone": get_new_phone}}
                                    contact_col.update_one(edit, new_phone)
                                    print("phone changed...")
                                case 3:
                                    get_new_mobile = input(
                                        "enter new mobile: ")
                                    new_mobile = {
                                        "$set": {"mobile": get_new_mobile}}
                                    contact_col.update_one(edit, new_mobile)
                                    print("mobile changed...")
                                case 4:
                                    get_new_whatsapp = input(
                                        "enter new whatsapp id: ")
                                    new_whatsapp = {
                                        "$set": {"whatsapp": get_new_whatsapp}}
                                    contact_col.update_one(edit, new_whatsapp)
                                    print("whatsapp id changed...")
                                case 5:
                                    get_new_telegram = input(
                                        "enter new telegram id: ")
                                    new_telegram = {
                                        "$set": {"telegram": get_new_telegram}}
                                    contact_col.update_one(edit, new_telegram)
                                    print("telegram id changed...")
                                case 6:
                                    get_new_instagram = input(
                                        "enter new instagram id: ")
                                    new_instagram = {
                                        "$set": {"instagram": get_new_instagram}}
                                    contact_col.update_one(edit, new_instagram)
                                    print("instagram id changed...")
                                case 7:
                                    get_new_email = input("enter new email: ")
                                    new_email = {
                                        "$set": {"email": get_new_email}}
                                    contact_col.update_one(edit, new_email)
                                    print("email changed...")
                                case 8:
                                    get_new_web = input("enter new web: ")
                                    new_web = {"$set": {"web": get_new_web}}
                                    contact_col.update_one(edit, new_web)
                                    print("website address changed...")
                        elif sure == "2":
                            print("ok")
                            break
                if counter >= 1:
                    break
            if counter == 0:
                print("not found...")
        case 6:
            break
