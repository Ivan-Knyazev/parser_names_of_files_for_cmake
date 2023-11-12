import os
import dotenv
import shutil
from typing import List


class Files:
    def __init__(self) -> None:
        dotenv.load_dotenv()

        self.path_cpp = os.getenv("PATH_CPP")
        self.path_result = os.getenv("PATH_RESULT")
        self.list_of_files = os.listdir(self.path_cpp)

        if os.path.exists(self.path_result):
            shutil.rmtree(self.path_result)
        os.mkdir(self.path_result)

        self.res_path = self.path_result + "\\\\CMakeLists.txt"

    def get_list_of_files(self) -> List[str]:
        return self.list_of_files

    def write_result(self) -> None:
        result_file = open(self.res_path, "x")
        result_file.close()

        with open(self.res_path, "w") as result_file:
            for n in range(len(self.list_of_files)):
                if self.list_of_files[n] == "CMakeLists.txt":
                    continue
                new_string = "add_executable(" + self.list_of_files[n][:-4] + \
                             " " + self.list_of_files[n] + ")\n"
                result_file.write(new_string)
                print("Writed " + self.list_of_files[n])

    def __repr__(self) -> str:
        return self.path_result


if __name__ == "__main__":
    cpps = Files()

    try:
        cpps.write_result()
    except:
        print("\nError :<")
    else:
        print("\nOK :>")
    finally:
        print("Programm was finished")

# print(cpps.get_list_of_files())
