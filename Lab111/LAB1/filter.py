Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> groupmates = [
	{
		"name":"Иван",
		"surname": "Гетманенко",
		"exams": ["Информатика","Английский язык","Web"],
		"marks": [4,4,5]
		},
	{
		"name":"Тимур",
		"surname": "Дзариев",
		"exams": ["Информатика","Английский язык","Web"],
		"marks": [5,3,5]
		},
	{
		"name":"Максим",
		"surname": "Кувайцев",
		"exams": ["Информатика","Английский язык","Web"],
		"marks": [3,5,4]
		},
	{
		"name":"Светлана",
		"surname": "Захарова",
		"exams": ["Информатика","Английский язык","Web"],
		"marks": [5,4,5]
		},
	{
		"name":"Варвара",
		"surname": "Захарова",
		"exams": ["Информатика","Английский язык","Web"],
		"marks": [4,4,4]
		}
	]

        def print_students(students):
            print(u"Имя".ljust(15), u"Фамилия".ljust(10),
        u"Экзамены".ljust(40), u"Оценки".ljust(10))
            for student in students:
                print(student["name"].ljust(15),
        student["surname"].ljust(10), str(student["exams"].ljust(30),
        str(student["marks"].ljust(20))
        print_students(groupmates)                                
                                                         
                      
