# main.py

farm_tasks = []
def show_menu():
    print("/n===== ระบบจัดการงานในฟาร์ม=====")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. เเสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4.สรุปจำนวนงานในเเต่ละประเภท")
    print("5. ออกจากโปรเเกรม")

def add_task():
    name = input("ชื่องาน: ")
    task_type = input("ประเภทงาน (พืช/สัตว์): ")
    detail = input("รายละเอียดเพิ่มเติม: ")
    date = input("วันที่ต้องทำ: ")

    farm_tasks.append({
        "name": name,
        "type": task_type.lower(),
        "detail": detail,
        "date":  date
    })
    print("เพิ่มงานสำเร็จ")

    # ฟังก์ชัน: เเสดงรายการทั้งหมดทั้งหมด
    def show_all_tasks():
        if not farm_tasks:
            print("ไม่มีงานในระบบ")
            return
        print("/nราายการทั้งหมด:")
        for i, task in enumerate(farm_tasks, start=1):
            print(f"{i} . [{task['type']}] {task['name']} - {task['datail']} (วันที่: {task['date']})")
    # ฟังก์ชัน: ลบงาน
    def delete_task():
        show_all_tasks()
        try:
            task_num = int(input("ระบุหมายเลขที่ต้องการลบ: "))
            if 1 <= task_num <= len(farm_tasks):
                removed = farm_tasks.pop(farm_num - 1)
                print(f"delete: {removed['name']} เรียบร้อย")
            else: 
                print("หมายเลขไม่ถูกต้อง")
        except:
            print("ใส่ตัวเลขใหม่")
    # ฟังก์ชัน: สรุปจำนวนงานเเต่ละประเภท
    def summmarize_tasks():
        summary = {}
    for task in farm_tasks:
        if task["type"] not in summary:
            summary[task["type"]] = 0
        summary[task["type"]] += 1
    print("/nสรุปงาน:")
    for task_type, count in summary.items():
        print(f"- {task_type}: {count} งาน")
while True:
    show_menu()
    choise = input("เลือกเมนูเลย(1-5): ")
    if choise == "1":
        add_task()
    elif choise =="2":
        show_all_tasks()
    elif choise =="3":
            delete_all_tasks()
    elif choise =="4":
        summary_all_tasks()
    elif choise =="5":
        print("ออกจากระบบ")
        break
        print("กรุณาเลือกเมนูให้ถูกต้อง (1-5)")