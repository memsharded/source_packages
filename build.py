import os

os.system("conan create src_pkg source/0.1@user/testing")
os.system("conan create consumer consumer/0.1@user/testing")