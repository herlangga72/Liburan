from Module import CRUD

Engine= CRUD.sql()
Engine..connect("root","127.0.0.1","rancang_desain")
Engine.Delete_data("NIM_MHS",200180710)
Engine.create("Herlangga",200180710,"Pascal","m.2","Pass")
Engine.Tampilkan_data()
Engine.Update_data ("HYS",200180710,"Pascal","m.2","Pass")
Engine.Tampilkan_data()
