# import time 
  
# class Student:  
#     def init(self, name, direction):  
#         self.name = name  
#         self.direction = direction  
#         self.books = []  
#         self.knowledge = 0  
#         self.is_ready_to_work = False  
#         self.languages = {}  
          
#     def read_book(self, book):  
#         self.books.append(book)  
#         self.__add_points(100)  
#         self.easter_egg()  
          
#     def do_homework(self):  
#         self.__add_points(10)  
#         self.easter_egg()  
          
#     def do_project(self):  
#         self.__add_points(50)  
#         self.easter_egg()  
  
#     def learn_new_language(self, language, level):  
#         if level < 1 or level > 100:  
#             raise ValueError("Level must be between 1 and 100.")  
#         self.languages[language] = level  
#         self.easter_egg()  
  
#     def easter_egg(self):  
#         if self.knowledge % 10 == 0:  
#             print("Одна ошибка и ты ошибся..")  
#             time.sleep(10)  
  
#     def __add_points(self, points):  
#         self.knowledge += points  
#         if self.knowledge >= 1000 and not self.is_ready_to_work:  
#             self.is_ready_to_work = True  
#             print("Этот студент готов к работе!")