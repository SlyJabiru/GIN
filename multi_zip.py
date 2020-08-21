from multiprocessing import Process

from os import system, getpid



def execute(cmd):
    proc = getpid()
    # print(cmd)
    system(cmd)
    print(f'End of job. folder: {cmd}, process id: {proc}')


arg_dict = {
    '4111': ['/home/gcp_study_sjlee/for-image-crop-bucket/4111/01/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4111/02/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4111/03/cropped/'],
    '4112': ['/home/gcp_study_sjlee/for-image-crop-bucket/4112/01/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4112/02/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4112/03/cropped/'],
    '4113': ['/home/gcp_study_sjlee/for-image-crop-bucket/4113/01/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4113/02/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4113/03/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4113/04/cropped/'],
    '4114': ['/home/gcp_study_sjlee/for-image-crop-bucket/4114/01/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4114/02/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4114/03/cropped/'],
    '4115': ['/home/gcp_study_sjlee/for-image-crop-bucket/4115/01/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4115/02/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4115/03/cropped/'],
    '4126': ['/home/gcp_study_sjlee/for-image-crop-bucket/4126/01/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4126/02/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4126/03/cropped/'],
    '4127': ['/home/gcp_study_sjlee/for-image-crop-bucket/4127/01/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4127/02/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4127/03/cropped/'],
    '4128': ['/home/gcp_study_sjlee/for-image-crop-bucket/4128/01/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4128/02/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4128/03/cropped/',
             '/home/gcp_study_sjlee/for-image-crop-bucket/4128/04/cropped/']
}
if __name__ == '__main__':
    targets = []

    for k in arg_dict:
        path_list = arg_dict[k]

        list_str = ' '.join(path_list)
        target = f'zip -r {k}.zip {list_str}'
        targets.append(target)

    procs = []

    for target in targets:
        proc = Process(target=execute, args=(target,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
