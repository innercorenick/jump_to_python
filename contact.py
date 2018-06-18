class Contact:

    def __init__(self, name, phone_number, e_mail, addr):
        self.name=name
        self.phone_number=phone_number
        self.e_mail=e_mail
        self.addr=addr

    def print_info(self):
        print('Name:    ', self.name)
        print('Phone Number:    ', self.phone_number)
        print('E-Mail:    ', self.e_mail)
        print('Adrress:    ', self.addr)
    
def set_contact():
    name=input('Name:   ')
    phone_number=input('Phone Number:   ')
    e_mail=input('E-Mail:   ')
    addr=input('Adrress:    ')
    contact=Contact(name, phone_number, e_mail, addr)
    return contact

def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴 선택:  ')
    return int(menu)

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name==name:
            del contact_list[i]

def run():
    contact_list=[]
    while True:
        menu=print_menu()
        if menu==1:
            contact=set_contact()
            contact_list.append(contact)
        elif menu==2:
            print_contact(contact_list)
        elif menu==3:
            name=input('Name:   ')
            delete_contact(contact_list, name)
        elif menu==4:
            print('프로그램이 종료됩니다.')
            break
        if menu>4 or menu<0:
            print('error')

if __name__=='__main__':
    run()
