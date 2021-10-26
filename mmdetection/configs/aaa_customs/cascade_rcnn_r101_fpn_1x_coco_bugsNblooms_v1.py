_base_ = './cascade_rcnn_r50_fpn_1x_coco.py'
model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='torchvision://resnet101')))

classes = ('Insect', 'Flower')
data = dict(
    train = dict(
        img_prefix = '/bound_data/datasets/labeled/fiftyone/projected/remapped/train/data/')
        classes = classes,
        ann_file = 'labels.json'),
    val = dict(
        img_prefix = '/bound_data/datasets/labeled/fiftyone/projected/remapped/val/data/',
        classes = classes,
        ann_file = 'labels.json'),
    test = dict(
        img_prefix = '/bound_data/datasets/labeled/fiftyone/projected/remapped/test/data/',
        classes = classes,
        ann_file = 'labels.json'))

# Load from pretrained..
load_from = '/bound_data/models/pretrained/cascade_mask_rcnn_r101_fpn_1x_coco_20200203-befdf6ee.pth'