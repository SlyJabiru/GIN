import os
import subprocess
import sys
import threading

def output_reader(proc, file):
    while True:
        byte = proc.stdout.read(1)
        if byte:
            sys.stdout.buffer.write(byte)
            sys.stdout.flush()
            file.buffer.write(byte)
        else:
            break


arg_list = [
    '/Users/leeseungjoon/Downloads/cll/work/03/',
    '/Users/leeseungjoon/Downloads/cll/work/04/',
    '/Users/leeseungjoon/Downloads/cll/work/05/',
    '/Users/leeseungjoon/Downloads/cll/work/02/',
    '/Users/leeseungjoon/Downloads/cll/work/11/',
    '/Users/leeseungjoon/Downloads/cll/work/10/',
    '/Users/leeseungjoon/Downloads/cll/work/07/',
    '/Users/leeseungjoon/Downloads/cll/work/09/',
    '/Users/leeseungjoon/Downloads/cll/work/08/',
    '/Users/leeseungjoon/Downloads/cll/work/01/',
    '/Users/leeseungjoon/Downloads/cll/work/06/',
    '/Users/leeseungjoon/Downloads/cll/work/010/',
    '/Users/leeseungjoon/Downloads/cll/work/12/'
]


with subprocess.Popen(['python3', 'img_crop_save.py', arg_list[0]], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc0, \
     subprocess.Popen(['python3', 'img_crop_save.py', arg_list[1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc1, \
     subprocess.Popen(['python3', 'img_crop_save.py', arg_list[2]], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc2, \
     subprocess.Popen(['python3', 'img_crop_save.py', arg_list[3]], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc3, \
     subprocess.Popen(['python3', 'img_crop_save.py', arg_list[4]], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc4, \
     subprocess.Popen(['python3', 'img_crop_save.py', arg_list[5]], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc5, \
     subprocess.Popen(['python3', 'img_crop_save.py', arg_list[6]], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc6, \
     subprocess.Popen(['python3', 'img_crop_save.py', arg_list[7]], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc7, \
     subprocess.Popen(['python3', 'img_crop_save.py', arg_list[8]], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc8, \
     subprocess.Popen(['python3', 'img_crop_save.py', arg_list[9]], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc9, \
     open('log0.log', 'w') as file0, \
     open('log1.log', 'w') as file1, \
     open('log2.log', 'w') as file2, \
     open('log3.log', 'w') as file3, \
     open('log4.log', 'w') as file4, \
     open('log5.log', 'w') as file5, \
     open('log6.log', 'w') as file6, \
     open('log7.log', 'w') as file7, \
     open('log8.log', 'w') as file8, \
     open('log9.log', 'w') as file9:
     # open('log10.log', 'w') as file10, \
     # open('log11.log', 'w') as file11, \
     # open('log12.log', 'w') as file12:
    # subprocess.Popen(['./img_crop_save.py', arg_list[10]], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc10, \
    # subprocess.Popen(['./img_crop_save.py', arg_list[11]], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc11, \
    # subprocess.Popen(['./img_crop_save.py', arg_list[12]], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc12, \

    t0 = threading.Thread(target=output_reader, args=(proc0, file0))
    t1 = threading.Thread(target=output_reader, args=(proc1, file1))
    t2 = threading.Thread(target=output_reader, args=(proc2, file2))
    t3 = threading.Thread(target=output_reader, args=(proc3, file3))
    t4 = threading.Thread(target=output_reader, args=(proc4, file4))
    t5 = threading.Thread(target=output_reader, args=(proc5, file5))
    t6 = threading.Thread(target=output_reader, args=(proc6, file6))
    t7 = threading.Thread(target=output_reader, args=(proc7, file7))
    t8 = threading.Thread(target=output_reader, args=(proc8, file8))
    t9 = threading.Thread(target=output_reader, args=(proc9, file9))
    # t10 = threading.Thread(target=output_reader, args=(proc10, file10))
    # t11 = threading.Thread(target=output_reader, args=(proc11, file11))
    # t12 = threading.Thread(target=output_reader, args=(proc12, file12))

    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    # t10.start()
    # t11.start()
    # t12.start()

    t0.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    # t10.join()
    # t11.join()
    # t12.join()
