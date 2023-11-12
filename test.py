with open("D:\\Projects\\parser_names_of_files_for_c++\\result\\CMakeLists.txt", "w") as result_file:
    for i in range(10):
        new_string = "add_executable(" + "1" + " " + "1.cpp" + ")\n"
        print(new_string)
        result_file.write(new_string)
