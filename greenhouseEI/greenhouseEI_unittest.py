import os
import shutil
import unittest
from greenhouseEI.tools import *


class Testgreenhouse(unittest.TestCase):
    #test info function
    def test_info(self):
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        print(path)
        self.assertEqual(1, info("JS39-65", "2018-04-11", path))
        self.assertEqual(1, info("71-001", "2019-07-03", path))
        #input wrong plantID
        self.assertEqual(0, info("JS39-651", "2018-04-11", path))
        self.assertEqual(0, info("", "2018-04-11", path))
        #input wrong path
        self.assertEqual(0, info("JS39-65", "2018-04-11", "user/"))
        self.assertEqual(0, info("JS39-65", "2018-04-11", "user/desktop"))
        self.assertEqual(0, info("JS39-65", "2018-04-11", "user1/"))
        self.assertEqual(0, info("JS39-65", "2018-04-11", ""))

    #test unzip function
    #when you run this test function, there should be .zip file in the folder
    def test_unzip(self):
        path = os.getcwd()
        self.assertEqual(1, unzip("JS39-65", "2018-04-11", "Hyp", path))
        files = os.listdir(path)
        for file in files:
            if ("JS39-65" in file) and ("2018-04-11" in file):
                file_name = file
                print(file_name)
                break
        shutil.rmtree(file_name)

        #input wrong plantID
        self.assertEqual(0, unzip("JS3965", "2018-04-11", "Hyp", path))
        self.assertEqual(0, unzip("JS9-65", "2018-04-11", "Hyp", path))
        self.assertEqual(0, unzip("J39-65", "2018-04-11", "Hyp", path))
        #self.assertEqual(0, unzip("", "2018-04-11", "Hyp", path))

        #input wrong image type
        self.assertEqual(0, unzip("JS39-65", "2018-0411", "yp", path))
        self.assertEqual(0, unzip("JS39-65", "2018-0411", "Hp", path))
        self.assertEqual(0, unzip("JS39-65", "2018-0411", "Hy", path))
       # self.assertEqual(0, unzip("JS39-65", "2018-0411", "", path))
        #input wrong path
        self.assertEqual(0, unzip("JS39-65", "2018-0411", "Hyp", "user/"))
        self.assertEqual(0, unzip("JS39-65", "2018-0411", "Hyp", "user/desk1"))
        self.assertEqual(0, unzip("JS39-65", "2018-0411", "Hyp", "user/desk2"))
        self.assertEqual(0, unzip("JS39-65", "2018-0411", "Hyp", ""))

    #test preprocess fuction
    #when you run this test function, there should be the Hyp folder in the folder
    def test_preprocess(self):
        path = os.getcwd()
        unzip("JS39-65", "2018-04-11", "Hyp", path)
        self.assertEqual(1, preprocess("JS39-65", "2018-04-11", path))

        files = os.listdir(path)
        for file in files:
            if ("JS39-65" in file) and ("2018-04-11" in file):
                file_name = file
                print(file_name)
                break
        print(file_name)
        shutil.rmtree(file_name)
        npy_name = file_name.split("_")[2] + "_" + file_name.split("_")[3]
        npy_name = npy_name + ".npy"
        os.remove(npy_name)

        #input wrong plantID
        self.assertEqual(0, preprocess("JS39-651", "2018-04-11", path))
        self.assertEqual(0, preprocess("JS3965", "2018-04-11", path))
        self.assertEqual(0, preprocess("JS3651", "2018-04-11", path))
        self.assertEqual(0, preprocess("", "2018-04-11", path))
        #input wrong date
        self.assertEqual(0, preprocess("JS39-65", "2018-04-111", path))
        self.assertEqual(0, preprocess("JS39-65", "2018-041", path))
        self.assertEqual(0, preprocess("JS39-65", "20184-111", path))
        self.assertEqual(0, preprocess("JS39-65", "201111", path))
        self.assertEqual(0, preprocess("JS39-65", "", path))
        #input wrong path
        self.assertEqual(0, preprocess("JS39-65", "2018-04-11", "user/desktop"))
        self.assertEqual(0, preprocess("JS39-65", "2018-04-11", "user1/"))
        self.assertEqual(0, preprocess("JS39-65", "2018-04-11", "user2/"))
        self.assertEqual(0, preprocess("JS39-65", "2018-04-11", ""))

    #test zip2np function:
    #when you run this test function, there should be only .zip file in the folder
    def test_zip2np(self):
        path = os.getcwd()
        print(path)
        self.assertEqual(1, zip2np("JS39-65", "2018-04-11", path))

        files = os.listdir(path)
        for file in files:
            if ("JS39-65" in file) and ("2018-04-11" in file):
                file_name = file
                print(file_name)
                break
        shutil.rmtree(file_name)
        npy_name = file_name.split("_")[2] + "_" + file_name.split("_")[3]
        npy_name = npy_name + ".npy"
        os.remove(npy_name)

        #input wrong plantID
        self.assertEqual(0, zip2np("JS39-651", "2018-04-11", path))
        self.assertEqual(0, zip2np("JS3965", "2018-04-11", path))
        self.assertEqual(0, zip2np("JS3651", "2018-04-11", path))
        self.assertEqual(0, zip2np("", "2018-04-11", path))
        #input wrong date
        self.assertEqual(0, zip2np("JS39-65", "2018-04-111", path))
        self.assertEqual(0, zip2np("JS39-65", "2018-041", path))
        self.assertEqual(0, zip2np("JS39-65", "20184-111", path))
        self.assertEqual(0, zip2np("JS39-65", "201111", path))
        self.assertEqual(0, zip2np("JS39-65", "", path))
        #input wrong path
        self.assertEqual(0, zip2np("JS39-65", "2018-04-11", "user/desktop"))
        self.assertEqual(0, zip2np("JS39-65", "2018-04-11", "user1/"))
        self.assertEqual(0, zip2np("JS39-65", "2018-04-11", "user2/"))
        self.assertEqual(0, zip2np("JS39-65", "2018-04-11", ""))
        shutil.rmtree(file_name)

if __name__ == '__main__':
    unittest.main()
