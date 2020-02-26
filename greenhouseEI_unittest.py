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
        self.assertEqual(1, info("71-001-Sesame-D-1", "2019-07-03", path))
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
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        self.assertEqual(1, unzip("JS39-65", "2018-04-11", "Hyp", path))
        self.assertEqual(1, unzip("71-001-Sesame-D-1", "2019-07-03", "Hyp", path))
        files = os.listdir(path)
        for file in files:
            if ("JS39-65" in file) and ("2018-04-11" in file) and (".zip" not in file) and (".npy" not in file):
                js_folder = file
                print(js_folder)
                shutil.rmtree(js_folder)
            if ("71-001-Sesame-D-1" in file) and (".zip" not in file) and (".npy" not in file):
                sesame_folder = file
                print(sesame_folder)
                shutil.rmtree(sesame_folder)

        #input wrong plantID
        self.assertEqual(0, unzip("JS3965", "2018-04-11", "Hyp", path))
        self.assertEqual(0, unzip("JS9-65", "2018-04-11", "Hyp", path))
        self.assertEqual(0, unzip("J39-65", "2018-04-11", "Hyp", path))
        self.assertEqual(0, unzip("", "2018-04-11", "Hyp", path))

        #input wrong image type
        self.assertEqual(0, unzip("JS39-65", "2018-0411", "yp", path))
        self.assertEqual(0, unzip("JS39-65", "2018-0411", "Hp", path))
        self.assertEqual(0, unzip("JS39-65", "2018-0411", "Hy", path))
        self.assertEqual(0, unzip("JS39-65", "2018-0411", "", path))
        #input wrong path
        self.assertEqual(0, unzip("JS39-65", "2018-0411", "Hyp", "user/"))
        self.assertEqual(0, unzip("JS39-65", "2018-0411", "Hyp", "user/desk1"))
        self.assertEqual(0, unzip("JS39-65", "2018-0411", "Hyp", "user/desk2"))
        self.assertEqual(0, unzip("JS39-65", "2018-0411", "Hyp", ""))

    #test preprocess fuction
    #when you run this test function, there should be the Hyp folder in the folder
    def test_preprocess(self):
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        unzip("JS39-65", "2018-04-11", "Hyp", path)
        unzip("71-001-Sesame-D-1", "2019-07-03", "Hyp", path)
        self.assertEqual(1, preprocess("JS39-65", "2018-04-11", path))
        self.assertEqual(1, preprocess("71-001-Sesame-D-1", "2019-07-03", path))

        files = os.listdir(path)
        for file in files:
            if ("JS39-65" in file) and ("2018-04-11" in file) and (".zip" not in file) and (".npy" not in file):
                js_folder = file
                print(js_folder)
                shutil.rmtree(js_folder)
                js_npy_name = js_folder.split("_")[2] + "_" + js_folder.split("_")[3]
                js_npy_name = js_npy_name + ".npy"
                os.remove(js_npy_name)

            if ("71-001-Sesame-D-1" in file) and (".zip" not in file) and (".npy" not in file):
                sesame_folder = file
                print(sesame_folder)
                shutil.rmtree(sesame_folder)
                sesame_npy_name = "71-001-Sesame-D-1_2019-07-03.npy"
                os.remove(sesame_npy_name)

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
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        print(path)
        self.assertEqual(1, zip2np("JS39-65", "2018-04-11", path))
        self.assertEqual(1, zip2np("71-001-Sesame-D-1", "2019-07-03", path))

        files = os.listdir(path)
        for file in files:
            if ("JS39-65" in file) and ("2018-04-11" in file) and (".zip" not in file) and (".npy" not in file):
                js_folder = file
                print(js_folder)
                shutil.rmtree(js_folder)
                js_npy_name = js_folder.split("_")[2] + "_" + js_folder.split("_")[3]
                js_npy_name = js_npy_name + ".npy"
                os.remove(js_npy_name)
            if ("71-001-Sesame-D-1" in file) and (".zip" not in file) and (".npy" not in file):
                sesame_folder = file
                print(sesame_folder)
                shutil.rmtree(sesame_folder)
                sesame_npy_name = "71-001-Sesame-D-1_2019-07-03.npy"
                os.remove(sesame_npy_name)


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

if __name__ == '__main__':
    unittest.main()
