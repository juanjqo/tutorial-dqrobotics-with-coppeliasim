# Example CMAKE project for Ubuntu
cmake_minimum_required(VERSION 3.5)

project(template)

set(CMAKE_CXX_STANDARD 11)

FIND_PACKAGE(Threads REQUIRED)
FIND_PACKAGE(Eigen3 REQUIRED)
INCLUDE_DIRECTORIES(${EIGEN3_INCLUDE_DIR})
ADD_COMPILE_OPTIONS(-Werror=return-type
                    -Wall -Wextra -Wmissing-declarations
                    -Wredundant-decls -Woverloaded-virtual)

add_executable(${PROJECT_NAME}
               ${PROJECT_NAME}.cpp)

target_link_libraries(${PROJECT_NAME}
                      dqrobotics
                      dqrobotics-interface-vrep
                      Threads::Threads)