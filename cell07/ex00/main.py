# main.py 
farm_taske =  []
def show_menu() :
    print("/n===== ฟาร์มของฉัน =====")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. เเสดงรายการทั้งหมด")
    print("3. ลบบงาน")
    print("4. สรุปจำนวนงานในเเต่ละประเภท")
    print("5. ออกจากโปรเเกรม")
def add_task():
    name = input("ชื่องาน: ")
    task_type  = input("ประเภทงาน (พืช/สัตว์): ")
    dete = input ("วันที่ต้องทำ")
    def show_all_tasks():
        if not farm_tasks:
            print("ไม่มีงานในระบบ")