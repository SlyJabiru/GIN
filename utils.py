from os.path import join
import torch


def save_checkpoint(tag, model, optimizer, multi_gpu, save_dir):
    print('Snapshot Checkpoint...')
    if multi_gpu:
        model_state_dict = model.module.state_dict()
    else:
        model_state_dict = model.state_dict()

    torch.save({
        'model': model_state_dict,
        'optimizer': optimizer.state_dict()
    }, join(save_dir, 'checkpoint_' + str(tag) + '.pth'))


def load_checkpoint(file, model, optimizer, multi_gpu):
    state_dict = torch.load(file, map_location='cpu')
    if multi_gpu:
        model.module.load_state_dict(state_dict['model'])
    else:
        model.load_state_dict(state_dict['model'])
    optimizer.load_state_dict(state_dict['optimizer'])
