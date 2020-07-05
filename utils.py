from os.path import join
import torch


def save_checkpoint(tag, model, optimizer, args):
    print('Snapshot Checkpoint...')
    if args.device_ids and len(args.device_ids) > 1:
        model_state_dict = model.module.state_dict()
    else:
        model_state_dict = model.state_dict()

    torch.save({
        'model': model_state_dict,
        'optimizer': optimizer.state_dict()
    }, join(args.save_dir, 'checkpoint_' + str(tag) + '.pth'))


def load_checkpoint(ckpt_file, model, optimizer, args):
    state_dict = torch.load(ckpt_file, map_location='cpu')
    if args.device_ids and len(args.device_ids) > 1:
        model.module.load_state_dict(state_dict['model'])
    else:
        model.load_state_dict(state_dict['model'])
    optimizer.load_state_dict(state_dict['optimizer'])
